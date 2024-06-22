__version__ = '0.1.0'

from .unit import *
from . import const
from . import mksa

def main():
    import code
    console = code.InteractiveConsole()
    console.runcode('''import readline
import rlcompleter
readline.parse_and_bind("tab: complete")
readline.set_completer(rlcompleter.Completer(locals()).complete)
import atexit
import os

histfile = os.path.join(os.path.expanduser("~"), ".python_history")
try:
    readline.read_history_file(histfile)
    # default history len is -1 (infinite), which may grow unruly
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)

from natunits.prelude import *
''')
    console.interact()