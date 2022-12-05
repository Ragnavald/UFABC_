def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if (a**2+b**2 > c**2):
        print("A")
    elif(a**2+b**2 == c**2):
        print("R")
    else:
        print("O")
if __name__ == '__main__':
    main()