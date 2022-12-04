import pandas as pd
import numpy as np


def main():
    music_data = pd.read_csv('music.csv')

#     cleaning the data
    X = music_data.drop(columns = ['genre'])
    print(X)

if __name__ == '__main__':
    main()


