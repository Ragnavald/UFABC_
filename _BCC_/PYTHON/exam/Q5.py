def main():
    import pandas as pd 
    df = pd.read_csv("https://www.dropbox.com/s/6s52z0tftn4pgp2/Exames4.csv?dl=1")
    coluna = input()
    valor = df[coluna].corr(df["Exame 1"])
    print("%.2f"%valor)
if __name__ == '__main__':
    main()