Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> test_list = ['one', 'two', "three"]
>>> for i in test_list:
	print(i)

	
one
two
three
>>> a = [(1,2), (3,4), (5,6)]
>>> for (first, last) in a:
	print(first + last)

	
3
7
11
>>> marks = [90, 25, 67, 45, 80]
>>> 
>>> number = 0
>>> for mark in marks:
	number = number +1
	if mark >= 60:
		print("%d번 학생은 합격입니다." % number)
	else:
		print("%d번 학생은 불합격입니다."%number)

	
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
>>> 