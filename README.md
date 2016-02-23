# custom_argparse

## Summary

The [argparse](https://docs.python.org/2/library/argparse.html) module in Python's standard library is incredibly useful, but the default formatting of its help and usage messages leaves much to be desired.  `custom_argparse` sublcasses [argparse.ArgumentParser](https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser) to allow the developer more control over the formatting of help and usage messages in command-line programs.

## Typical Use Case

The following instructions assume that you are adding custom_argparse to an existing git repository.

* Create a `lib` a somewhere in your project.
* Change directories into `lib` and run the command: `git submodule add https://github.com/Appdynamics/custom_argparse.git`
* Add your `lib` directory to the list of paths at python searches for modules it can import.  `import custom_argparse`.  Create an instance of `custom_argparse.ArgumentParser` and use it just as you would use its super-class.

### Example Code:

```
# for constants like argparse.SUPPRESS
import argparse

sys.path.append(
        os.path.join(sys.path[0], 'lib')
)
import custom_argparse

DESCRIPTION = """\
NOBODY expects the Spanish Inquisition! Our chief weapon is surprise...surprise
and fear...fear and surprise.... Our two weapons are fear and surprise...and
ruthless efficiency.... Our *three* weapons are fear, surprise, and ruthless
efficiency...and an almost fanatical devotion to the Pope.... Our *four*...
no... *Amongst* our weapons.... Amongst our weaponry...are such elements as
fear, surprise....
"""

USAGE = """\
Usage: spanish-inqusition.py
Options:
    -r | --rack             Now, Cardinal -- the rack!
    -t | --turn [n]         Cardinal, give the rack [oh dear] give the rack a
                            turn. (Where n is an optional, positive number of
                            turns.)
    -s | --soft-cushion     Poke her with the soft cushions!
    -c | --comfy-chair      Put her in the Comfy Chair!
    -h | --help             Print help message and exit.
"""


# Set up command line arg parser.
#
# Be careful here. add_help=True causes the program to immediately print the
# help message and exit(0) when cmdline.parse_args() is called and it
# encounters '-h' or '--help'.  Explicitly add -h / --help with
# cmdline.add_argument() and choose an action other than 'help' if you want
# other behavior.
#
cmdline = custom_argparse.ArgumentParser(
    description=DESCRIPTION,
    usage_str=USAGE_STR,
    add_help=True
)

# cmdline.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required]
#   [, help][, metavar][, dest])
cmdline.add_argument('-r', '--rack', action='store_true', required=False)
cmdline.add_argument('-t', '--turn', nargs='?', default=argparse.SUPPRESS required=False)
cmdline.add_argument('-s', '--soft-cushion', action='store_true', required=False)
cmdline.add_argument('-c', '--comfy-chair', action='store_true', required=False)

args = cmdline.parse_args()

if args.turn:
    if not args.rack:
        sys.stderr.write("Error: There is no rack to turn.")
        exit(1)
    turns = args.turn[0] if args.turn[0] else 1
# ...

if args.soft_cushion:
    sys.stderr.write("Do your worst!")
```


## Contributing

### Required Tools:

* [gitflow-avh](https://github.com/petervanderdoes/gitflow-avh)
* [Sphinx Python Documentation Generator](http://www.sphinx-doc.org/en/stable/install.html)

### Recommended Tools:

* [PyCharm](https://www.jetbrains.com/pycharm/) Professional or Community Edition