print('question 1')
str=str(input('entre a string : '))
space=" " #to chek if input is single word or multiple words
if space in str:
    s2=str.split()
    s3=set(s2)
    for words in s3:
        print('frequency of',words,'=',s2.count(words)) #gives frequency of words
else:
    for l in str:
        print('frequency of',l,'=',str.count(l))#gives frequency of characters incase word


print('question 2')
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month between 1-12: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day between 1-31: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


print('question 3')
a=int(input('entre first element of list: '))#taking input of numbers to be squared from user
b=int(input('entre second element of list: '))
c=int(input('entre third element of list: '))
list1=[a,b,c] #creating list of inputs
list2=[a**2,b**2,c**2] #creating list of squares of input
output=list(zip(list1,list2))
print(output)


print('question 4')
gp=int(input('entre your grade points: '))
if gp in range(4,11):
    if gp==4:
        print('Your grade is D and Poor performance.')
    elif gp==5:
        print('Your grade is C and Below Average performance.')
    elif gp==6:
        print('Your grade is C+ and Average performance.')
    elif gp==7:
        print('Your grade is B and Good performance.')
    elif gp==8:
        print('Your grade is B+ and Very Good performance.')
    elif gp==9:
        print('Your grade is A and Excellent performance.')
    else:
        print('Your grade is A+ and Outstanding performance.')
else:
    print('ERROR: GRADE OUT OF RANGE!')


print('question 5')
n='ABCDEFGHIJK'
print(n)
for i in range(2,11):
    if i%2==0:
        print(n[:-i])
        i=i+1


print('question 6')
SID=[]
name=[]
s1=input('entre sid: ')
n1=input('entre name: ')
SID.append(s1); name.append(n1)
print('list of SID: ',SID,'\n list of name: ',name)
q=str(input('add more entries? (Y=yes/N=no): '))
while 'Y' in q:
    s2=input('entre SID: '); n2=input('entre name: ')
    SID.append(s2); name.append(n2)
    print('list of SID: ',SID,'\n list of name: ',name)
    q=str(input('add more entries? (Y=yes/N=no): '))
d=dict(zip(SID,name))
print('(a)')
print('Dictionary with SID as key and name as value: ',d)
print('(b)')
sortedv=sorted(d.values())
sortedtd={}
for i in sortedv:
    for k in d.keys():
        if d[k]==i:
            sortedtd[k]=d[k]
            break
print(sortedtd)
print('(c)')
print('(d)')
sid=input('enter SID: ')
print(d.get(sid))


print("question 7")
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")
#code for fibonacci series
else:
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    else:
        list1 = [1, 1]
        a = 1
        b = 1
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
# printing the final fibonacci series
print("\nThe fibonacci series with {n} elements is: ")
print(list1)
# Finding average of fibonacci series
sum = 0    
# finding sum of all elements in list1
for num in list1:
    sum = sum + num
average = (sum / n)
# Till two decimal place
two_decimal = "{:.2f}".format(average)
# printing average
print("\nAverage of given fibonacci series is: ",{two_decimal})


print('question 8')
s1={1,2,3,4,5}
s2={2,4,6,8}
s3={1,5,9,13,17}
print('(a)')
print((s1|s2)-(s1 & s2))
print('(b)')
print((s1|s2|s3)-(s1 & s2)-(s2&s3)-(s3&s1))
print('(c)')
print((s1&s2)|(s2&s3)|(s3&s1)-(s1&s2&s3))
print('(d)')
d=[]
for i in range(6,10):
    if i in range(1,10):
        d.append(i)
D=set(d)
print(D)
print('(e)')
print(set(range(1,10))-s1-s2-s3)




    




