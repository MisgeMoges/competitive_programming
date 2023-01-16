def gradingStudents(grades):
    # Write your code here
    
    def process_grade(grade: int) -> int:
    
        remainder = grade % 5 
        if(grade< 38):
            return grade
        elif(remainder >= 3):
            return grade + 5-remainder
        else:
            return grade
