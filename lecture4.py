#dictonary and set in python
info={
    "name":"laxmi singh",
    "subjects":["python","java","c"],
    "topics":("dict","set"),
    "age":21,
    "is adult":True,
    12.32:23
}
print(type(info))
print(info)
print(info["name"])
print(info["subjects"])
print(info["topics"])
#print(info["surname"])      gives error
info["name"]="laxmi kumari singh"   # assign new value
print(info)
info["college"]="tnb college"    #   add new value
print(info)
null_dict={}      #null dictonary
null_dict["name"]="laxmi singh"
print(null_dict)

#nested dictonary
student={
    "name":"laxmi singh",
    "subjects":{
        "phy":98,
        "chem":98,
        "maths":97
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["phy"])

#dictonaries methods
print(student.keys())
print(list(student.keys()))   #typecast in list
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))
print(list(student.items()))