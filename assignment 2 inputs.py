print('question 1')
print('\n')
a='Python is a case sensitive language'
print(a)
print('(a)')
print('  length of string is: ',len(a))
print('(b)')
b=a[::-1];print('  reverse of string: ',b)
print('(c)')
c=a[10:27]
print('  stored part of given string: ',c)
print('(d)')
d='object oriented ' 
e=a.replace(c,d)
print('  replaced output: ',e)
print('(e)')
print('  index of substring "a" is: ',a.index('a'))
print('(f)')
print('  ',a.replace(' ',''))


print('question 2')
print('\n')
a='Aakanksha Kataria'
b='21104025'
c='Electrical Engineering'
d='9.1'
print(' Hey, %s here! \n My SID is %s \n I am from %s department and my CGPA is %s'%(a,b,c,d))


print('question 3\n')
a=56
b=10
print('a=56')
print('b=10')
print('(a)')
print('  a&b=',a&b)
print('(b)')
print('  a|b=',a|b)
print('(c)')
print('  a^b=',a^b)
print('(d)')
print('  left shift a=',a<<2)
print('  left shift b=',b<<2)
print('(e)')
print('  right shift a=',a>>2)
print('  right shift b=',b>>4)


print('question 4\n')
a=input('enter a number a: ')
b=input('enter a number b: ')
c=input('enter a number c: ')
if a>b and b>c:
    print('greatest number is a')
elif a<b and c<b:
    print('greatest number is b')
elif a<c and b<c:
    print('greatest number is c')
    

print('question 5\n')
a=input('entre a string: ')
b='name'
if b in a:
    print('is name present in string? : Yes')
else:
    print('is name present in string? : No')


print('question 6\n')
A=float(input('enter side length of triangle(a): '))
B=float(input('enter side length of triangle(b): '))
C=float(input('enter side length of triangle(c): '))
a=round(A)
b=round(B)
c=round(C)
if a+b<c:
    print('is triangle possible? : No')
elif b+c<a:
    print('is triangle possible? : No')
elif c+a<b:
    print('is triangle possible? : No')
else:
    print('is triangle possible? : Yes')



