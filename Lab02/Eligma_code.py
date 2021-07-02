#source alphabet utk replace
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

uppercase_alphabet = [x.upper() for x in alphabet]
alphabet.extend(uppercase_alphabet)
alphabet.extend(alphabet)

#input user code 
code = input("Masukan string: ")
code = list(code)

#find number and sum
number = []
for item in code:
    for subitem in item.split():
        if(subitem.isdigit()):
            number.append(subitem)

number = [int(i) for i in number]
summary_of_number = sum(number)

#find letter and make a list
letter = []
for item2 in code:
    for subitem2 in item2.split():
        if(subitem2.isalpha()):
            letter.append(subitem2)

#replace every element of letter with alphabet
for x in range(len(letter)):
    index = alphabet.index(letter[x]) 
    letter[x] = alphabet[index + summary_of_number]

#convert list to string
output = ""
for element in letter:
    output += element
print(output)

