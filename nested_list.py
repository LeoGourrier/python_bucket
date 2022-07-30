#Objective: Print the name of the student with the second lowest grade
#If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
records = []

#store only the grades from the records list
grades = []


#Get the nth lowest grade
def get_lowest(list_grades,last=1):
    for name, grade in records:
        grades.append(grade)
    
    list_grades.sort(reverse = False)
    lowest_grade = list_grades[last-1]
    return lowest_grade
    
#Get name(s) of the nth lowest grade holder(s)
def get_names(last):
    the_grade = get_lowest(grades,last)
    names = []
    for name, grade in records:
        if grade == the_grade:
            names.append(name)
    names.sort()
    for _ in names:
        print(_)
            
#get_names(2)

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    #print(records)
    get_names(2)