import backend


def test_backend_importable():
    assert backend is not None


def test_main_exists():
    assert callable(backend.main)


def test_main_runs(capsys):
    backend.main()
    captured = capsys.readouterr()
    assert "Hello from backend!" in captured.out
