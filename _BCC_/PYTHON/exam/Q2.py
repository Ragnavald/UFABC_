import math
def main():
    
    a = float(input())
    b = float(input())
    c = float(input())
    delta = b**2-4*a*c

    r2 = (-b-math.sqrt(delta))/(2*a)
    print("%.2f" %r2)

if __name__ == '__main__':
    main()