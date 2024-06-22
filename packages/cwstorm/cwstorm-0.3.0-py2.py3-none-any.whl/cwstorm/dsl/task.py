from cwstorm.dsl.work_node import WorkNode

# from cwstorm.dsl.cmd import Cmd
import re


class Task(WorkNode):
    """Task node.

    Tasks contain commands. They may be added to other Tasks as dependencies or to the Job..
    """

    ORDER = 3
    ATTRS = {
        "commands": {"type": "list:Cmd", },
        "hardware": {
            "type": "str",
            "validator": re.compile(r"^[a-z0-9_\-\.\s]+$", re.IGNORECASE),
        },
        "preemptible": {"type": "bool", "default": True},
        "env": {"type": "dict"},
        "lifecycle": {
            "type": "dict",
            "validator": {"keys": ["minsec", "maxsec"]},
            "default": {"minsec": 0, "maxsec": 3600},
        },
        "attempts": {
            "type": "int",
            "validator": {"min": 1, "max": 10},
            "default": 1,
        },
        "output_path": {"type": "str", "default": "/tmp"},
        "packages": {
            "type": "list:str",
            "validator": re.compile(r"^[a-fA-F0-9]{32}$"),
        },
    }
