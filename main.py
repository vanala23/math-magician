import os
import sys

def add(a, b):
    return a + b

def main():
    print("Welcome to Math Magician!")
    op = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    result = 0

    if(op == '+'):
        result = add(a, b)

    print(f"{a} {op} {b} = {result}")    

if __name__ == "__main__":
    main()
