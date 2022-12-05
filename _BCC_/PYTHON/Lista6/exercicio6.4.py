import pandas as pd

def main():
    df = pd.read_csv("https://www.dropbox.com/s/kwibw8umms9yh9w/NotasAjuste.csv?dl=1")
    nomeExame = input()
    Exame_mean = df[nomeExame].mean()

    if (Exame_mean < 50):
        df["Ajuste"] = df[nomeExame]*1.2
    elif(Exame_mean < 70):
        df["Ajuste"] = df[nomeExame]*1.1
    elif(Exame_mean < 80):
        df["Ajuste"] = df[nomeExame]*1.05
    else:            
        df["Ajuste"] = df[nomeExame]
    print(df)
if __name__ == '__main__':
    main()