import pandas as pd
def main():
    df = pd.read_csv("https://www.dropbox.com/s/08mj9xfm8f6p9ph/fake-classrooms05.csv?dl=1")
    print("%.2f" %df["Prova 1"].std())
   
if __name__ == '__main__':
    main()
