# College Admission Project in Python
# Features: Course list with fees, student registration, fee payment, admission status

students = []

course_fees = {
    "Computer Science": 25000,
    "Information Technology": 22000,
    "Mechanical Engineering": 26000,
    "Civil Engineering": 24000,
    "Electronics": 23000,
    "Business Administration": 18000
}

print("Welcome to the College Admission System")

while True:
    print("\nMenu:")
    print("1. Apply for Admission")
    print("2. View Course List and Fees")
    print("3. View Admission List")
    print("4. Check Admission Status")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))

        if age < 18:
            print("Admission is only allowed for students aged 18 and above.")
            continue

        print("\nAvailable Courses and Fees:")
        for course, fee in course_fees.items():
            print(f"- {course}: Rs.{fee}")

        course = input("Enter preferred course: ")

        if course not in course_fees:
            print("Invalid course selected. Please choose from the available courses.")
            continue

        fee = course_fees[course]

        print(f"\nStudent Details:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Course: {course}")
        print(f"Admission Fee: Rs.{fee}")

        payment = input("Do you want to pay the fee now? (yes/no): ").lower()
        if payment == 'yes':
            print(f"Payment successful for {name}.")
            status = "Admitted"
        else:
            status = "Pending"

        student = {
            "name": name,
            "age": age,
            "course": course,
            "fee": fee,
            "status": status
        }
        students.append(student)
        print(f"{name} has been added to the admission system.")

    elif choice == '2':
        print("\nCourse List and Fees:")
        for course, fee in course_fees.items():
            print(f"- {course}: Rs.{fee}")

    elif choice == '3':
        if not students:
            print("No students have applied yet.")
        else:
            print("\nAdmission List:")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']} - {student['course']} - Rs.{student['fee']} - {student['status']}")

    elif choice == '4':
        if not students:
            print("No student records available.")
        else:
            name = input("Enter student name to check status: ")
            found = False
            for student in students:
                if student['name'].lower() == name.lower():
                    print(f"\nStatus for {student['name']}:")
                    print(f"Course: {student['course']}")
                    print(f"Course Fee: Rs.{student['fee']}")
                    print(f"Admission Status: {student['status']}")
                    found = True
                    break
            if not found:
                print("Student not found.")

    elif choice == '5':
        print("Thank you! College admission system closed.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
