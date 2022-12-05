import pandas as pd

def main():

    n = int(input())
    i = 0
    while(i<n):
        link = input()
        i = i + 1
        df = pd.read_csv(link, sep = ",")
        print("%.2f"%df["B"].mean())
if __name__ == '_main_':
    main()