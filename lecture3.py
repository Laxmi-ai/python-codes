#lists and tuples
marks=[1,2,3,4,5]
print (marks)
print(type(marks))
print(marks[2])
print(len(marks))
student=["laxmi",34,"bhagalpur"]
print(student)
student[0]="laxmi singh" 
print(student)
#print(student[6]) #gives error ...list  index out of range

#list slicing  ..... similar to string slicing

print(marks[1:3])    #[2,3]
print(marks[:4])    #same as [0:4]
print(marks[1:])    # same as [1:len(marks)]
print(marks[-3:-1])
# list mrthods 
list=[34,56,76,87]
print("list=",list)
list.reverse()  # reverse the list
print( "reverse=", list)
list.append(45)     #add element at the ends
print("add element="  , list)
list.sort()   #assending order 
print( "assending order=",  list)
list.sort(reverse=True)    #decending order 
print( "decemding order =" , list)
list.insert(1,44)     #insert element at endex
print( "insert element at index", list)


list=["carrot","banana","mango"]
print("list=",list)
list.reverse()  # reverse the list
print( "reverse=", list)
list.sort()   #assending order 
print( "assending order=",  list)
list.sort(reverse=True)    #decending order 
print( "decemding order =" , list)


#tuples in python
tup=(2,1,3,1)
print(type(tup))
print(tup[1])
print(tup[3])
tup=(1,)     #, is compulsary in tuple to tell compliler its type is tuple
print(type(tup))
tup=(1)
print(type(tup))

#wap to ask the user to enter name of 3 favourite movies and store them in the list
movies=[]
movie1=input("enter 1st movie ")
movie2=input("enter 2nd movie ")
movie3=input("enter 3rd movie ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#wap to check if a list contain a palindrom of element
#list1=list(input("enter elements to check palindrome no."))
list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else: 
    print("not palindrome")   

grade=("c","d","a","b","b","a",)
print(grade.count("a"))

#store the above values in a list and sort them from "a" to "d".

grade=["c","d","a","b","b","a"]
grade.sort()
print(grade) 