import pandas as pd
def main():
    df = pd.read_csv("https://www.dropbox.com/s/fspfiuvv3ywti5p/fake-classrooms14.csv?dl=1") 
    print("%.2f" %df["Trabalho"].median())
if __name__ == '__main__':
    main()
