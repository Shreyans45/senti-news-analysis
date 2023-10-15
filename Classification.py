def classify_sentiment(aggregate_score):
    if aggregate_score > 0:
        return 'positive'
    elif aggregate_score < 0:
        return 'negative'
    else:
        return 'neutral'
        
