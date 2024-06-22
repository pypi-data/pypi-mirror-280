from cwstorm.dsl.work_node import WorkNode
import re


class Email(WorkNode):
    """
    Email

    An Email node sends an email to a list of addresses when it is executed.
    """

    ORDER = 6
    ATTRS = {
        "addresses": {
            "type": "list:str",
            "validator": re.compile(
                r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
            ),
            "default": ["joe.bloggs@example.com"],
        },
        "subject": {
            "type": "str",
            "default": "Completed: ${workflow-id}",
            "validator": re.compile( r"^[^\r\n]{1,255}$", re.IGNORECASE),
        },
        "body": {
            "type": "str",
            "default": "The job with ID ${workflow-id} has been successfully completed.",
            "validator": re.compile(r"^[\s\S]*$", re.IGNORECASE),
        },
    }
