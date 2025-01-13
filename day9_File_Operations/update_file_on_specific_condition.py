# Program to update the server configuration file when the Max Count for the system = 200. Change it to 500 in conf file. 

def update_file (file_path, key, value):

    with open(file_path,"r") as file:
        lines = file.readlines()

    
    with open(file_path,"w") as file2:
        for line in lines:
            if key in line:
                file2.write(key + "=" + value + "\n")
            
            else:
                file2.write(line)


server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '600'  # New maximum connections allowed

update_file ( server_config_file, key_to_update, new_value)