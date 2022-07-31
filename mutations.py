#Objective: Read a given string, change the character at a given index and then print the modified string. 
def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    string_list = ''.join(string_list)
    return string_list

if __name__ == '__main__':
    #s = input()
    #i, c = input().split()
    
    s = "hey"
    i = 1
    c = "g"
    s_new = mutate_string(s, int(i), c)
    print(s_new)