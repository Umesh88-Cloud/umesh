
def absentSC(listOfStudent, numberOfStudent):
   count = 0
   for i in range(numberOfStudent):
       if listOfStudent[i] == 0:
           count += 1
   return count


def maxMarks(listOfStudent, numberOfStudent):
   max = 0
   for i in range(numberOfStudent):
       if max < listOfStudent[i]:
           max = listOfStudent[i]
   return max


def largestMFreq(numberOfStudent, listOfStudent):
   count = 0
   check = maxMarks(listOfStudent, numberOfStudent)
   for i in range(numberOfStudent):
       if check == listOfStudent[i]:
           count += 1
   return count


def minMFreq(numberOfStudent, listOfStudent):
   count = 0
   check = minMarks(listOfStudent, numberOfStudent)
   for i in range(numberOfStudent):
       if check == listOfStudent[i]:
           count += 1
   return count


def minMarks(listOfStudent, numberOfStudent):
   min = listOfStudent[0]
   for i in range(numberOfStudent):
       if min > listOfStudent[i]:
           min = listOfStudent[i]
   return min


def averageOfMarks(listOfStudent, numberOfStudent):
   sumInitialize = 0
   for i in range(numberOfStudent):
       sumInitialize += listOfStudent[i]
   return (sumInitialize / numberOfStudent)

loop = True
listOfStudent = []
numberOfStudent = int(input("Enter No of Student: "))

for i in range(numberOfStudent):
   marks = int(input("Enter marks for student "+ str(i+1) +": "))
   listOfStudent.append(marks)
   
def showList():
   print(
       "--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n5)Enter 5 for minimum Marks Frequency\n6)Enter 6 for Count of absent student\n7) Enter 7 to exit")
showList()
while loop:
   choice = input("Enter your choice: ")
   if choice == "1":
       print("Average marks obtained by student is:", averageOfMarks(listOfStudent, numberOfStudent))
   elif choice == "2":
       print("Maximum marks obtained by student is: ", maxMarks(listOfStudent, numberOfStudent))
   elif choice == "3":
       print("Minimum marks obtained by student is: ", minMarks(listOfStudent, numberOfStudent))
   elif choice == "4":
       print("{maxMarks(listOfStudent, numberOfStudent)} is largest marks and its frequency is: ",
             largestMFreq(numberOfStudent, listOfStudent))
   elif choice == "5":
       print(minMarks(listOfStudent, numberOfStudent), " is minimum marks and its frequency is: ",
             minMFreq(numberOfStudent, listOfStudent))
   elif choice == "6":
       print("Number of absent student are: ", absentSC(listOfStudent, numberOfStudent))
       
   elif choice == "8":
       loop = False
   else:
       print("You entered wrong choice try again")

