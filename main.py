import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import statistics


def main():
    music_data = pd.read_csv('music.csv')

#   data set up
    X = music_data.drop(columns=['genre'])
    y = music_data['genre']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8)

#   training model
    model = DecisionTreeClassifier()
    model.fit(X_train.values, y_train)

    joblib.dump(model, 'music-recommender.joblib')  # saving the trained model in a file

    model = joblib.load('music-recommender.joblib')
    predictions = model.predict(X_test)

#   evaluate accuracy
    score = accuracy_score(y_test, predictions)
    print(score)


if __name__ == '__main__':
    main()


