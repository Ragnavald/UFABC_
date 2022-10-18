def main():

    import pandas as pd
    df = pd.read_csv("https://www.dropbox.com/s/nnma31aisywunr3/fake-file01.csv?dl=1")
    print(df.groupby("Escolaridade")["Idade"].sum())

if __name__ == '__main__':
    main()