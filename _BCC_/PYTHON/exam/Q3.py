def main():
    import pandas as pd
    df = pd.read_csv("https://www.dropbox.com/s/wdv9z9e9uyywsqs/fake-file11.csv?dl=1")
    df_filtrada = df.query("Funcionario <= 10 and Idade > 43")
    vetor = ['Funcionario','Idade','Salario','Escolaridade']
    print(df_filtrada[vetor])
    
if __name__ == '__main__':
    main()