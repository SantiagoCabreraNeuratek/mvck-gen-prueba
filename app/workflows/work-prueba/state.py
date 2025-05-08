class SentimentState:
    def __init__(self):
        self.text = None
        self.sentiment = None
        self.previous_sentiment = None
        self.is_converged = False

    def update_sentiment(self, sentiment):
        self.previous_sentiment = self.sentiment
        self.sentiment = sentiment
        self.check_convergence()

    def check_convergence(self):
        if self.previous_sentiment == self.sentiment:
            self.is_converged = True