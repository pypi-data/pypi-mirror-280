"""Valid Input Data Class.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class InputData:
    """A Data Class Containing Program Input.

    Fields:
    - workspace_xml (str): The contents of the workspace.xml file.
    - changelist_name (str): The name of the Changelist, or None.
    """
    workspace_xml: str
    changelist_name: str | None = None
