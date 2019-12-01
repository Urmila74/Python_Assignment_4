""" Assignment # 4
Q1 : Use a dictionary to store information about a person you know. Store their first name, last name, age,
and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print
each piece of information stored in your dictionary. Add a new key value pair about qualification then
update the qualification value to high academic level then delete it.

"""


person ={
    
    "first_name":"Urmila",
    "last_name":"Khatri",
    "age":"23",
    "city":"khipro"
}

# Printing type for check type of data 
#print(type(person))
print("Below mentioned existing dictionary\n-----------------------------------------\n")
print(person)
print("\nAdded new key with value in dictionary from update function\n-----------------------------------------")

person.update({"qualification":"intermedaite"})
print(person)
print("\nUpdating the value of qualification key in dictionary\n-----------------------------------------\n")
print("Currently the value of qualification is "+  person['qualification'])
person['qualification'] = "Undergraduate"
print("\n\t HERE IS THE UPDATED DICTIONARY WITH UPDATED VALUES OF QUALIFICATION.\n")
print(person)
del person['qualification']

print("\n\t DELETED THE KEY OF QUALIFICATION AND BELOW MENTIONED\n")

print(person)
