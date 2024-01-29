

# with open('write_file.txt', 'w') as f:
#    text_in_file =  f.read()

#    print(text_in_file)

# with open('write_file.txt', 'a+') as f:
#     f.write("write something to read")
#     text_in_file = 'alleo'
#     text_in_file = f.read()

# print(text_in_file)

with open('this_file.txt', 'w+') as f:
    f.write("Apple is a fruitt\n"
            "Mango is a fruit ")

with open('this_file.txt', 'r') as f:
    content_1 = f.readline()
    content_2 = f.readline()

    print("Line 1:", content_1)
    print("Line 2:", content_2)

