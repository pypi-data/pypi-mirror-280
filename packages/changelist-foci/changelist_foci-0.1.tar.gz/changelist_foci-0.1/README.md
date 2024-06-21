# Changelist-FOCI
Obtains the FOCI from a ChangeList.

## How It Works
The changelist information is loaded from a workspace file, and processed into Changelist Data objects.
The Changelist Data is then processed to obtain the FOCI (File Oriented Commit Information).

## Arguments
**Workspace Path:** `--workspace`
The Workspace path is an optional argument, which is used to load the workspace file contents.

If the `workspace_path` argument is not provided, it is assumed that the current working directory is the project root directory.

**Changelist Name:** `--changelist`
The Changelist name is an optional argument, that is used to select which Changelist to obtain the FOCI for.

If the changelist name is not provided, it is assumed that the active changelist `(default = true)` will be the target of the operation.
