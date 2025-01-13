arn = "arn:aws:iam::123456789012:user/uditahuja"

# Here the 'split' function is basically splitting the string into 2 parts 
# Which is a list of strings and we are taking the second one from the list 
print(arn.split('/')[1])
name = arn.split('/')[1];

name2 = "new";

#Using 'upper' function to make it caps on
print(name.upper());
print(name.lower());

# Replace function to replace some characters
name3 = name2.replace('e','o');
print(name3)

# '+' operator for Strng Concatenation 
result = name + " " + name2;
print(result);

# Find Length of the string by 'len' function
print(len(result))

# 'Strip' function only removed spaces from front
spaceText= "    My name is udit Ahuja"
print(spaceText.strip());

#IMPORTANT
# split will create a list of all the words based on delimiter
str = 'My name is Udit Ahuja'
words = str.split(' ')
print(type(words))
print("Words :", words)
