import pandas as pd
import numpy as np
def main():
    df = pd.read_csv("https://www.dropbox.com/s/6s52z0tftn4pgp2/Exames4.csv?dl=1")
    n = int(input("Digite número inteiro:"))
    (a,b) = np.polyfit(x = df["Exame 2"], y = df["Exame 1"], deg=1)
    y = a*n+b
    print("%.2f"%y)
if __name__ == '__main__':
    main()