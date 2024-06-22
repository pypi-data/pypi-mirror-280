from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

class QDA:
    def __init__(self):
        self.model = QuadraticDiscriminantAnalysis()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.score(X, y)