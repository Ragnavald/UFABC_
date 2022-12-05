import pandas as pd
import numpy as np
def main():
    df = pd.read_csv("https://www.dropbox.com/s/ys58atlga3escl0/Exames3_versao3.csv?dl=1")
    n = int(input("Digite número inteiro:"))
    (a,b,c,d) = np.polyfit(x = df["Exame 1"], y = df["Exame 2"], deg=3)
    y = a*n**3+b*n**2+c*n+d
    print("%.2f"%y)
if __name__ == '__main__':
    main()