# Declaration of the dictionary variable

student = {
    "name" : "Udit",
    "age" : 11,
    "class" : "11th"
}

print(student)    # Print the entire dict

print(student["age"])  # Print only a single value for the key passed.  

print(type(student))

# ==================

# Now, array of Dictionaries are as : 

students = [
    {
        "name" : "udit",
        "age" : 12
    },

    {
        "name" : "uditi",
        "age" : 121
    },
    
    {
        "name" : "uditiya",
        "age" : 1212
    }
    
]

print(students[1]["name"])