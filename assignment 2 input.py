#Q1
string="python is a case sensitive language"
print("the length of the string is:",len(string))
print("the reverse string is:",string[ : :-1])
new_string=string[10:26]
print(new_string)
print(string.replace('a case sensitive','object oriented'))
print(string.index("a"))
print(string.replace(" ",""))
print("\n")


#Q2
name="Pooja Gusain"
SID=21104052
dep="electrical engineering"
CGPA=9.9
intro="Hey, {} Here! \n My SID is {} \n I an from {} department and my CGPA is {}"
formatted_intro=intro.format(name,SID,dep,CGPA)
print(formatted_intro)
print("\n")


#Q3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)
print("\n")

#Q4
first_no=int(input("enter first no-"))
second_no=int(input("enter second no-"))
third_no=int(input("enter third no-"))
print("the largest number is:", max(first_no,second_no,third_no))
print("\n")

#Q5
user=input("enter a string: ")
if "name" in user:
	print("yes")
else:
	print("no")
print("\n")


#Q6
first_side=float(input("enter first side of triangle "))
second_side=float(input("enter second side of triangle "))
third_side=float(input("enter third side of triangle "))
first=int(first_side)
second=int(second_side)
third=int(third_side)
if(first<second+third)&(second<first+third)&(third<second+first):
	print("these 3 sides CAN form a triangle")
else:
	print("these 3 sides CANNOT form a triangle")



























