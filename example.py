
import os

# path = os.getenv('MY_DB_URL')

# Printing the total environment variables

for k, v in os.environ.items():
    print(f'{k}={v}')

# getting the particular environment variable  
home_dir = os.environ['HOME']
username = os.environ['USER']
print(f'{username} home directory is {home_dir}')



# Set Environment variable using python

env_var = input('Please enter environment variable name:\n')

env_var_value = input('Please enter environment variable value:\n')

os.environ[env_var] = env_var_value

print(f'{env_var}={os.environ[env_var]} environment variable has been set.')


