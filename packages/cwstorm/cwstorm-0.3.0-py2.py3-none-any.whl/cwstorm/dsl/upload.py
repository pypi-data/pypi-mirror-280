from cwstorm.dsl.work_node import WorkNode

import re


class Upload(WorkNode):
    """Upload node.

    Uploads contain lists of filepaths. They are a special kind of task and can be added anywhere a Task can be added.
    """

    ORDER = 4
    ATTRS = {
        "files": {
            "type": "list:dict",
            "validator": {"keys": ["path", "size", "md5"]},
        }
    }
