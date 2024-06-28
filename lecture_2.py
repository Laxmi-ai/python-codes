#string
str1="laxmi"
str2="singh"
final_str= str1 +str2
print(final_str)
length= len(final_str)
print(length)
str4 = 'laxmi singh'
str5 = """laxmi singh"""
lent = len(str5)
print(lent)
#slicing
str="laxmi singh"
print(str[0:5])
print(str[:11])
print(str[0:7])
#negative slicing
print(str[-5:-1])
#string function
string ="this is my room."
print(string.endswith("oom.")) #str.endswith
print(string.endswith("th"))
print(string.capitalize()) #to capitalize the first letter
print(string) #it will again print the same letter
print(string.replace("i" ,"u")) #str.replace
print(string.replace("this","that"))
print(string.find("is"))
print(string.find("w"))
print(string.count("i"))
#wap to input user's first name and print its length
name=input("write your name=")
print("lenth of my name is :",len(name))
# wap to finf the opccurance of $ in a string
stri="my $ name$ is $ laxmi$ "
print(stri.count("$"))
marks=int (input("enter the marks :"))
if(marks>90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print( "grade of student",grade)             
#check wheather the no.is odd or even
num=int(input("enter a no."))
if(num%2==0):
    print("even number")
else:
    print("odd number")   

#wap yo find the greatest of 3 number entered by the user
a=int(input("enter 1st no. ="))
b=int(input("enter 2nd no. ="))
c=int(input("enter 3rd no. ="))
if(a>b and a>c ):
    print("a is greater")
elif(b>c ):
    print("b is greater no.")
else:
    print("c is greater")         
#wap to check wheather the no is multiple of 7 or not
x=int(input("enter a number= "))
if(x%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")    