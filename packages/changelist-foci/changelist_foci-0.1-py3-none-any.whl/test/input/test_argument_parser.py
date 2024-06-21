"""Testing Argument Parser Methods.
"""
from changelist_foci.input.argument_parser import parse_arguments


def test_parse_arguments_empty_list():
    result = parse_arguments('')
    assert result.changelist_name == None
    assert result.workspace_path is None


def test_parse_arguments_change_list_main():
    result = parse_arguments(['--changelist', 'Main'])
    assert result.changelist_name == 'Main'
    assert result.workspace_path is None

