Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a, b = 1, 1
>>> total = 0
>>> while a<=4000000:
	if a % 2 == 0:
		total += a
	a, b = b, a+b
print total
