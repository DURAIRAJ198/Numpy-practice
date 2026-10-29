# Art College Admission Project in Python
# Features: course list, student registration, portfolio review, scholarship status, and admission status

applicants = []

course_fees = {
    "Fine Arts": 18000,
    "Graphic Design": 20000,
    "Fashion Design": 22000,
    "Interior Design": 24000,
    "Animation": 26000,
    "Photography": 19000,
    "Sculpture": 17000
}

print("Welcome to the Art College Admission System")

while True:
    print("\nMenu:")
    print("1. Apply for Admission")
    print("2. View Art Courses and Fees")
    print("3. View Admission Applicants")
    print("4. Check Admission Status")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter applicant name: ")
        age = int(input("Enter applicant age: "))

        if age < 16:
            print("Admission is only allowed for students aged 16 and above.")
            continue

        print("\nAvailable Courses and Fees:")
        for course, fee in course_fees.items():
            print(f"- {course}: Rs.{fee}")

        course = input("Enter preferred art course: ")

        if course not in course_fees:
            print("Invalid course selected. Please choose from the available options.")
            continue

        portfolio = input("Do you have an art portfolio? (yes/no): ").lower()
        if portfolio == 'yes':
            portfolio_score = int(input("Rate your portfolio quality from 1 to 10: "))
        else:
            portfolio_score = 0

        fee = course_fees[course]
        scholarship = "No"
        if portfolio_score >= 8:
            scholarship = "Eligible"
        elif portfolio_score >= 5:
            scholarship = "Partial"

        print("\nApplicant Details:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Course: {course}")
        print(f"Admission Fee: Rs.{fee}")
        print(f"Portfolio: {'Yes' if portfolio == 'yes' else 'No'}")
        print(f"Scholarship Status: {scholarship}")

        payment = input("Do you want to pay the admission fee now? (yes/no): ").lower()
        if payment == 'yes':
            print(f"Payment successful for {name}.")
            status = "Admitted"
        else:
            status = "Pending"

        applicant = {
            "name": name,
            "age": age,
            "course": course,
            "fee": fee,
            "portfolio": portfolio,
            "scholarship": scholarship,
            "status": status
        }
        applicants.append(applicant)
        print(f"{name} has been added to the art college admission system.")

    elif choice == '2':
        print("\nArt Courses and Fees:")
        for course, fee in course_fees.items():
            print(f"- {course}: Rs.{fee}")

    elif choice == '3':
        if not applicants:
            print("No applicants have registered yet.")
        else:
            print("\nAdmission Applicants:")
            for i, applicant in enumerate(applicants, start=1):
                print(f"{i}. {applicant['name']} - {applicant['course']} - Rs.{applicant['fee']} - {applicant['status']} - Scholarship: {applicant['scholarship']}")

    elif choice == '4':
        if not applicants:
            print("No applicant records available.")
        else:
            name = input("Enter applicant name to check status: ")
            found = False
            for applicant in applicants:
                if applicant['name'].lower() == name.lower():
                    print(f"\nStatus for {applicant['name']}:")
                    print(f"Course: {applicant['course']}")
                    print(f"Course Fee: Rs.{applicant['fee']}")
                    print(f"Scholarship Status: {applicant['scholarship']}")
                    print(f"Admission Status: {applicant['status']}")
                    found = True
                    break
            if not found:
                print("Applicant not found.")

    elif choice == '5':
        print("Thank you! The art college admission system has been closed.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
