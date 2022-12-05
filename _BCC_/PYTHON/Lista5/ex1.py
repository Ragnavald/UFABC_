import pandas as pd

def main():

    df = pd.read_csv("https://www.dropbox.com/s/yqpb4dtd2xgxdpt/Exames5.csv?dl=1")
    c1 = (df["Exame 2"].corr(df["Exame 1"]))**2
    c2 = (df["Exame 3"].corr(df["Exame 1"]))**2
    print("%.2f"%c1)
    print("%.2f"%c2)
    if c1>c2 :
        print(2)
    else:
        print(3)


if __name__ == '__main__':
    main()