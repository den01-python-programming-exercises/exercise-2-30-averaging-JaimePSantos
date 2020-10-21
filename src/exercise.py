def sum(number1, number2, number3, number4):
    # you can copy your implementation of the method sum here
    soma= number1+ number2+ number3+ number4
    return soma
def average(number1, number2, number3, number4):
    # write your code here
    # calculate the sum of the elements by calling the method sum
    avg = sum(number1, number2, number3, number4) /4
    return avg
 
def main():
    result = average(4, 3, 6, 1)
    print("Average: " + str(result))

if __name__ == '__main__':
    main()
