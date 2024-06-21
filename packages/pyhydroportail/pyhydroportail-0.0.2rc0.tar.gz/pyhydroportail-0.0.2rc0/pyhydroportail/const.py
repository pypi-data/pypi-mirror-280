EXPORT_VARIABLES_TYPES = {
    "simple": ("simple_and_interpolated_and_hourly_variable", "simpleAndInterpolatedAndHourlyVariable"),
    "daily_variable": ("daily_variable", "dailyVariable"),
    "monthly_variable": ("monthly_variable", "monthlyVariable"),
}

EXPORT_VARIABLES = {
    "H": {
        "human_value": "Hauteur instantannée",
        "variable_type": EXPORT_VARIABLES_TYPES["simple"],
        "require_dt": False,
    },
    "Q": {"human_value": "Débit instantannée", "variable_type": EXPORT_VARIABLES_TYPES["simple"], "require_dt": False},
    "Hln": {
        "human_value": "Hauteur interpolées toutes les N minutes",
        "variable_type": EXPORT_VARIABLES_TYPES["simple"],
        "require_dt": True,
    },
    "Qln": {
        "human_value": "Débit interpolés toutes les N minutes",
        "variable_type": EXPORT_VARIABLES_TYPES["simple"],
        "require_dt": True,
    },
    "QmnH": {
        "human_value": "Débit moyen N horaire",
        "variable_type": EXPORT_VARIABLES_TYPES["simple"],
        "require_dt": True,
    },
    "HlNnJ": {
        "human_value": "Hauteur instantanée minimale N journalière",
        "variable_type": EXPORT_VARIABLES_TYPES["daily_variable"],
        "require_dt": True,
    },
    "HlXnJ": {
        "human_value": "Hauteur instantanée maximale N journalière",
        "variable_type": EXPORT_VARIABLES_TYPES["daily_variable"],
        "require_dt": True,
    },
    "QmnJ": {
        "human_value": "Débit moyen sur N jours",
        "variable_type": EXPORT_VARIABLES_TYPES["daily_variable"],
        "require_dt": True,
    },
    "QlNJ": {
        "human_value": "Débit instantané minimal N journalier",
        "variable_type": EXPORT_VARIABLES_TYPES["daily_variable"],
        "require_dt": True,
    },
    "QlXJ": {
        "human_value": "Débit instantané minimal N journalier",
        "variable_type": EXPORT_VARIABLES_TYPES["daily_variable"],
        "require_dt": True,
    },
    "HINM": {
        "human_value": "Hauteur instantanée minimale mensuelle",
        "variable_type": EXPORT_VARIABLES_TYPES["monthly_variable"],
        "require_dt": False,
    },
    "HIXM": {
        "human_value": "Hauteur instantanée maximale mensuelle",
        "variable_type": EXPORT_VARIABLES_TYPES["monthly_variable"],
        "require_dt": False,
    },
    "QmM": {
        "human_value": "Débit moyen mensuel",
        "variable_type": EXPORT_VARIABLES_TYPES["monthly_variable"],
        "require_dt": False,
    },
    "QINM": {
        "human_value": "Débit instantané minimal mensuel",
        "variable_type": EXPORT_VARIABLES_TYPES["monthly_variable"],
        "require_dt": False,
    },
    "QIXM": {
        "human_value": "Débit instantané minimal mensuel",
        "variable_type": EXPORT_VARIABLES_TYPES["monthly_variable"],
        "require_dt": False,
    },
}
