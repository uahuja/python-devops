
import sys
import os

print(os.getenv("password"))

n1=os.getenv("token")
n2=os.getenv("keys")

print(n1 + " This is the way ENV works " + n2)
