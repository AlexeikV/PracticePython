def reverse(word):
	temp = ''
	for i in range(len(word)):
		temp += word[len(word)-1-i]
	return temp

word = input('Please insert a word:\n')

x = reverse(word)
if x == word:
	print('This is word is a Palindrome')
else:
	print('This word isnt a Palindrome')