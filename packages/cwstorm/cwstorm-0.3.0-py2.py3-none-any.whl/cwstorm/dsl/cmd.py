from cwstorm.dsl.node import Node
import re


class Cmd(Node):
    """
    Cmd.

    A Cmd represents a single command line to be executed. Tasks hold a list of Cmds, and Cmd arguments are held in a list. Lists of commands in a task run in serial.
    """

    ORDER = 5
    ATTRS = {
        "argv": {
            "type": "list:str",
            "validator": re.compile(
                r"^[a-zA-Z0-9_@,\-\.\/\s%:*?<>$()+%'\"\[\]{}&|;~!#`]+$", re.IGNORECASE
            ),
        },
    }

    def __init__(self, *args):
        self.argv(*args)
