#Create List
myList = []

#Add AWS Services to the list
myList.append("AWS CLI")
myList.append("EC2")
myList.append("S3")
myList.append("RDS")


#Print List, Print Length
print(myList)
print(len(myList))

#Remove item, Print List, Print Length
myList.remove("AWS CLI")
myList.remove("RDS")
print(myList)
print(len(myList))
