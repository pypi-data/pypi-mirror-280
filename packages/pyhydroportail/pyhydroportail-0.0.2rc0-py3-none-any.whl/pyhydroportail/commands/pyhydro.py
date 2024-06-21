import logging
import sys

try:
    import importlib_metadata
except ModuleNotFoundError:  # pragma: nocover
    import importlib.metadata as importlib_metadata

import pyhydroportail.actions.export
import pyhydroportail.actions.hcrm
import pyhydroportail.actions.info
import pyhydroportail.actions.search
from pyhydroportail.commands.arguments import parse_arguments

logger = logging.getLogger(__name__)


def run_actions(arguments):
    global_arguments = arguments["global"]

    for action_name, action_arguments in arguments.items():
        if action_name == "search":
            pyhydroportail.actions.search.run_search(global_arguments, action_arguments)
        elif action_name == "info":
            pyhydroportail.actions.info.run_info(global_arguments, action_arguments)
        elif action_name == "export":
            pyhydroportail.actions.export.run_export(global_arguments, action_arguments)
        elif action_name == "hcrm":
            pyhydroportail.actions.hcrm.run_hcrm(global_arguments, action_arguments)


def exit_with_help_link():  # pragma: no cover
    """
    Display a link to get help and exit with an error code.
    """
    logger.critical("")
    logger.critical("TODO")
    sys.exit(1)


def main():
    try:
        arguments = parse_arguments(*sys.argv[1:])
    except ValueError as error:
        logger.critical(error)
        exit_with_help_link()

    global_arguments = arguments["global"]
    if global_arguments.version:
        print(importlib_metadata.version("pyhydroportail"))
        sys.exit(0)

    try:
        run_actions(arguments)
    except ValueError as error:
        print(error)
        sys.exit(1)
