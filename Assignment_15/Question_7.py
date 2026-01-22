# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

def main():
    data = []
    for i in range(5):
        no = input("Enter string :")
        data.append(no)
    
    strings_list = list(filter(lambda x1 : len(x1) > 5 , data))
    print(strings_list)


if __name__ == "__main__":
    main()