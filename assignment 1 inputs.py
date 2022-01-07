print("question 1")
p=int(input("type a number = "))
q=int(input("type another number = "))
r=int(input("type another number = "))
s=(p+q+r)/3
print("the average of the entered numbers is = ",s)


print("question 2")
p=float(input("enter gross income to the nearest penny: "))
q=10000
print("standard deduction = $10,000")
r=int(input("number of dependents: "))
s=r*3000
print("dependent deduction is: $3000 per dependent")
t=p-q-s
print("taxable income is: $",t,)
u=t*20/100
print("your income tax amount is: $",u)


print('question 3')
p=int(input("enter your SID:"))
q=str(input("enter name:"))
r=str(input("gender(use F for female, M for male, O for other):"))
s=(input('enter course name:'))
t=float(input("enter CGPA:"))
list1=[p,q,r,s,t]
print("Student Info:",list1)


print('question 4')
print("max marks = 50 ")
p=float(input("enter student 1 marks:"))
q=float(input("enter student 2 marks:"))
r=float(input("enter student 3 marks:"))
s=float(input("enter student 4 marks:"))
t=float(input("enter student 5 marks:"))
list1=[p,q,r,s,t]
print("list of marks obtained by students:",list1)
list1.sort()
print("sorted list of student's marks:", list1)


print('question 5')
list1=['Red','Green','White','Black','Pink','Yellow']
print("COLOR",list1)
print("(a):")
del list1[3]
print("COLOR",list1)
print("(b):")
list2=['Red','Green','White','Black','Pink','Yellow']
del list2[3]; list2[3]="Purple"
print("COLOR:",list2)

