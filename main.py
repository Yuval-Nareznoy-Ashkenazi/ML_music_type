import pandas as pd
import numpy as np


def main():
    df = pd.read_csv('vgsales.csv')

    print(df.shape)
    print(df.values)

    print('Exporting df to csv file.')
    df.to_csv('modified_vgsales.csv')

    print('Exporting describe to csv file.')
    df.describe().to_csv('describe.csv')


if __name__ == '__main__':
    main()


