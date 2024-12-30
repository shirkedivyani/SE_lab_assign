class StudentGrades:
    """
    A class to manage student grades and determine pass/fail status.
    """

    def __init__(self, student_name):
        self.student_name = student_name  # Name of the student
        self.CA1_CA2 = 0  # Combined marks for CA1 and CA2
        self.MSE = 0      # Marks for MSE
        self.ESE = 0      # Marks for ESE

    def set_grades(self, CA1_CA2, MSE, ESE):
        """
        Set grades for CA1+CA2, MSE, and ESE. Ensures values are within valid ranges.
        """
        if not (0 <= CA1_CA2 <= 20):
            raise ValueError("CA1_CA2 must be between 0 and 20")
        if not (0 <= MSE <= 20):
            raise ValueError("MSE must be between 0 and 20")
        if not (0 <= ESE <= 60):
            raise ValueError("ESE must be between 0 and 60")

        self.CA1_CA2 = CA1_CA2
        self.MSE = MSE
        self.ESE = ESE

    def check_pass_fail(self):
        """
        Check pass/fail based on grades.
        Criteria: ESE >= 20 OR total >= 40 to pass.
        """
        total = self.CA1_CA2 + self.MSE + self.ESE
        if self.ESE >= 20 or total >= 40:
            return "Pass"
        return "Fail"

""""
if __name__ == "__main__":
    student_name = input("Enter the student's name: ")
    student = StudentGrades(student_name)

    try:
        # Input grades
        CA1_CA2 = int(input("Enter CA1 + CA2 marks (0-20): "))
        MSE = int(input("Enter MSE marks (0-20): "))
        ESE = int(input("Enter ESE marks (0-60): "))

        # Set grades
        student.set_grades(CA1_CA2, MSE, ESE)

        # Check pass/fail
        print(f"Student Name: {student.student_name}")
        print("Result:", student.check_pass_fail())

    except ValueError as e:
        print("Error:", e)
"""