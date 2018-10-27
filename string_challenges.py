# Вывести последнюю букву в слове
word = 'Набережные Челны'
mylist=word[-1]



# Вывести количество букв а в слове
word = 'Архангельск'
arkhangelsk = word.lower()
word.count('a')
#print(arkhangelsk.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангeльск'
arkhangelsk = word.lower()
glasnye = ("а","e")
vse_glasnye = 0
for glasnaya in glasnye:
	vse_glasnye = vse_glasnye + arkhangelsk.count(glasnaya)
	#print(arkhangelsk.count(glasnaya))
#print(vse_glasnye)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence.count(" ")
number_words = sentence.count(' ') + 1
#print(number_words)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence.split()
#print(sentence.split())

for first_word in sentence.split():
	first_letter = first_word [0]
	#print(first_letter)


# Вывести длину всех слов деленных на их количество.
sentence = 'Мы приехали в гости'
#считать длину каждого слова
#посчитать общую (совокупную) длину всех слов без пробелов
#считать количество слов
#посчитать частное стр.43/44
sentence.split()
number_of_words = len(sentence.split())
#print(len(sentence.split()))
lenofword = 0
for letter in sentence.split():
	#lenofword = len(letter)
	#print(lenofword) 
	lenofword = lenofword + len(letter)
#print(lenofword)
print(lenofword/number_of_words)

