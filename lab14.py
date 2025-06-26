# SDM: This program will print out '#' and increasing the amount in each row to form a triangle. In addition, it will take a string and reverse it. There should be a loop that reverses the string as well as a recursive function that does the same thing. The function should return the reversed string to be printed outside of the function.


def print_tri(row_length):
    if row_length != 1:
        print_tri(row_length - 1)
    print(row_length * "#")

print_tri(5)
print("ending...")

def reverse(input_string):
    if input_string == "":
        return input_string
    else:
        return reverse(input_string[1:]) + input_string[0]


test_string = "Fool Moon night"
reversed_string = ""
for index in range(len(test_string)):
    if index != 0:
        reversed_string += test_string[index*-1]
    if index == len(test_string)-1:
        reversed_string += test_string[0]

print(reversed_string)
print(reverse(test_string))