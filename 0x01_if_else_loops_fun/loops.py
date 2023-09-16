for x in range(9, 1, 2):
    print(x)

# print alphabet


# the stop index in range in not included
# so we will add one
for y in range(65, 91):
    print(chr(y))


# exclude just my name alphabet: R A B I A

for j in range(97, 123):
    char = chr(j)
    if char != "r" and char != "a" and char != "b" and char != "i":
        print(char)


"""
    Print numbers 0 to 98
     in decimal and hexadecimal.
"""
hex(20)  # return "0x14"

for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
