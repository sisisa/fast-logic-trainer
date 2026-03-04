def test_root_redirect(client):
    """ルートアクセス時にSwagger UIへリダイレクトされるかテスト"""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"

def test_health_check(client):
    """ヘルスチェックエンドポイントの可用性テスト"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "latency": "low"}

def test_evaluate_thought_success(client):
    """正常な思考データが送信された場合のスコア算出テスト"""
    payload = {
        "topic": "FastAPIの利点",
        "keywords": ["型安全", "高速", "非同期"],
        "time_taken_ms": 1500
    }
    response = client.post("/api/v1/training/evaluate", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "feedback" in data
    assert data["score"] > 0

def test_evaluate_thought_validation_error(client):
    """不正なデータ（時間計測エラーなど）が送信された場合のPydanticバリデーションテスト"""
    payload = {
        "topic": "エラーテスト",
        "keywords": [], # キーワードが空（min_items=1に違反）
        "time_taken_ms": -100 # 時間がマイナス（gt=0に違反）
    }
    response = client.post("/api/v1/training/evaluate", json=payload)
    
    # 422 Unprocessable Entity が返ることを確認し、型安全性が機能していることを証明する
    assert response.status_code == 422