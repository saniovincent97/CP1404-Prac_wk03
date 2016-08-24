LOWER = 33
UPPER = 127
string_to_convert = (input("Please enter a character"))
print("The ASCII code for ", string_to_convert + " is", ord(string_to_convert))
num_to_convert = int(input("Enter a number between {} and {}".format(LOWER, UPPER)))
if num_to_convert > LOWER and num_to_convert < UPPER:
    print("The ASCII code for ", num_to_convert,  chr(num_to_convert))
else:
    print("Please enter the correct range between {} and {}".format(LOWER, UPPER))


