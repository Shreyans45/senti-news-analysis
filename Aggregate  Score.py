def calculate_aggregate_sentiment(tokens):
    sentiment_scores = [get_sentiment_score(word) for word in tokens]
    return sum(sentiment_scores)
