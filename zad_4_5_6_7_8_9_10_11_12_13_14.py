# task 4 & 5

text = 'example text'

print(dir(text))
help(text.lower)

# task 6

name = 'Kamil'
surname = 'Michalak'

print(name[::-1].title(), surname[::-1].title())

# task 7

list_1 = [a for a in range(1, 11)]

list_2 = list_1[5:]
list_1 = list_1[:5]

print(list_1)
print(list_2)

# task 8

list_1 = list_1 + list_2
list_1 = [0] + list_1

list_1_copy = list_1.copy()

print(list_1[::-1])

# task 9

students = [(1, 'name 1 surname 1'), (2, 'name 2 surname 2'), (3, 'name 3 surname 3')]

# task 10

student_dict = {}

for element in students:
    key = element[0]
    value = element[1]
    student_dict[key] = value

print(student_dict)

age_dict = {1: 22, 2: 23, 3: 19}
address_dict = {1: 'address 1', 2: 'address 2', 3: 'address 3'}
email_dict = {1: 'email@1.com', 2: 'email@2.com', 3: 'email@3.com'}
year_dict = {1: 1998, 2: 1997, 3: 2001}

# task 11

phones = ['111222333', '222333444', '333444555', '444555666', '111222333']
phones = set(phones)
print(phones)

# task 12

for x in range(1, 11):
    print(x)

# task 13

for x in range(100, 19, -5):
    print(x)

# task 14

d_list = []

d_list.append(student_dict)  # 0
d_list.append(address_dict)  # 1
d_list.append(age_dict)  # 2
d_list.append(year_dict)  # 3
d_list.append(email_dict)  # 4

for key in range(1, 4):

    tmp_list = []

    for d in d_list:
        tmp_list.append(d[key])

    text = 'Student {name} o indeksie {key} ma {age} lat, urodził się w {year}, mieszka w {address} oraz ' \
           'posiada email {email}'.format(name=tmp_list[0], key=key, age=tmp_list[2], year=tmp_list[3],
                                          address=tmp_list[1], email=tmp_list[4])

    print(text)