import pandas as pd 
import numpy as np

def main():
    df = pd.read_csv("https://www.dropbox.com/s/cpo4eyqoztwn3nc/fake-classrooms-correl07.csv?dl=1")
    coluna = input()
    x = float(input())
    (a,b) = np.polyfit(x = df[coluna], y = df["Nota Final"], deg=1) 

    f = a*x+b

    print("%.2f"%f)

if __name__ == '__main__':
    main()