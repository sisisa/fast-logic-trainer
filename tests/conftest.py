import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    """
    テスト用のFastAPIクライアントを提供するFixture。
    これにより、実際のネットワーク通信なしにAPIのルーティングやロジックをテストできる。
    """
    with TestClient(app) as c:
        yield c