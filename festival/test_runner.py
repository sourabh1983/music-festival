import requests

from festival.runner import run_music_festival

from . import service


class MockResponse:
    @staticmethod
    def json():
        return [
                    {
                        "name": "music festival 1",
                        "bands": [
                            {
                                "name": "band 1",
                                "recordLabel": "record label 1"
                            },
                            {
                                "name": "band 2",
                                "recordLabel": "record label 1"
                            },
                            {
                                "name": "band 3",
                                "recordLabel": "record label 2"
                            }
                        ]
                    },
                ]

    def raise_for_status(test):
        pass


def test_get_json(monkeypatch, capsys):

    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    data = service.get_festivals()
    run_music_festival(data)
    assert capsys.readouterr().out == 'record label 1\n\tband 1\n\t\tmusic festival 1\n\tband 2\n\t\tmusic festival 1\nrecord label 2\n\tband 3\n\t\tmusic festival 1\n'
