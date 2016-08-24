def main():
    lower = 33
    upper = 127
    string_convert = (input("Please enter a character"))
    print("The ASCII code for ", string_convert + " is", ord(string_convert))
    check_num = get_number(lower, upper,)
    print("The ASCII code for ", check_num, "is" ,chr(check_num) )



def get_number(lower,upper):
    while True:
        try:
            num_convert = int(input("Enter a number between {} and {}".format(lower, upper)))
            while num_convert > lower and num_convert < upper:
                return num_convert
            else:
                print("Please enter a valid number!")
                continue
        except ValueError:
            print("Please enter a valid number!")
        else:
            break





main()