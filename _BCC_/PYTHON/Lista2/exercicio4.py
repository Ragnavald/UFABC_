def main():
    import pandas as pd
    df = pd.read_csv('https://www.dropbox.com/s/fklekauxy0n3xdy/fake-file06.csv?dl=1')
    print(df.sort_values(by=["Genero","Idade"], ascending=[False,True]))

if __name__ == '__main__':
    main()