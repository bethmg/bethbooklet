# beth's handy script for printing a5 booklets on a one-sided a4 printer

import numpy as np
from sys import exit

l = int(input("Start page: ")) - 1
endpage = int(input("End page: "))

numprint = endpage-l
sheets = 0

if numprint < 3:
	print("Do you really need a booklet for this??")
	exit()

if numprint % 4 == 0:
	#print("Number of pages is divisible by 4")
	list1 = []
	list2 = []		
	s1 = ""	
	s2 = ""
	for i in range(0,int(numprint/2)):
		sheets += 0.5
		if i % 2 == 0:
			list1.append(numprint-i+l)
			list2.append(i+2+l)
		else:
			list1.append(i+l)
			list2.append(numprint-i+l)
	
	for i in range(0,int(numprint/2)):
		if i == int(numprint/2)-1:
			s1+=str(list1[i])
			s2+=str(list2[i])
		else:
			s1+=str(list1[i])
			s2+=str(list2[i])
			s1+=", "
			s2+=", "
		
	print("First print pages: ", s1)
	#print("Turn over printed pages top to bottom so that the printed side is facing away")
	print("Then reverse the stack, print pages: ", s2)

		
if (numprint-2) % 4 == 0:
	#print("Number of pages -2 is divisible by 4")
	print("On right hand side of paper, print page", 1+l)
	print("On left hand of reverse, print page", 2+l)
	sheets += 1
	list1 = []
	list2 = []		
	s1 = ""	
	s2 = ""
	for i in range(0,int((numprint-2)/2)):
		sheets += 0.5
		if i % 2 == 0:
			list1.append(numprint-i+l)
			list2.append(i+4+l)
		else:
			list1.append(i+2+l)
			list2.append(numprint-i+l)
	
	for i in range(0,int((numprint-2)/2)):
		if i == int((numprint-2)/2)-1:
			s1+=str(list1[i])
			s2+=str(list2[i])
		else:
			s1+=str(list1[i])
			s2+=str(list2[i])
			s1+=", "
			s2+=", "
		
	print("Then print pages: ", s1)
	#print("Turn over printed pages top to bottom so that the printed side is facing away")
	print("Reverse the stack, print pages: ", s2)

	
if (numprint-1) % 4 == 0:
	#print("Number of pages -1 is divisible by 4")
	print("On right hand side of paper, print page", 1+l)
	print("On left hand of reverse, print page", 2+l)
	sheets += 1
	print("Print page", 3+l ,"on the right hand side of new page")
	print("On reverse, print pages", 4+l ,",", endpage)		
	sheets += 1
	list1 = []
	list2 = []		
	s1 = ""	
	s2 = ""
	for i in range(0,int((numprint-5)/2)):
		sheets += 0.5
		if i % 2 == 0:
			list1.append(numprint-i-1+l)
			list2.append(i+6+l)
		else:
			list1.append(i+4+l)
			list2.append(numprint-i-1+l)
		
	for i in range(0,int((numprint-5)/2)):
		if i == int(((numprint-5)/2) - 1):
			s1+=str(list1[i])
			s2+=str(list2[i])
		else:
			s1+=str(list1[i])
			s2+=str(list2[i])
			s1+=", "
			s2+=", "
		
	if numprint != 5:	
		print("Then print pages: ", s1)
		#print("Turn over printed pages top to bottom so that the printed side is facing away")
		print("Reverse the stack, print pages: ", s2)
		
		
if (numprint-3) % 4 == 0:
	#print("Number of pages -3 is divisible by 4")
	print("On right hand side of paper, print page", 1+l)
	print("On reverse, print pages:", 2+l , ",", endpage)
	sheets += 1
	if numprint > 3:
		list1 = []
		list2 = []		
		s1 = ""	
		s2 = ""
		for i in range(0,int((numprint-2)/2)):
			sheets += 0.5
			if i % 2 == 0:
				list1.append(numprint-i-1+l)
				list2.append(i+4+l)
			else:
				list1.append(i+2+l)
				list2.append(numprint-i-1+l)
		
		for i in range(0,int((numprint-2)/2)):
			if i == int((numprint-2)/2)-1:
				s1+=str(list1[i])
				s2+=str(list2[i])
			else:
				s1+=str(list1[i])
				s2+=str(list2[i])
				s1+=", "
				s2+=", "
			
		print("Then print pages: ", s1)
		#print("Turn over printed pages top to bottom so that the printed side is facing away")
		print("Reverse the stack, print pages: ", s2)

if int(sheets)==1:
	print("You will need 1 sheet of paper")
else:
	print("You will need", int(sheets), "sheets of paper")

