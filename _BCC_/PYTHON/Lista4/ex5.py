import numpy as np
import pandas as pd
def main():
    df = pd.read_csv("https://www.dropbox.com/s/aqo9magrsmob374/fake-classrooms11.csv?dl=1")
    df["Ponderada"] = df["Trabalho"] * 5 + df["Prova 1"]*5
    print(df)

if __name__ == '__main__':
    main()