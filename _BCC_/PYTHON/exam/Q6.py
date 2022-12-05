def main():
  i=0
  n=0
  while i < 5:
    n = float(input())
    if(n>198):
      print("Meta atingida")
      break
    else:
      print("Insuficiente")
    i = i + 1
if __name__ == '__main__':
  main()