import sys
isimler = sys.argv[2].split(",")
student_dict = dict()
with open(sys.argv[1],"r") as file1:
    students = file1.read().splitlines()
    for i in students:
        i = i.split(":")
        student_dict[i[0]] = i[1]
for i in isimler:
    try:
        print("Name: {}, University: {}".format(i,student_dict[i]))
    except KeyError:
        print("No record of ‘{}’ was found!".format(i))