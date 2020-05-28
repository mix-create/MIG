# task 1

text = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz ' \
       'pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków ' \
       'później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował ' \
       'się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ' \
       'ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na ' \
       'komputerach osobistych, jak Aldus PageMaker'

# task 2

name = 'Kamil'
surname = 'Michalak'

letter_1 = name[2]
letter_2 = surname[3]

letter_1_amt = text.count(letter_1)
letter_2_amt = text.count(letter_2)

print('W tekście jest {liczba_liter1} liter {litera1} oraz {liczba_liter2} liter {litera2}'.format(
    liczba_liter1=letter_1_amt, liczba_liter2=letter_2_amt, litera1=letter_1, litera2=letter_2))

