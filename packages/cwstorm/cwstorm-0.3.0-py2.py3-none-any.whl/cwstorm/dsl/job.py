import re
import os
import platform
from cwstorm.dsl.dag_node import DagNode
from cwstorm import __schema_version__

 
def _get_username():
    """Return the username of the current user."""
    result = (
        os.environ.get("USERNAME")
        if platform.system() == "Windows"
        else os.environ.get("USER")
    )
    if not result:
        result = "unknown"
    return result


class Job(DagNode):
    """Job node.

    There's one job node in a graph. Conceptually, it is what the other nodes in the graph are working towards.
    """

    ORDER = 2
    ATTRS = {
        "comment": {
            "type": "str",
            "validator": re.compile(r'^[_a-z0-9 ,.!?\'"]+$', re.IGNORECASE),
        },
        "project": {
            "type": "str",
            "validator": re.compile(r"^[a-z0-9_\-\.\s]+$", re.IGNORECASE),
        },
        "author": {
            "type": "str",
            "validator": re.compile(r"^[a-z\s]+$", re.IGNORECASE),
            "default": _get_username()
        },
        "location": {
            "type": "str",
            "validator": re.compile(
                r"^(?:[a-z][a-z0-9]*$|([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$|^$)",
                re.IGNORECASE,
            ),
        },
        "schema_version": {
            "type": "str",
            "validator": re.compile(r"^\d{1,2}\.\d{1,2}.\d{1,2}$"),
            "default": __schema_version__,
        },
    }

    def is_original(self, _):
        """Always true."""
        return True

    def is_reference(self, _):
        """Always false."""
        return False
