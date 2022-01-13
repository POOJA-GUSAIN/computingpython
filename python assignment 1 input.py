#question 1
print("Q1. to find average of 3 numbers")
first_no=int(input("enter first no.:"))
second_no=int(input("enter second no.:"))
third_no=int(input("enter third no.:"))
sum=(first_no+second_no+third_no)
average=sum/3
print(average)
print("\n")

#question 2
print("Q2. to find income tax")
gross_income=int(input("enter your gross income:"))
no_of_dependents=int(input("enter your no of dependents:"))
standard_deduction=10000
dependent_deduction=3000
taxable_income=(gross_income)-(standard_deduction)-(dependent_deduction)*(no_of_dependents)
income_tax=(float(taxable_income))*(0.2)
print(income_tax)
print("\n")

#question 3
print("Q3. a list of different data types")
list=[21104052,"pooja_gusain","F","BTech(EE)",9.8]
print(list)
print("\n")

#question 4
print("Q4. marks of 5 students in sorted manner")
a=int(input("enter marks of first student:"))
b=int(input("enter marks of second student:"))
c=int(input("enter marks of third student:"))
d=int(input("enter marks of fourth student:"))
e=int(input("enter marks of fifth student:"))
marks=[a,b,c,d,e]
print(marks)
sorted_list=sorted(marks)
print(sorted_list)
print("\n")

#question 5(a)
print("Q5(a)")
list=["red","green","white","black","pink","yellow"]
print(list)
list.remove("black")
print(list)
print("\n")

#question 5(b)
print("Q5(b)")
list=["red","green","white","black","pink","yellow"]
list[3:5]=["purple"]
print(list)















