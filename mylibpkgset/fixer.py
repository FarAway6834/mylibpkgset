from martialaw.martialaw import martialaw as _closr
from sys import argv as _a
from os.path import splitext as _s
_o = open
@_closr
def fixer(fun, fil):
    with _o(f'{_s(fil}.py','w') as w:
        with _o(fil) as r:fun(w,r)
@_closr
def fixermain(fun, fil):
    fixer(fun)(fil[1])