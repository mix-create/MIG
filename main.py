from math import log, e
from file_manager import FileManager
import chuck_norris

# task 1


def func(list_a, list_b):
    return list_a[::2] + list_b[1::2]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(func(a, b))

# task 2


def text_stats(data_text: str):
    return {
        'length': len(data_text),
        'letters': list(set(data_text)),
        'big letters': data_text.upper(),
        'small letters': data_text.lower()
    }


print(text_stats('Lorem ipsum dolor sit amet'))

# task 3


def remover(text: str, letter: str):
    return text.replace(letter, '')


print(remover('Lorem ipsum dolor sit amet', 'i'))

# task 4


def converter(temperature: float, conversion_type: str):

    if conversion_type == 'Fahrenheit':
        return 9 / 5 * temperature + 32
    elif conversion_type == 'Kelvin':
        return temperature + 273
    elif conversion_type == 'Rankine':
        return temperature * 1.8 + 491.67
    else:
        return 'Given conversion type does not exist.'


print(converter(1, 'Fahrenheit'))
print(converter(1, 'Kelvin'))
print(converter(1, 'Rankine'))
print(converter(1, 'Rankenheit'))

# task 5


class Calculator:

    def add(self, number_a, number_b):
        return number_a + number_b

    def difference(self, number_a, number_b):
        return number_a - number_b

    def multiply(self, number_a, number_b):
        return number_a * number_b

    def divide(self, number_a, number_b):
        if number_b != 0:
            return number_a / number_b
        else:
            print('Error - zero division')

# task 6


class ScienceCalculator(Calculator):

    def power(self, number_a, number_b):
        return number_a ** number_b

    def natural_log(self, number_a):
        return log(number_a, e)

    def log_10(self, number_a):
        return log(number_a, 10)

# task 7


def reverser(text: str):
    return text[::-1]


print(reverser('koteł'))

# task 9

my_file_manager = FileManager('file.txt')
my_file_manager.update_file('Lorem ipsum dolor sit amet \n')
my_file_manager.update_file('Lorem ipsum dolor sit amet \n')
print(my_file_manager.read_file())

# task 10

print(chuck_norris.get_quip_for_name('Kamil'))

