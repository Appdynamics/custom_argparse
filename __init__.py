# Copyright 2016, AppDynamics, Inc. and its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

"""

# __version__ = "$Revision$"

# $Id$

import argparse
import sys


class ArgumentParser(argparse.ArgumentParser):
    """Subclass of
    https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
    Overrides print_usage(), print_help(), and error() to allow for explicit
    control over the format of a calling utility's description and usage strings.
    """
    def __init__(
            self,
            description,
            usage,
            prog=None,
            epilog=None,
            parents=[],
            formatter_class=argparse.HelpFormatter,
            prefix_chars='-',
            fromfile_prefix_chars=None,
            argument_default=None,
            conflict_handler='error',
            add_help=True
    ):
        """Similar to
        https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        However, the description and usage_str fields are required.
        :param str description: Formatted string describing what the calling \
        program does.
        :param str usage: Formatted string containing flags, arguments and \
        their descriptions for the calling program.
        :param prog: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param epilog: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param parents: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param formatter_class: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param prefix_chars: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param fromfile_prefix_chars:  See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param argument_default: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param conflict_handler: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :param add_help: See https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser
        :return: a new ArgumentParser object
        """
        argparse.ArgumentParser.__init__(
            self,
            prog=prog,
            usage=usage,
            description=description,
            epilog=epilog,
            parents=parents,
            formatter_class=formatter_class,
            prefix_chars=prefix_chars,
            fromfile_prefix_chars=fromfile_prefix_chars,
            argument_default=argument_default,
            conflict_handler=conflict_handler,
            add_help=add_help
        )

    def print_usage(self, fd=None):
        if fd is None:
            fd = sys.stderr
        self._print_message(self.usage, fd)

    def print_help(self, fd=None):
        if fd is None:
            fd = sys.stderr
        self._print_message('\n' + self.description + '\n' + self.usage, fd)

    def error(self, message):
        self._print_message("error: {0}\n\n".format(message), sys.stderr)
        self.print_usage()
        self.exit(2)