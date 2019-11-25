from backend import backend


class TestBackend:
    def test_start_websocket(self):
        backend.start_websocket()
        assert True