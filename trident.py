def main():
  filename = './input.txt'

  with open(filename,'r') as fi:
    for line in fi:
      print(line)

if __name__ == "__main__":
    main()