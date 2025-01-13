import requests

# Search for the Git Pull API in official github docs. 
# https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests
# /repos/{owner}/{repo}/pulls

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# Here , response is an object and not just a list.
# so , this print statememt won't work. 
print(response)

print(type(response))

# Hence, we use this. 
#print (response.json())   

# Now, JSON here is automatically converted to dictionary internally. 

# Now, to print any respective data, we can use the array method of reference.
# Compare the JSON respopnse from browser to see all the keys properly. 

print ( response.json()[1]["id"])
print ( response.json()[4]["user"]["login"])

output = response.json()

for i in range(len(output)):
    print(output[i]["user"]["login"])

# better way : 

for i in output:
    print(i["user"]["login"])