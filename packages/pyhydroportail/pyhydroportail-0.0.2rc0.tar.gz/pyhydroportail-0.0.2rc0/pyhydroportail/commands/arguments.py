import collections
import itertools
import sys
from argparse import ArgumentParser

from pyhydroportail.const import EXPORT_VARIABLES

ACTION_ALIASES = {
    "search": ["-s"],
    "info": ["-I"],
    "export": [],
    "hcrm": [],
}


def get_subaction_parsers(action_parser):
    """
    Given an argparse.ArgumentParser instance, lookup the subactions in it and return a dict from
    subaction name to subaction parser.
    """
    if not action_parser._subparsers:
        return {}

    return {
        subaction_name: subaction_parser
        for group_action in action_parser._subparsers._group_actions
        for subaction_name, subaction_parser in group_action.choices.items()
    }


def get_subactions_for_actions(action_parsers):
    """
    Given a dict from action name to an argparse.ArgumentParser instance, make a map from action
    name to the names of contained sub-actions.
    """
    return {
        action: tuple(
            subaction_name
            for group_action in action_parser._subparsers._group_actions
            for subaction_name in group_action.choices.keys()
        )
        for action, action_parser in action_parsers.items()
        if action_parser._subparsers
    }


def omit_values_colliding_with_action_names(unparsed_arguments, parsed_arguments):
    """
    Given a sequence of string arguments and a dict from action name to parsed argparse.Namespace
    arguments, return the string arguments with any values omitted that happen to be the same as
    the name of a borgmatic action.

    This prevents, for instance, "check --only extract" from triggering the "extract" action.
    """
    remaining_arguments = list(unparsed_arguments)

    for action_name, parsed in parsed_arguments.items():
        for value in vars(parsed).values():
            if isinstance(value, str):
                if value in ACTION_ALIASES.keys():
                    remaining_arguments.remove(value)
            elif isinstance(value, list):
                for item in value:
                    if item in ACTION_ALIASES.keys():
                        remaining_arguments.remove(item)

    return tuple(remaining_arguments)


def parse_and_record_action_arguments(
    unparsed_arguments, parsed_arguments, action_parser, action_name, canonical_name=None
):
    """
    Given unparsed arguments as a sequence of strings, parsed arguments as a dict from action name
    to parsed argparse.Namespace, a parser to parse with, an action name, and an optional canonical
    action name (in case this the action name is an alias), parse the arguments and return a list of
    any remaining string arguments that were not parsed. Also record the parsed argparse.Namespace
    by setting it into the given parsed arguments. Return None if no parsing occurs because the
    given action doesn't apply to the given unparsed arguments.
    """
    filtered_arguments = omit_values_colliding_with_action_names(unparsed_arguments, parsed_arguments)

    if action_name not in filtered_arguments:
        return tuple(unparsed_arguments)

    parsed, remaining = action_parser.parse_known_args(filtered_arguments[1:])
    parsed_arguments[canonical_name or action_name] = parsed

    return tuple(argument for argument in remaining if argument != action_name)


def get_unparsable_arguments(remaining_action_arguments):
    """
    Given a sequence of argument tuples (one per action parser that parsed arguments), determine the
    remaining arguments that no action parsers have consumed.
    """
    if not remaining_action_arguments:
        return ()

    return tuple(
        argument
        for argument in dict.fromkeys(itertools.chain.from_iterable(remaining_action_arguments)).keys()
        if all(argument in action_arguments for action_arguments in remaining_action_arguments)
    )


def parse_arguments_for_actions(unparsed_arguments, action_parsers, global_parser):
    """
    Given a sequence of arguments, a dict from action name to argparse.ArgumentParser instance,
    and the global parser as a argparse.ArgumentParser instance, give each requested action's
    parser a shot at parsing all arguments. This allows common arguments like "--repository" to be
    shared across multiple action parsers.

    Return the result as a tuple of: (a dict mapping from action name to an argparse.Namespace of
    parsed arguments, a tuple of argument tuples where each is the remaining arguments not claimed
    by any action parser).
    """
    arguments = collections.OrderedDict()
    help_requested = bool("--help" in unparsed_arguments or "-h" in unparsed_arguments)
    remaining_action_arguments = []
    alias_to_action_name = {alias: action_name for action_name, aliases in ACTION_ALIASES.items() for alias in aliases}

    # Ask each action parser, one by one, to parse arguments.
    for argument in unparsed_arguments:
        action_name = argument
        canonical_name = alias_to_action_name.get(action_name, action_name)
        action_parser = action_parsers.get(action_name)

        if not action_parser:
            continue

        subaction_parsers = get_subaction_parsers(action_parser)

        # But first parse with subaction parsers, if any.
        if subaction_parsers:
            subactions_parsed = False

            for subaction_name, subaction_parser in subaction_parsers.items():
                remaining_action_arguments.append(
                    tuple(
                        argument
                        for argument in parse_and_record_action_arguments(
                            unparsed_arguments,
                            arguments,
                            subaction_parser,
                            subaction_name,
                        )
                        if argument != action_name
                    )
                )

                if subaction_name in arguments:
                    subactions_parsed = True

            if not subactions_parsed:
                if help_requested:
                    action_parser.print_help()
                    sys.exit(0)
                else:
                    msg = ", ".join(get_subactions_for_actions(action_parsers)[action_name])
                    raise ValueError(f"Missing sub-action after {action_name} action. Expected one of: {msg}")
        # Otherwise, parse with the main action parser.
        else:
            remaining_action_arguments.append(
                parse_and_record_action_arguments(
                    unparsed_arguments, arguments, action_parser, action_name, canonical_name
                )
            )

    arguments["global"], remaining = global_parser.parse_known_args(unparsed_arguments)
    remaining_action_arguments.append(remaining)

    return (
        arguments,
        tuple(remaining_action_arguments) if arguments else unparsed_arguments,
    )


def make_parsers():
    # Global
    global_parser = ArgumentParser(add_help=False)
    global_group = global_parser.add_argument_group("Arguments globaux")
    global_group.add_argument(
        "--version",
        dest="version",
        default=False,
        action="store_true",
        help="Affiche la version installée de pyHydroPortail et quitte",
    )

    global_plus_action_parser = ArgumentParser(
        description="""
            TODO
            """,
        parents=[global_parser],
    )
    action_parsers = global_plus_action_parser.add_subparsers(
        title="actions",
        metavar="",
        help="Spécifier une action. Utilser --help avec l'action pour les détails:",
    )

    # Search
    search_parser = action_parsers.add_parser(
        "search",
        aliases=ACTION_ALIASES["search"],
        help="Recherche les stations correspondantes au mot clé indiqué",
        description="Recherche les stations correspondantes au mot clé indiqué",
        add_help=False,
    )
    search_group = search_parser.add_argument_group("Argument de l'action search")
    search_group.add_argument(
        "mot_clé",
        help="Mot clé à rechercher",
        nargs="+",
    )
    search_group.add_argument(
        "--inclure-fermée",
        dest="include_closed",
        action="store_true",
        help="Afficher également les stations fermées.",
    )
    search_group.add_argument("-h", "--help", action="help", help="Affiche cette aide et quitte.")

    # Info
    info_parser = action_parsers.add_parser(
        "info",
        aliases=ACTION_ALIASES["info"],
        help="Affiche les informations du site ou de la station",
        description="Affiche les informations du site ou de la station",
        add_help=False,
    )
    info_group = info_parser.add_argument_group("Argument de l'action info")
    info_group.add_argument(
        "code",
        help="Code du site ou station",
    )
    info_group.add_argument(
        "-f",
        "--full",
        dest="include_closed",
        action="store_true",
        help="Affiche cette aide et quitte.",
    )
    info_group.add_argument("-h", "--help", action="help", help="Affiche cette aide et quitte.")

    # Export
    export_parser = action_parsers.add_parser(
        "export",
        aliases=ACTION_ALIASES["export"],
        help="Export des séries de données d'une station",
        description="Export des séries de données d'une station",
        add_help=False,
    )
    export_group = export_parser.add_argument_group("Argument de l'action export")
    export_group.add_argument(
        "code",
        help="Code du site ou station",
    )
    grandeur_help = "Grandeur à exporter. Choix possibles : "
    for key, value in EXPORT_VARIABLES.items():
        grandeur_help += f"{key} : {value['human_value']} -- "
    export_group.add_argument(
        "-g",
        "--grandeur",
        dest="grandeur",
        choices=list(EXPORT_VARIABLES.keys()),
        required=True,
        help=grandeur_help,
        metavar="",
    )
    export_group.add_argument(
        "-dt",
        "--intervalle-temps",
        dest="timestep",
        help="Pas de temps (minute, heure ou jour suivant la grandeur sélectionnée)",
    )
    export_group.add_argument(
        "-p",
        "--periodes",
        dest="periodes",
        required=True,
        action="append",
        help="Périodes à exporter",
    )
    export_group.add_argument(
        "--excel",
        help="Enregistre la ou les série(s) dans un fichier Excel",
    )
    export_group.add_argument(
        "-o",
        "--output-path",
        dest="output_path",
        help="Dossier de sortie",
    )
    export_group.add_argument(
        "--list",
        dest="output_as_list",
        action="store_true",
        help="Affiche les valeurs exportées dans le terminal. Le dossier de sortie sera ignoré.",
    )
    export_group.add_argument("-h", "--help", action="help", help="Affiche cette aide et quitte.")

    # Hydrogramme centré réduit moyen
    hcrm_parser = action_parsers.add_parser(
        "hcrm",
        aliases=ACTION_ALIASES["hcrm"],
        help="todo",
        description="todo",
        add_help=False,
    )
    hcrm_group = hcrm_parser.add_argument_group("Argument de l'action hcrm")
    hcrm_group.add_argument(
        "-i",
        "--input",
        dest="inputs",
        required=True,
        action="append",
        help="Fichier(s)/dossier d'entrée",
    )
    hcrm_group.add_argument(
        "-o",
        "--excel-name",
        dest="excel_name",
        required=True,
        help="Nom du fichier Excel de sortie",
    )
    return global_parser, action_parsers, global_plus_action_parser


def parse_arguments(*unparsed_arguments):
    # print(unparsed_arguments)
    global_parser, action_parsers, global_plus_action_parser = make_parsers()
    arguments, remaining_action_arguments = parse_arguments_for_actions(
        unparsed_arguments, action_parsers.choices, global_parser
    )
    # print(arguments)

    unknown_arguments = get_unparsable_arguments(remaining_action_arguments)

    if not unparsed_arguments:
        global_plus_action_parser.print_help()
        raise ValueError("Aucune action spécifiée")

    if unknown_arguments:
        if "--help" in unknown_arguments or "-h" in unknown_arguments:
            global_plus_action_parser.print_help()
            sys.exit(0)

        global_plus_action_parser.print_usage()
        raise ValueError(
            f"Unrecognized argument{'s' if len(unknown_arguments) > 1 else ''}: {' '.join(unknown_arguments)}"
        )

    NEED_TIMESTEP = [grandeur for grandeur, value in EXPORT_VARIABLES.items() if value["require_dt"]]
    if "export" in arguments and arguments["export"].grandeur in NEED_TIMESTEP and not arguments["export"].timestep:
        raise ValueError(f"La grandeur {arguments['export'].grandeur} nécessite le paramètre \"-dt\".")

    return arguments
