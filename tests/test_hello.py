from hello import hello

def test_hello_prints(capsys):
    hello()
    captured=capsys.readouterr()
    assert "hello python" in captured.out
