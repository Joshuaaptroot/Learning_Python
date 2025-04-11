import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    newScores = scores.sort_values("score", ascending=False)
    newDf= pd.DataFrame({
        "score" : newScores["score"],
        "rank" : pd.factorize(newScores["score"]) [0] + 1

    })

    return newDf