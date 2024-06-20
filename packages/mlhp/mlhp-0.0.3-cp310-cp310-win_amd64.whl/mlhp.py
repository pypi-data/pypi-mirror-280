# This file is part of the mlhp project. License: See LICENSE

import os, sys, ast

try:
    # mlhp.py script folder
    path = os.path.abspath( os.path.dirname(sys.argv[0]) );
    
    # Try to open path/mlhpPythonPath containing the python module path. This
    # file is written as post build command after compiling pymlhpcore.
    with open( os.path.join( path, 'mlhpPythonPath' ), 'r') as f:
        sys.path.append( os.path.normpath( f.read( ).splitlines( )[0] ) )
   
except IOError: 
    pass

from pymlhpcore import *
from pymlhpcore import _scalarFieldFromTree, _scalarFieldFromAddress, _domainIntegrandFromAddress

def _iterativeSolve(internalSolve, matrix, rhs, preconditioner, maxit, tolerance, residualNorms):
    maximumNumberOfIterations = len( rhs ) if maxit is None else maxit
    
    M = makeMultiply( matrix ) if isinstance(matrix, AbsSparseMatrix) else matrix
    
    if preconditioner is None:
        P = makeNoPreconditioner( len( rhs ) )
    elif isinstance(preconditioner, AbsSparseMatrix):
        P = makeMultiply( preconditioner )
    else:
        P = preconditioner
     
    [solution, residuals] = internalSolve( M, rhs, P, maximumNumberOfIterations, tolerance );
    
    return [solution, residuals] if residualNorms else solution
    
def cg( matrix, rhs, preconditioner=None, maxit=None, tolerance=1e-8, residualNorms=False ):
    return _iterativeSolve(internalCG, matrix, rhs, preconditioner, maxit, tolerance, residualNorms)

def bicgstab( matrix, rhs, preconditioner=None, maxit=None, tolerance=1e-8, residualNorms=False ):
    return _iterativeSolve(internalBiCGStab, matrix, rhs, preconditioner, maxit, tolerance, residualNorms)

def makeScalars( n, value=0.0 ):
    return [ScalarDouble( value ) for _ in range( n )]
    
def writeBasisOutput(basis, postmesh=None, writer=VtuOutput("output.vtu"), processors=[]):
    kwargs = {'basis': basis, 'writer' : writer}
    
    if postmesh is not None:
        kwargs['postmesh'] = postmesh
    if len(processors) > 0:
        convert = lambda p : type(p).__name__[:-2] != 'ElementProcessor'
        kwargs['processors'] = [(convertToElementProcessor(p) if convert(p) else p) for p in processors]
            
    internalWriteBasisOutput(**kwargs)
 
def writeMeshOutput(mesh, postmesh=None, writer=VtuOutput("output.vtu"), processors=[]):
    kwargs = {'mesh': mesh, 'writer' : writer}
    
    if postmesh is not None:
        kwargs['postmesh'] = postmesh
    if len(processors) > 0:
        kwargs['processors'] = processors
            
    internalWriteMeshOutput(**kwargs)
 
def _parseFunction(expr):
    tree, tokens = ast.parse(expr).body, []
    
    def _convert(node):
        id = _convert.index
        _convert.index += 1
        if isinstance(node, ast.AST):
            nodeType = node.__class__.__name__
            if nodeType == "Constant":
                tokens.append([id, nodeType, str(node.value)])
            elif nodeType == "BinOp":
                tokens.append([id, nodeType, node.op.__class__.__name__, _convert(node.left), _convert(node.right)])
            elif nodeType == "BoolOp" and len(node.values) == 2:
                tokens.append([id, nodeType, node.op.__class__.__name__, _convert(node.values[0]), _convert(node.values[1])])
            elif nodeType == "Compare" and len(node.comparators) == 1:
                tokens.append([id, nodeType, node.ops[0].__class__.__name__, _convert(node.left), _convert(node.comparators[0])])
            elif nodeType == "Call":
                tokens.append([id, nodeType, node.func.id] + [_convert(arg) for arg in node.args])
            elif nodeType == "Name" and node.id in {'x', 'y', 'z', 'r', 's', 't'}:
                tokens.append([id, "Input", str( { 'x' : 0, 'y' : 1, 'z' : 2, 'r' : 0, 's' : 1, 't' : 2 }[node.id] ) ])
            elif nodeType == "Subscript" and isinstance(node.slice, ast.Constant):
                tokens.append([id, "Input", str(node.slice.value)])
            elif nodeType == "UnaryOp":
                tokens.append([id, nodeType, node.op.__class__.__name__, _convert(node.operand)])
            elif nodeType == "IfExp":
                tokens.append([id, "Call", "select", _convert(node.test), _convert(node.body), _convert(node.orelse)])
            elif nodeType == "Num": # Legacy python 3.7
                tokens.append([id, "Constant", str(node.n)])
            elif nodeType == "Subscript" and node.slice.__class__.__name__ == "Index": # Legacy python 3.7
                tokens.append([id, "Input", str(node.slice.value.n)])
            else:
                raise(ValueError("Expression of type \"" + nodeType + "\" is not supported."))
        return str(id)
    
    if len(tree) == 0:
        raise ValueError("Empty expression string.")
    
    _convert.index = 0
    _convert(tree[0].value)
    
    return [token[1:] for token in sorted(tokens, key=lambda token : token[0])]
    
def scalarField(ndim, func=None, address=None):
    if address is not None:
        if func is not None: raise ValueError("Both function and address given.")
        return _scalarFieldFromAddress(ndim, address)
    if hasattr(func, "address"):
        return _scalarFieldFromAddress(ndim, func.address)
    if isinstance(func, (bool, int, float)):
        return _scalarFieldFromTree(ndim, _parseFunction(str(float(func))))
    if isinstance(func, str):
        return _scalarFieldFromTree(ndim, _parseFunction(func))
    raise ValueError("No useful function input parameter.")
 
def implicitFunction(ndim, func=None, address=None):
    return implicitThreshold(scalarField(ndim, func, address), 0.5)
 
def domainIntegrand(ndim, callback, types, maxdiff, tmpdofs=0):
    return _domainIntegrandFromAddress(ndim, callback.address, types, maxdiff, tmpdofs) 
    
del os, sys, path
