"""Data describing a File Change.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ChangeData:
    """The Change Information that is associated with a single file.

    Properties:
    - before_path (str | None): The initial path of the file.
    - before_dir (bool | None): Whether the initial file is a directory.
    - after_path (str | None): The final path of the file.
    - after_dir (bool | None): Whether the final path is a directory.
    """
    before_path: str | None = None
    before_dir: bool | None = None
    after_path: str | None = None
    after_dir: bool | None = None

    def get_subject(self) -> str:
        """
        """
        if self.before_path is None:
            if self.after_path is None:
                exit('Empty Change Data')
            # todo: Process the After Path
            file_name = _get_file_name(self.after_path)
            return f"Create {file_name}"
        elif self.after_path is None:
            # todo: Process Before Path
            file_name = _get_file_name(self.before_path)
            return f"Remove {file_name}"
        else:
            name_before = _get_file_name(self.before_path)
            name_after = _get_file_name(self.after_path)
            # Compare name changes
            if name_before == name_after:
                return f"Update {name_before}"
            #
            return f"Move {name_before} to {name_after}"

def _get_file_name(path_value: str) -> str:
    """
    """
    root_def = '$PROJECT_DIR$'
    if not path_value.startswith(root_def):
        exit("Path Values must start with project root.")
    # 
    rel_path = path_value[len(root_def):]
    #
    return rel_path
