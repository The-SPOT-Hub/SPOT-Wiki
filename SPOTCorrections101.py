def punctuation_type(str):
    if str == str.upper():
        print('This is all caps')
    elif str == str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1)
punctuation_type(str2)
punctuation_type(str3)

str1 = "    "
str2 = "  Hello   "
str3 = "Hello World"

print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

sentence = "Hello     World!   How are you?   "
word_count = sum(1 for word in sentence.split() if not word.isspace())
print("Number of words in the sentence:", word_count)

print("new")

def number_range(number):
    match number:
        case n if n < 0:
            print(f'{number} is less than 0')
        case n if n <= 50:
            print(f'{number} is between 0 and 50')
        case n if n <= 100:
            print(f'{number} is between 51 and 100')
        case _:
            print(f'{number} is greater than 100')
number_range(0)
number_range(15)
number_range(51)
number_range(75)
number_range(110)
number_range(-10)


my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)
for value in values:
    print(value)

elements = [0, 1 , 2, "Dima"]
print(elements.reverse())
print(elements)

ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dimo(info):
    try:
        info['dimo']
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dimo(ages))

def function1():
    x = 10

    def function2():
        y = 20
        print(x)

    function2()
    print(x)

function1()