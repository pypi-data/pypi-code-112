""" This module cooks up a docstring when imported. Its only purpose is to
    be displayed in the sphinx documentation. """


from typing import Any, Dict as tDict, List, Tuple as tTuple, Type

from sympy.integrals.meijerint import _create_lookup_table
from sympy.core.add import Add
from sympy.core.relational import Eq
from sympy.core.symbol import Symbol
from sympy.printing.latex import latex

t = {}  # type: tDict[tTuple[Type, ...], List[Any]]
_create_lookup_table(t)

doc = ""

for about, category in sorted(t.items()):
    if about == ():
        doc += 'Elementary functions:\n\n'
    else:
        doc += 'Functions involving ' + ', '.join('`%s`' % latex(
            list(category[0][0].atoms(func))[0]) for func in about) + ':\n\n'
    for formula, gs, cond, hint in category:
        if not isinstance(gs, list):
            g = Symbol('\\text{generated}')
        else:
            g = Add(*[fac*f for (fac, f) in gs])
        obj = Eq(formula, g)
        if cond is True:
            cond = ""
        else:
            cond = ',\\text{ if } %s' % latex(cond)
        doc += ".. math::\n  %s%s\n\n" % (latex(obj), cond)

__doc__ = doc
