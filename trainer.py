import time
import httpx

API_BASE_URL = "http://127.0.0.1:8000/api/v1/training"

def main():
    print("=== Fast Logic Trainer (CLI Client) ===")
    print("APIサーバーに接続し、トレーニングを開始します...\n")

    with httpx.Client(base_url=API_BASE_URL) as client:
        # 1. お題の取得 (GETリクエスト)
        response = client.get("/topic")
        if response.status_code != 200:
            print("APIサーバーが起動していません。uvicorn app.main:app を実行してください。")
            return
        
        topic = response.json()["topic"]
        print(f"[お題] {topic}")
        print("思考を整理し、カンマ区切りでキーワードを入力してください。")
        print("Enterキーを押すと計測が開始されます。")
        input(">> 準備ができたらEnterを押してください...")

        # 2. 時間計測と入力受付
        start_time = time.time()
        user_input = input("\n回答 (例: カプセル化,継承,ポリモーフィズム): ")
        end_time = time.time()

        time_taken_ms = int((end_time - start_time) * 1000)
        keywords = [k.strip() for k in user_input.split(",") if k.strip()]

        # 3. 評価の依頼 (POSTリクエスト)
        payload = {
            "topic": topic,
            "keywords": keywords,
            "time_taken_ms": time_taken_ms
        }
        
        print("\nAPIへ評価をリクエスト中...")
        eval_response = client.post("/evaluate", json=payload)
        
        if eval_response.status_code == 200:
            result = eval_response.json()
            print("\n=== 評価結果 ===")
            print(f"思考時間: {time_taken_ms} ms")
            print(f"抽出キーワード: {keywords}")
            print(f"スコア: {result['score']}")
            print(f"フィードバック: {result['feedback']}")
        else:
            print("評価エラー:", eval_response.json())

if __name__ == "__main__":
    main()