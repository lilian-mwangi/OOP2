#NB: The blank print statement is meant to output a blank line for readability
#ArithmeticOperators
print('Arithmetic Operators:')
a = 5
b = 2

print(a+b)  #addition

print(a-b)  #subtraction

print(a*b)  #multiplication

print(a/b)  #division

print(a%b)  #modulus

print(a**b) #exponent

print(a//b) #floordivision

print()

#Comparison Operators
print('Comparison Operators:')

print(a==b) #False

print(a!=b) #True

print(a>=b) #True

print(a<=b) #False

print(a>b)  #True

print(a<b)  #False

print()

#Assignment Operators
print('Assignment Operators:')

#The following function prints the result of variable c
def cee(c):
    print('Value of c is', c)
    return

c = a + b #=
cee(c)

c+=b     #c=c+b
cee(c)

c-=b     #c=c-b
cee(c)

c*=b     #c=c*b
cee(c)

c/=b     #c=c/b
cee(c)

c%=b     #c=c%b
cee(c)

c**=b    #c=c**b
cee(c)

c//=b    #c=c//b
cee(c)

print()

#Bitwise Operators
x = 20      #0001 0100
y = 13      #0000 1101

print('Bitwise Operators:')

#The following function prints the result of var ans
def bit(ans):
    print("Your binary value is =", "{:08b}".format(ans))
    return

#Binary OR
ans = x|y
bit(ans)

#Binary AND
ans = x&y
bit(ans)

#Binary XOR
ans = x^y
bit(ans)

#Binary One's Complement (not)
ans = ~y
bit(ans)

#Binary Left Shift
ans = x<<2
bit(ans)

#Binary Right Shift
ans = x>>2
bit(ans)

print()

#Logical Operators
print('Logical Operators:')

#AND
print(bool(a and b))

#OR
print(bool(a or b))

#NOT
print(not(a and b))

print()
 
#Identity Operators
print('Identity Operators:')

#is
print(a is b)   #False

#is not
print(a is not b)   #True

print()

#Membership Operators
print('Membership Operators:')

myList = ["The Prestige", "The Social Network", "Skyscraper", "Mulan"]
nowPlaying = "Mulan"

#in
print(nowPlaying in myList)   #True

#not in
print(nowPlaying not in myList)   #False