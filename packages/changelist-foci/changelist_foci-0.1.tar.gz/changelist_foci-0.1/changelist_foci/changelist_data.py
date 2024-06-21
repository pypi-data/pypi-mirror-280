"""The Data Class for a ChangeList.
"""
from dataclasses import dataclass

from changelist_foci.change_data import ChangeData


@dataclass(frozen=True)
class ChangelistData:
    """
    The complete Data class representing a ChangeList.
    
    Properties:
    - id (str): The unique id of the changelist.
    - name (str): The name of the changelist.
    - changes (list[ChangeData]): The list of file changes in the changelist.
    - comment (str): The comment associated with the changelist.
    - is_default (bool): Whether this is the active changelist.
    """
    id: str
    name: str
    changes: list[ChangeData]
    comment: str = ""
    is_default: bool = False

    def get_foci(self) -> str:
        """
        Obtain the FOCI of a Changelist.

        Returns:
        str - The FOCI string.
        """
        subject_lines = "\n".join(map(lambda x: f"* {x.get_subject()}", self.changes))
        return f"{self.name}:\n" + subject_lines
