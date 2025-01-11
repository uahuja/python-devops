
name = [ "Udit", "Ahuja", "Saumya", "Agrawal"]
print(type(name))
name.append("Ahuja2")
name.append("Ahuja2")
print(name)


name2 = ( "Udit", "Ahuja", "Saumya", "Agrawal" )
print(type(name2))
name2.append("Ahuja2")    # Can't happen as Tuples are immutable
print(name2)