import re
from cwstorm.dsl.dag_node import DagNode



class WorkNode(DagNode):
    
    BASE_ATTRS = {
        "initial_state": {
            "type": "str",
            "validator": re.compile(r"^(HOLD|START)$"),
            "default": "HOLD",
        }
    }
    ATTRS = {}
    ORDER = None
