sheik=['a','e','i','o','u','A','E','I','O','U']
s=raw_input()
if(s in sheik):
	print('Vowel')
elif(s!=sheik):
	print('Consonant')
else:
	print('invalid')
