def main():
    import pandas as pd
    df = pd.read_csv("https://www.dropbox.com/s/e3pb9ax1b15wu3a/fake-classrooms09.csv?dl=1")
    coluna = input()
    var = df[coluna].std()
    print("%.2f" %var)
if __name__ == '__main__':
    main()