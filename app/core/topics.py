from typing import List

# お題のモックデータベース
TOPICS: List[str] = [
    "オブジェクト指向の3大要素を説明せよ",
    "REST APIの設計原則を3つ挙げよ",
    "RDBとNoSQLの使い分けの基準は何か",
    "「関心の分離」がもたらすメリットとは",
    "GitにおけるRebaseとMergeの違いを説明せよ",
    "Dockerのコンテナと仮想マシンの違いは何か",
    "CI/CDの目的と主な利点を説明せよ"
]

def get_topics() -> List[str]:
    """すべてのお題を取得する"""
    return TOPICS
