name_text = open("name.txt","w")
name = input("Please enter your name ")
print(name, file=name_text)
name_text.close()