import pandas as pd

def main():
    df = pd.read_csv("https://www.dropbox.com/s/jqficiaig0a8aze/NotasTurmas.csv?dl=1")
    turma = input()
    mediana = df[turma].median()
    media = df[turma].mean()
    if (media >= mediana):
        print("Media")
    else:
        print("Mediana")    

if __name__ == '__main__':
    main()