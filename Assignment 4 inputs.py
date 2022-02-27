print('question 1 \n')
#defining function for tower of hanoi
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
#number of discs n:
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')


print('question 2\n')
#entering number of rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#method 1: using recursions
print("\nMethod 1: using recursions:\n")
def pascal(n, ogn=n):
    if n == 0:
        return
    
    pascal(n-1,ogn)

    #printing the spaces
    print('  '*(ogn-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#Method 2: using loops
print("\nMethod 2: Using loops:\n")
for l in range(1, n+1):

    #similiar to recursions method
    print('  '*(n - l), end='')

    x = 1
    for i in range(1, l+1):

        print(x, end='   ')

        x = x * (l - i) // i
    print()


print('question 3\n')
#taking inout from user
a=int(input('enter a number: '))
b=int(input('enter another number: '))
#finding quotient and remainder
o=divmod(a,b)
print('(quotient,remainder: )',o)
#fullfilling question criterias using built-in functions
print('(a)')
print('is function callable?: ',callable(o))
print('(b)')
print('are all values non zero?: ',all(v!=0 for v in o))
print('(c)')
t=o+(4,5,6)
t=tuple(filter(lambda x:x<=4,t))
print('output with filtered values: ',t)
print('(d)')
s=set(t)
print('set: ',s)
print('(e)')
f=frozenset(s)
print('immutable set: ',f)
print('(f)')
m=max(s)
print('maximum value in set: ',m)
print('hash of max value: ',hash(m))


print('question 4\n')
#creating class
class Student:
    def __init__(self,name,rollno):
        print('student created!')
        self.name = name
        self.rollno = rollno
    def __del__(self):
        print('student destroyed!')
#creating objects in class 
s1n=str(input('enter student 1 name: '))
s1r=int(input('enter student 1 rollno: '))
s1= Student(s1n,s1r)
s2n=str(input('enter student 2 name: '))
s2r=int(input('enter student 2 rollno: '))
s2= Student(s2n,s2r)
s3n=str(input('enter student 3 name: '))
s3r=int(input('enter student 3 rollno: '))
s3= Student(s3n,s3r)
#calling __del__() function to destroy object
print('deleting student 3: ')
del s3


print('question 5\n')
#creating class to store employee's data
class Employees:
    def __init__(self,name,salary):
        print('employee added!')
        self.name=name
        self.salary=salary
    def __del__(self):
        print('employee destroyed!')
    def update(self,salary):
        self.salary=salary
        print('salary updated!')
#adding employees
e1=Employees('Mehak',40000)
e2=Employees('Ashok',50000)
e3=Employees('Viren',60000)
print('(a)\n')
#updating Mehak's salary
Employees.update(e1,70000)
print('(b)\n')
#deleting Viren's record
del e3


print('question 6\n')
#enter word by firstt friend:
w=str(input('Enter word: '))
#entering meaningfull word with same letters
tw=str(input('Enter meaningfull word for friendship test!: '))
#defining dictionary
def count_dict(w):
    count = {}
    list1 = list(w)
    n=len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]]+=1
        else:
            count[list1[i]]=1
    return count
#performing test
if count_dict(w) != count_dict(tw):
    print('EHEH! Letter not exact, friendship is FAKE!')
else:
    #Shopekeeper's input verify word meaning
    def userinput():
        ans=str(input('Does word make sense?(y or n)'))
        if ans=='y':
            print('HORRAY! your friendship is TRUE!')
        elif ans=='n':
            print('EHEH! the word does not make sense, sorry your friendship is FAKE!')
        else:
            print('ERROR! invalid input,try again!')
    userinput()
    print('')


