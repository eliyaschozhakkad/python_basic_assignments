print("Enter the marks scored by the students")
written_test=int(input("Written test= "))
lab_exam=int(input("lab exam= "))
assignment=int(input("Assignment= "))
overall_grade=(written_test*0.7)+(lab_exam*0.2)+(assignment*0.1)
print(f"Grade of the student is {overall_grade}")