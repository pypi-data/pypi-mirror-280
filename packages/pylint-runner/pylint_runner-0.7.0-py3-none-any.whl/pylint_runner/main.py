#!/usr/bin/env python
"""
Runs pylint on all contained python files in this directory, printint out
nice colorized warnings/errors without all the other report fluff
"""

from argparse import ArgumentParser
import configparser
import os
import sys

import colorama
import pylint
import pylint.lint

from . import __version__
from .utils import get_files_from_dir, get_pylint_kwargs

PYTHON_VERSION = ".".join([str(x) for x in sys.version_info[0:3]])


class Runner:
    """ A pylint runner that will lint all files recursively from the CWD. """

    DEFAULT_IGNORE_FOLDERS = [".git", ".idea", "__pycache__"]
    DEFAULT_ARGS = ["--reports=n", "--output-format=colorized"]
    DEFAULT_RCFILE = ".pylintrc"

    def __init__(self, args=None):
        if args is None:
            args = []

        colorama.init(autoreset=True)

        self.verbose = False
        self.args = self.DEFAULT_ARGS
        self.rcfile = self.DEFAULT_RCFILE
        self.ignore_folders = self.DEFAULT_IGNORE_FOLDERS

        self._parse_args(args)
        self._parse_ignores()

    def is_using_default_rcfile(self):
        """ Check if the rcfile is the default rcfile. """
        return self.rcfile == os.getcwd() + "/" + self.DEFAULT_RCFILE

    def _parse_args(self, args):
        """Parses any supplied command-line args and provides help text. """

        parser = ArgumentParser(
            description="Runs pylint recursively on a directory"
        )

        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            action="store_true",
            default=False,
            help="Verbose mode (report which files were found for testing).",
        )

        parser.add_argument(
            "--rcfile",
            dest="rcfile",
            action="store",
            default=".pylintrc",
            help="A relative or absolute path to your pylint rcfile. Defaults to\
                            `.pylintrc` at the current working directory",
        )

        parser.add_argument(
            "-V",
            "--version",
            action="version",
            version=f"%(prog)s ({__version__}) for Python {PYTHON_VERSION}",
        )

        options, rest = parser.parse_known_args(args)

        self.verbose = options.verbose

        if options.rcfile:
            if not os.path.isfile(options.rcfile):
                options.rcfile = os.getcwd() + "/" + options.rcfile
            self.rcfile = options.rcfile

        self.args += rest

        return options

    def _parse_ignores(self):
        """ Parse the ignores setting from the pylintrc file if available. """

        error_message = (
            colorama.Fore.RED
            + f"{self.rcfile} does not appear to be a valid pylintrc file"
            + colorama.Fore.RESET
        )

        if not os.path.isfile(self.rcfile):
            if not self.is_using_default_rcfile():
                print(error_message)
                sys.exit(1)
            else:
                return

        config = configparser.ConfigParser()
        try:
            config.read(self.rcfile)
        except configparser.MissingSectionHeaderError:
            print(error_message)
            sys.exit(1)

        if config.has_section("MASTER") and config.get("MASTER", "ignore"):
            self.ignore_folders += config.get("MASTER", "ignore").split(",")

    def _print_line(self, line):
        """ Print output only with verbose flag. """
        if self.verbose:
            print(line)

    def run(self, output=None, error=None):
        """ Runs pylint on all python files in the current directory """

        pylint_output = output if output is not None else sys.stdout
        pylint_error = error if error is not None else sys.stderr
        savedout, savederr = sys.__stdout__, sys.__stderr__
        sys.stdout = pylint_output
        sys.stderr = pylint_error

        pylint_files = get_files_from_dir(os.curdir, self.ignore_folders)
        print(
            "Using pylint "
            + colorama.Fore.RED
            + pylint.__version__
            + colorama.Fore.RESET
            + " for python "
            + colorama.Fore.RED
            + PYTHON_VERSION
            + colorama.Fore.RESET,
            file=sys.stdout
        )

        self._print_line("pylint running on the following files:")
        for pylint_file in pylint_files:
            # we need to recast this as a string, else pylint enters an
            # endless recursion
            split_file = str(pylint_file).split("/")
            split_file[-1] = colorama.Fore.CYAN + split_file[-1] \
                + colorama.Fore.RESET
            pylint_file = "/".join(split_file)
            self._print_line("- " + pylint_file)
        self._print_line("----")

        if not self.is_using_default_rcfile():
            # insert this at the front so it's not after any potential
            # positional arguments
            self.args.insert(0, f"--rcfile={self.rcfile}")

        exit_kwarg = get_pylint_kwargs(pylint.__version__)

        run = pylint.lint.Run(self.args + pylint_files, **exit_kwarg)
        sys.stdout = savedout
        sys.stderr = savederr

        sys.exit(run.linter.msg_status)


def main(output=None, error=None, verbose=False, args=None):
    """ The main (cli) interface for the pylint runner. """
    if args is None:
        args = sys.argv[1:]
    if verbose and '--verbose' not in args:
        args.insert(0, '--verbose')
    runner = Runner(args)
    runner.run(output, error)


if __name__ == "__main__":
    main(verbose=True)
