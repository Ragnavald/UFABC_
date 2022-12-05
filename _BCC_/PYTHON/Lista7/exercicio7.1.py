def main():
    i=0
    cont_positivo = 0
    cont_negativo = 0
    cont_zeros = 0
    while(i<10):
        num = int(input())
        if (num > 0):
            cont_positivo = cont_positivo + 1
        elif (num < 0):
            cont_negativo = cont_negativo + 1
        else:
            cont_zeros = cont_zeros + 1
        i = i + 1
    print(cont_positivo)
    print(cont_negativo)
    print(cont_zeros)
if __name__ == '_main_':
    main()