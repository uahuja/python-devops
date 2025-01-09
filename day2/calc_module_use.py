# Importing the entire module ( set of 4 functions)
import calc as calc_old
import calc_return as calc_new

# Calling the entire module , so all three functions would be called.
calc_old     

# Below is the calling if we just have to call a single function. 

calc_old.add();
calc_old.sub();
calc_old.mul();

print("Sum is :", calc_new.add(4,6))
print("Product is :", calc_new.mul(3,6))
