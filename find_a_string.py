#Objective: In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
#String traversal will take place from left to right, not from right to left. 

def count_substring(string, sub_string):
    count = 0
    if len(string) > len(sub_string):
        #Will start at index 0 of string and loop through based on the len of substring
        return count
    else:
        return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)