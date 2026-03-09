import time
import httpx
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.table import Table
from rich import print as rprint

API_BASE_URL = "http://127.0.0.1:8000/api/v1/training"
console = Console()

def main():
    console.clear()
    console.print(Panel.fit("[bold blue]Fast Logic Trainer[/bold blue] (CLI Client)", border_style="cyan"))
    console.print("[dim]APIサーバーに接続し、トレーニングを開始します...[/dim]\n")

    with httpx.Client(base_url=API_BASE_URL) as client:
        # 1. お題の取得 (GETリクエスト)
        try:
            response = client.get("/topic")
            if response.status_code != 200:
                console.print("[bold red]APIサーバーエラー:[/bold red] 正常な応答が得られませんでした。")
                return
        except httpx.ConnectError:
            console.print("[bold red]接続エラー:[/bold red] APIサーバーが起動していません。`uvicorn app.main:app` を実行してください。")
            return
        
        topic = response.json()["topic"]
        
        console.print(Panel(f"[bold green]{topic}[/bold green]", title="🎯 本日のお題", border_style="green"))
        console.print("思考を整理し、[yellow]カンマ区切り[/yellow]でキーワードを入力してください。")
        console.print("Enterキーを押すと計測が開始されます。")
        
        Prompt.ask("\n[bold cyan]>> 準備ができたらEnterを押してください...[/bold cyan]", default="")

        # 2. 時間計測と入力受付
        start_time = time.time()
        
        # richのPromptを使って入力を受け付ける
        console.print("\n[bold]思考の出力開始！[/bold]")
        user_input = Prompt.ask("[bold magenta]回答 (例: カプセル化,継承,ポリモーフィズム)[/bold magenta]")
        
        end_time = time.time()

        time_taken_ms = int((end_time - start_time) * 1000)
        keywords = [k.strip() for k in user_input.split(",") if k.strip()]

        if not keywords:
            console.print("[bold red]キーワードが入力されませんでした。[/bold red]")
            return

        # 3. 評価の依頼 (POSTリクエスト)
        payload = {
            "topic": topic,
            "keywords": keywords,
            "time_taken_ms": time_taken_ms
        }
        
        with console.status("[bold green]APIへ評価をリクエスト中...[/bold green]", spinner="dots"):
            eval_response = client.post("/evaluate", json=payload)
        
        if eval_response.status_code == 200:
            result = eval_response.json()
            score = result['score']
            feedback = result['feedback']
            
            # スコアによる色分け
            score_color = "green" if score > 80 else "yellow" if score > 50 else "red"
            
            # 結果表示用テーブル
            table = Table(show_header=False, box=None)
            table.add_column("Property", style="bold cyan")
            table.add_column("Value")
            table.add_row("思考時間", f"{time_taken_ms:,} ms")
            table.add_row("抽出キーワード", f"{', '.join(keywords)} ({len(keywords)}個)")
            table.add_row("スコア", f"[{score_color} bold]{score}[/]")
            
            console.print("\n")
            console.print(Panel(
                table,
                title="🏆 評価結果",
                border_style="blue",
                padding=(1, 2)
            ))
            
            console.print(f"\n[bold]フィードバック:[/bold] {feedback}")
        else:
            console.print(f"[bold red]評価エラー:[/bold red] {eval_response.text}")

if __name__ == "__main__":
    main()