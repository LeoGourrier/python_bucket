from random import *
import string


def gen_ec2_names():
    
    department = ["accounting", "marketing","finops"]
    
    department_input = input("What is the name of your department?")
    
    if department_input.lower() in department:
        number_of_random_names = int(input("How many EC2 names do you want to generate?"))
        
        for _ in range(number_of_random_names):
            print(department_input.lower() + "_" + ''.join(choices(string.ascii_letters + string.digits + string.punctuation, k=5)))
    else:
        print("Your department is not an option. Perhaps you should use a different app.")
    
gen_ec2_names()