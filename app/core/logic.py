from app.schemas.thought import ThoughtInput, ThoughtResult

def evaluate_thought_speed(data: ThoughtInput) -> ThoughtResult:
    """思考の速度と情報量からパフォーマンスを評価する純粋関数"""
    base_score = 100.0
    
    # 1秒（1000ms）ごとにペナルティ、ただしキーワード数で加点
    time_penalty = data.time_taken_ms / 1000.0
    keyword_bonus = len(data.keywords) * 2.0
    
    final_score = max(0.0, base_score - time_penalty + keyword_bonus)
    
    feedback = "最適化された反射神経です" if final_score > 80 else "レイテンシの改善が必要です"
    
    return ThoughtResult(
        score=round(final_score, 2),
        feedback=feedback
    )