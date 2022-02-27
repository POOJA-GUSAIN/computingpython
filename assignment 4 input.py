#Q1
print("Q1")
def hanoi_tower(n,A,B,C):
    if n==1:
        #only one disk is present
        print("move 1st disk from",A,"to",C)
        return
    hanoi_tower(n-1,A,C,B) 
    print("move",n,"th disk from",A,"to",C)
    hanoi_tower(n-1,B,A,C)

hanoi_tower(3,"A","B","C")  

print("\n")

#Q2
print("Q2")
#iterative approach
n=int(input("enter the number of rows you want in pascal triangle: "))
for i in range (1,n+1):
    for j in range(0,n-i+1):
        print(" ",end=" ")

    c=1
    for j in range(1,i+1):
        print(" ",c,end=" ")

        c=c*(i-j)//j
    print() 


#recursive approach
n=int(input("Enter no of rows for Pascals triangle:"))
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

for i in range(n):
    for col in range (n-1,i,-1):
        #for left spacing
        print(end=" ")
    for col in range(i+1):
        #nCr=n!/((n-r)!*n!)
        val=int(fact(i)/(fact(col)*fact(i-col)))
        print(val,end=" ")
    print()                

print("\n")   

#Q3
print("Q3")
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
result=divmod(num1,num2)
print("Quotient is ",result[0],"remainder is ",result[1])
#(a)
function_call=callable(divmod)
print("(a) ",function_call)
#(b)
all_zeros=all(result)
#returns TRUE if all are non zeros
print("(b)",all_zeros)
#(c)
new_tuple=result+(4,5,6)
print(new_tuple)
filtered_tuple=tuple(filter(lambda x: x<=4,new_tuple))
print("(c) ",filtered_tuple)
#(d)
form_a_set=set(filtered_tuple)
print("(d) ",form_a_set)
#(e)
new_set=frozenset(form_a_set)
#frozenset is immutable
print("(e)",new_set)
#(f)
max_of_set=max(new_set)
print("maximum of set is",max_of_set)
print("the hash value of max of set is",hash(max_of_set))

print("\n")

#Q4
print("Q4")
class Student:
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno

    def details(self):
        print("name: ",self.name)
        print("rollno: ",self.rollno)

    def __del__(self):
        print("done")

    
student1=Student("pooja", 52)
student1.details()
del student1 

print("\n")

#Q5
print("Q5")
class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def print_details(self):
        print("name: ",self.name)
        print("salary: ",self.salary)

    def __del__(self):
        print("done")

    
employee1=employee("mehak", 40000)
employee2=employee("ashok", 50000)
employee3=employee("viren", 60000)
employee1.print_details()
employee2.print_details()
employee3.print_details()
#(a)
print("(a)updated record of mehak-")
employee1.salary=70000
employee1.print_details()
#(b)
#detete record of viren
del employee3 
print("\n")

#Q6
print("Q6")
george=input("enter word utterd by george: ")
barbie=input("enter word created by barbie using same letters as george: ")
sorted_barbie=sorted(barbie)
sorted_george=sorted(george)

if sorted_barbie==sorted_george:
    #creates a list of letters after sorting which should be same for their true friendship
    print("Their friendship is true.")
else:
    print("Their friendship is fake.")    
     

