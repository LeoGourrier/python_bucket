#Objective: In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
#String traversal will take place from left to right, not from right to left. 

def count_substring(string, sub_string):
    count = 0
    at_the_end = False  
   
    #If the substring is bigger than the string, return 0
    if len(string) > len(sub_string):
        #Iterate through the string
        for string_index in range(0, len(string)):
            if at_the_end == False:
                #Resets Substring's index
                substring_index = 0
                #reset tracker for the next set of comparisons
                tracker = 0
                #Get the comparison indexes that are the size of the sub_string for properly iterating through string
                for comparison_index in range(string_index, string_index + len(sub_string)):
                    #print(comparison_index)
 
                    #print(string[comparison_index] + " == " + sub_string[substring_index])
                    #if there's a match increase tracker
                    if (string[comparison_index] == sub_string[substring_index]):
                        tracker += 1
                    #If tracker equal the length of the sub_string, all characters matched perfectly, increase count
                    if (tracker == len(sub_string)):
                        count += 1
                        #print(count)
                    
                    substring_index += 1
                
                #Determines when we've come to the last possible iteration of the string comparisons
                if(comparison_index == len(string)-1):
                    at_the_end = True
                    #print("we're at the end" + str(comparison_index))
                    
                #print("----")
                #print(str(string_index) + "\n")
        return count
    #subtring was bigger than the string, end function
    else:
        return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    #string = 'abcdefgabcdeddefg'
    #sub_string = 'd'
    
    count = count_substring(string, sub_string)
    print(count)