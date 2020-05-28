# task 3

# padding and alignment

print('big indent {:>15}'.format('<- here'))

# truncating long strings

print('{:.5}'.format('kamil ślimak'))

# int

print('Year {:d}'.format(2020))

# float with restrictions

print('{:22.5f}'.format(123456789.123456789))

# placeholders

dict_example = {'abc': 100, 'def': 200}

print('Dictionary values {abc} {def}'.format(**dict_example))