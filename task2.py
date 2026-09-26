# def num(a):
#     if  a>=0:
#         print("positive number")
#     elif a<=0:
#         print("negative number")
#     else:
#         print("zero")

# num(1)
# num(0)
# num(-1)

#odd or even
def num(a):
    if a%2==0:
        return("even")
    
    else:
        return("odd")

print(num(5))

# #largest among three numbers
# a=(input("enter the first number:"))
# b=(input("enter the second number:"))
# c=(input("enter the third number:"))
# def largest(a,b,c):


#     if a>b and b>=c:
#         print("largest",a)
#     elif b>=c and c<=a:
#         print("largest",b)
#     else:
#         print("largest",c)

# a=(input("enter the first number:"))
# b=(input("enter the second number:"))
# c=(input("enter the third number:"))
# largest(a,b,c)

#length of a string
def make_capital(a):
    return a.upper()

a= input("Enter a word: ")
print("capitalized the word:", make_capital(a))