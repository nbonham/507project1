#import csv

## Part 1: [8 pts] Create a dictionary of the student that is organized as shown [note that the dictionary is “pretty printed” here for readability--you don’t need to do this. Just calling print(my_dict) is OK] : - DONE
## {'Julie': {‘Assn 1’:'9', ‘Assn 2’: '19', ‘Assn 3’: '9', ‘Final Exam’: '22'},
## Student	Assn 1	Assn 2	Assn 3	Final Exam

# initialize dictionaries
studentGrades = {}
assignments = {}
finalGrades = {}
count = 0

# open the file, script out new lines and then create lists for stuff needed later, like headers, weights and max points. Also create a dictionary with keys as student names and values as a dictionary of their grades
fhand = open("gradebook.csv")
for line in fhand :
    line = line.strip('\n')
    items = line.split(",")
    #print(type(items))
    if line.startswith("Student") :
        headers = line.split(",")
        #print(headers)
    elif line.startswith("weight"):
        weights = line.split(",")
    elif line.startswith("max_points"):
        maxpoints = line.split(",")
    else:
        studentGrades[items[0]] = {headers[1] : items[1], headers[2] : items[2], headers[3] : items[3], headers[4]:items[4]}

fhand.close()

print('PART 1')
print(studentGrades)
print('')

#print(headers)
#print(weights)
#print(maxpoints)

## Part 2: [8 pts] Create a dictionary of the assignment weights and point values that is organized as shown [note that the dictionary is “pretty printed” here for readability--you don’t need to do this.Just calling print(my_dict) is OK]:
## {'Assn 1': {'weight': '0.15', 'max_points': '12'},

# needed to deal with the "student" in the header and then used similar process as in part 1
for header in headers :
    if header == "Student" :
        continue
    else :
        try:
            count += 1
            assignments[header] = {'weight' : weights[count], 'max_points' : maxpoints[count]}
        except:
            continue

print('PART 2')
print(assignments)
print('')


## Part 3:  [8 pts] Create a function ‘student_average(student_name)’ that returns the weighted final grade for the student whose name is passed into the function. [The “weighted average” is the sum of (weight * percentage grade) for all of a student’s assignments]. Print() each student’s weighted average to the console like so (your output should match the following):
## Julie : 84.33333333333333

print('PART 3')
def student_average(student_name) :
    avg = 0
    #print(studentGrades[student_name])
    a1 = (float(studentGrades.get(student_name).get("Assn 1")) / float(assignments.get('Assn 1').get('max_points'))) * float(assignments.get('Assn 1').get('weight'))
    a2 = (float(studentGrades.get(student_name).get("Assn 2")) / float(assignments.get('Assn 2').get('max_points'))) * float(assignments.get('Assn 2').get('weight'))
    a3 = (float(studentGrades.get(student_name).get("Assn 3")) / float(assignments.get('Assn 3').get('max_points'))) * float(assignments.get('Assn 3').get('weight'))
    final = (float(studentGrades.get(student_name).get("Final Exam")) / float(assignments.get('Final Exam').get('max_points'))) * float(assignments.get('Final Exam').get('weight'))
    avg = (a1 + a2 + a3 + final)*100
    return str(avg)

# (grade / max) * weight = total


for student in studentGrades :
    print(student + " : " + student_average(student))
print('')

## Part 4: [6 pts] Create a function ‘assn_average(assn_name)” that returns the average score *as a percentage* for that assignment, across all students. Print() the average score for each assignment, like so (your output should match the following):
print('PART 4')

# loop through the students and return their grades for the assignment name that is passed through, sum the grades, sum the max points and then calculate the average, returning the result
classAvgList = []

def assn_average(assn_name):
    classSum = 0
    classMax = 0
    for student in studentGrades :
        #print(student)
        classSum += float(studentGrades.get(student).get(assn_name))
        classMax += float(assignments.get(assn_name).get('max_points'))
    classAvg = (classSum / classMax)*100
    classAvgList.append(classAvg)
    return classAvg

# loop through the assignment names and pass them into the assn_average function. If statement to skip pass the "students" item in the list
for header in headers :
    if header == "Student" :
        continue
    else :
        print(header + " : " + str(assn_average(header)))

print('')


## Part 5: [5 pts extra credit] Create a function ‘format_gradebook()’ that uses string.format() to generate a single string that, when printed out, looks like this.
print('PART 5')

def format_gradebook():
    totalClassAvg = 0
    totalClassGrade = 0
    c = 0

    rowHeaders = "{0:<12}{1:>12}{2:>12}{3:>12}{4:>12}{5:>12}".format(headers[0], headers[1], headers[2], headers[3], headers[4],'Grade')
    print(rowHeaders)
    print('-'*75)
    for student in studentGrades :
        a1 = float(studentGrades.get(student).get("Assn 1"))/float(assignments.get("Assn 1").get('max_points'))*100
        a2 = float(studentGrades.get(student).get("Assn 2"))/float(assignments.get("Assn 2").get('max_points'))*100
        a3 = float(studentGrades.get(student).get("Assn 3"))/float(assignments.get("Assn 3").get('max_points'))*100
        fe = float(studentGrades.get(student).get("Final Exam"))/float(assignments.get("Final Exam").get('max_points'))*100
        grade = a1*float(weights[1])+a2*float(weights[2])+a3*float(weights[3])+fe*float(weights[4])
        totalClassGrade += grade
        c += 1
        rowStudent = "{0:<12}{1:>11.1f}%{2:>11.1f}%{3:>11.1f}%{4:>11.1f}%{5:>11.1f}%".format(student,a1, a2, a3, fe, grade)
        print(rowStudent)
    print('-'*75)
    totalClassAvg = totalClassGrade / c
    rowAverages = "{0:<12}{1:>11.1f}%{2:>11.1f}%{3:>11.1f}%{4:>11.1f}%{5:>11.1f}%".format('Average',float(classAvgList[0]),float(classAvgList[1]),float(classAvgList[2]),float(classAvgList[3]),totalClassAvg)
    print(rowAverages)

    #print("nevermind, realized how much I would have to refactor my code to make this not be a pain in the butt...")

format_gradebook()
