with open("test_utf.txt") as infile:
    test_string = infile.read()

print("Length:", len(test_string))
for c in test_string:
    print(c, ord(c))
