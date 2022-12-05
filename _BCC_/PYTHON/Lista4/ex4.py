import pandas as pd
import numpy as np
def main():
    df = pd.read_csv("https://www.dropbox.com/s/e3pb9ax1b15wu3a/fake-classrooms09.csv?dl=1")
    print("%.2f" %np.percentile(df["Trabalho"],q=32))
    
if __name__ == '__main__':
    main()