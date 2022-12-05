import pandas as pd
def main():
    df = pd.read_csv("https://www.dropbox.com/s/d639ba1mx3pi4vl/fake-classrooms20.csv?dl=1")  
    print(df["Trabalho"].mode())
if __name__ == '__main__':
    main()
