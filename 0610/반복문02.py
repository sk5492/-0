Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> family = ['mother', 'father', 'gentleman', 'sexy lady']
>>> for x in family:

	print('%s %s' % (x, len(x)))

	
mother 6
father 6
gentleman 9
sexy lady 9
>>> range(2, 7)
range(2, 7)
>>> list(range(2. 7))
SyntaxError: invalid syntax
>>> [2, 3, 4, 5, 6]
[2, 3, 4, 5, 6]
>>> a = [4, 5, 6, 7]
>>> for i in a:
	print(i)

	
4
5
6
7
>>> for i in range(4, 8):
	print(i)

	
4
5
6
7
>>> 