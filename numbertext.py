number_file = open("numbers.txt", "r")
num1 = int(number_file.readline())
num2 = int(number_file.readline())
print(num1 + num2)
number_file.close()