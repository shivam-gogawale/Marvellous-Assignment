# 4. Write a program which accepts one number and prints binary equivalent.

def binaryNumber(no):    
    ans = []
    while no > 0:
        ans.append(no%2)
        no = no // 2
    return ans

def main():
    Number = int(input("Enter Number :"))
    ret = binaryNumber(Number)

    binary = list()
   
    for i in range(len(ret)-1,-1,-1):
        binary.append(ret[i])

    print('binary equivalent',binary)

if __name__ == "__main__":
    main()