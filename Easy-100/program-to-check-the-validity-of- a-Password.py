'''
Python program to check the validity of a Password
Last Updated: 18-04-2020
In this program, we will be taking a password as a combination of alphanumeric characters along with special characters, and check whether the password is valid or not with the help of few conditions.

Primary conditions for password validation :

Minimum 8 characters.
The alphabets must be between [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
Examples:

Input : R@m@_f0rtu9e$
Output : Valid Password

Input : Rama_fortune$
Output : Invalid Password
Explanation: Number is missing

Input : Rama#fortu9e 
Output : Invalid Password
Explanation: Must consist from _ or @ or $
'''
l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
if (len(s) >= 8): 
	for i in s: 

		# counting lowercase alphabets 
		if (i.islower()): 
			l+=1			

		# counting uppercase alphabets 
		if (i.isupper()): 
			u+=1			

		# counting digits 
		if (i.isdigit()): 
			d+=1			

		# counting the mentioned special characters 
		if(i=='@'or i=='$' or i=='_'): 
			p+=1		
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)): 
	print("Valid Password") 
else: 
	print("Invalid Password") 
