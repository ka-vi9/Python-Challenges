print("challenge 17")
pizza_slices = int (input("Enter number of pizza slices: "))
students = int (input ("Enter number of students: "))
slices_per_student = pizza_slices//students
extra_slices = pizza_slices%students
print ("Each student can have " + str(slices_per_student)+" slices of pizza, with " + str(extra_slices) + " slices left over.")

#print ("Each student can have " + str(slices_per_student)+" slices of pizza, with " + str(extra_slices) + " slices left over")
