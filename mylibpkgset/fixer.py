from martialaw.martialaw import martialaw as _closer
from sys import argv as a
from os.path import splitext as _s
_o = open
@_closer
def fixer(fun, fil):
    with _o(f'{_s(fil}.py','w') as w:
        with _o(fil) as r:fun(w,r)