def main():
    import pandas as pd
    df = pd.read_csv('https://www.dropbox.com/s/qn4mpk1inlpttng/fake-file05.csv?dl=1')
    df.query("Meses < 46 or Idade == 35")
if __name__ == '__main__':
    main()