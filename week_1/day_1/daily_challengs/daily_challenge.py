# ------ Challenge 1

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)

# ------ Challenge 2

text = input("Enter a string: ")

if text:
    result = text[0]
    
    for char in text[1:]:
        if char != result[-1]:
            result += char
else:
    result = ""

print("String without consecutive duplicates:", result)

