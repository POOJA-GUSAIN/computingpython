#Q1
print("ANS 1")
def word_count(str):
    counts=dict()
    words=str.split()

    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
text=input("enter a string:")
print(word_count(text))
print("\n")


#Q2
print("ANS 2")
year=int(input("Enter a year(1800-2025):"))
if (year%4==0):
    leap_year=True
else:
    leap_year=False

month=int(input("Enter a month(1-12):"))
if month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28
elif month in (1,3,5,7,8,10,12):
    month_length=31
else:
    month_length=30

day=int(input("Enter the day(1-31):"))
if day<month_length:
    day+=1
else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1

print("The next date is:",(day,month,year)) 
print("\n")                                           


#Q3
print("ANS 3")
def square(list):
    final=[(num,num*num) for num in list]
    return final
list2=[3,9,10]
print(square(list2)) 
print("\n")   


#Q4
print("ANS 4")
grade_point=int(input("Enter grade points[4-10]:"))
if grade_point==10:
    print("your grade is A+ and Outstanding performance.")
elif grade_point==9:
    print("your grade is A and Excellent performance.")
elif grade_point==8:
    print("your grade is B+ and Very Good performance.")
elif grade_point==7:
    print("your grade is B and Good performance.")
elif grade_point==6:
    print("your grade is C+ and Average performance.")
elif grade_point==5:
    print("your grade is C and Below Average performance.")
elif grade_point==4:
    print("your grade is D and Poor performance.")
else:
    print("grade point is out of RANGE.")
print("\n")


#Q5
print("ANS 5")
string="ABCDEFGHIJK"
string_length=len(string)
for i in range (string_length):
    for j in range (i):
        print(" ",end="")
    for j in range (string_length-2*i):
        print(string[j],end="")
    print()



#Q6
print("ANS 6")
dic={}
while True:
    more=input("Enter Y (if you want to add in dictionary),else enter N: ")
#Y for yes and N for no
    if more=="N":
        break
    elif more=="Y":
        sid=int(input("Enter SID of student: "))
        name=input("Enter name of student: ")
    dic[sid]=name
print("the dictionary is: ",dic)
print("\n")

#part(a)
print("the students details are as follows:")
for sid in dic:
    print("the sid is: ",sid,"and name of student is: ",dic[sid])
print("\n")

#part(b)
sort_by_name={k:v for k,v in sorted(dic.items(),key=lambda v: v[1])}
print("sorted by name:",sort_by_name)

#part(c)
sort_by_sid={k:v for k,v in sorted(dic.items())}
print("sorted by SID:",sort_by_sid)
print("\n")

#part(d)
ask_for_sid=int(input("enter SID of student to know the name: "))
got_name=dic[ask_for_sid]
print("the name of this student is",got_name)
print("\n")



#Q7
print("ANS 7")
n=int(input("enter number of terms you want in fibonacci sequence(n):"))
a=0
b=1
print(a)
print(b)
for number in range (1,n-1):
    c=a+b
    print(c)
    a,b=b,c

def fibosum(n):
    if n==1 or n==0:
        print(n)
    else:
        sum=0
        a=0
        b=1
        sum=a+b
        for i in range (1,n-1):
            c=a+b
            sum+=c
            a=b
            b=c    
        return(sum)

sum_of_fibonacci=fibosum(n)
print("average of fibonacci is ",(sum_of_fibonacci)/n)    
print("\n")


#Q8
print("ANS 8")
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#part(a)
set4=(set1|set2)-(set1&set2)
print("part(a):",set4)

#part(b)
set5=(set1|set2|set3)-(set1&set2)-(set2&set3)-(set1&set3)-(set1&set2&set3)
print("part(b):",set5)

#part(c)
set6=((set1&set2)|(set2&set3)|(set1&set3)-(set1&set2&set3))
print("part(c):",set6)

#part(d)
new_set={(integer) for integer in range (1,10)}
set7=(new_set)-(set1)
print("part(d):",set7)

#part(e)
set8=(new_set)-(set1|set2|set3)
print("part(e):",set8)

print("\n")











