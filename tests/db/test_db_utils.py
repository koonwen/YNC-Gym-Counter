
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('app.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output


def test_reset_table_command(runner, monkeypatch):
    def fake_reset_data_table():
        pass
    monkeypatch.setattr('app.db.reset_data_table', fake_reset_data_table)
    result = runner.invoke(args=["reset-data-table"])
    assert 'Data table reset' in result.output


def test_mock_data_command(runner, monkeypatch):
    def fake_mock_db():
        pass
    monkeypatch.setattr('app.db.mock_db', fake_mock_db())
    result = runner.invoke(args=["mock-db"])
    assert 'Mock data initialized' in result.output