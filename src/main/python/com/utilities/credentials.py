import configparser
# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('../resources/credential.ini')

print(config)
# Get values from the 'Settings' section
username = config['Settings']['username']
password = config['Settings']['password']


def login(user, pwd =''):
    print(f'Username: {username}')
    print(f'password: {pwd}')

print(__name__)
if __name__ == '__main__':
    login(username, password)
    # print(f'Password: {password}')