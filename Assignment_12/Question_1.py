# 1. Write a program which accepts one character and checks whether it is vowel or consonant.

# Input: a
# Output: Vowel

def CheckVowel(char):
    low_char = char.lower()
    if low_char in ('a','e','i','o','u'):
        return True

def main():
    char = input("Enter character :")
    ret = CheckVowel(char)

    if ret:
        print('character is Vowel')
    else:
        print('character is Not Vowel')
        


if __name__ == "__main__":
    main()