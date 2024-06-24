import roter.cli as cli


def test_parse_request_empty(capsys):
    options = cli.parse_request([])
    assert options == 0
    out, err = capsys.readouterr()
    assert 'usage: roter' in out
    assert not err
