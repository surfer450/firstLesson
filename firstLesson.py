def factorial():
    # function get num from user and print factorial
    num = input("enter number: ")
    if not(num.isnumeric()):
        print("cant do factorial to string or negetive numbers!")
        return

    num = int(num)
    mul = 1
    for i in range(1, num + 1):
        mul = mul * i
    print("the factorial is: ", mul)




def fibonachi(num):
    # function get index in fibonachi and print its value
    if not (isinstance(num, int)) or num < 0:
        print("cant calculate fibonachi for string or negetive!")
        return -1

    if num == 1 or num == 2:
        return 1
    return fibonachi(num - 1) + fibonachi(num - 2)




def find_denominator(num1, num2):
    # function get 2 numbers and print the biggest denominator for both
    if not (isinstance(num1, int) and isinstance(num2, int)):
        print("cant find devider for strings!")
        return -1

    denominator = 0
    min_num = num1
    if num2 < min_num:
        min_num = num2

    for i in range(1, min_num+1):
        if num1 % i == 0 and num2 % i == 0:
            denominator = i
    return denominator



def main():
    num = find_denominator("sagy", 20)
    print(num)


if __name__ == "__main__":
    main()
