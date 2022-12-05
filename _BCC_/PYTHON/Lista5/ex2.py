import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("https://www.dropbox.com/s/07l7fxfyu997b4a/Exames2_versao2.csv?dl=1")
    (a,b,c) =np.polyfit(x=df["Exame 1"], y=df["Exame 2"], deg=2)
    print("%.2f"%a)
    print("%.2f"%b)
    print("%.2f"%c)
    # plt.plot(df["Exame 1"], df["Exame 2"],'.')
    # x = np.arange(0,100,0.1)
    # y = a*x**2 + b*x + c
    # plt.plot(x,y,'')
    # plt.show()
    
if __name__ == '__main__':
    main()