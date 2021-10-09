# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Need to close file as it uses some of the resources
# from your computer

# from root - absolute path
# with open("/Users/evemorgan2/Desktop/my_file.txt") as file:

# from current file location - relative path
with open("../../../../Desktop/my_file.txt") as file:


    # Saved into variable called file

    contents = file.read()
    print(contents)

# Automatically closes when done with it

#  use a to append, use w to write
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text:\nI live in SF.")
#
# with open("new_file.txt", mode="w") as file:
#     file.write("New text. Eve")
