import csv

try:
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        total_salary = 0

        print("EMPLOYEE PAYROLL SUMMARY")
        print("-----------------------------------")

        for emp in reader:
            basic = float(emp["Basic"])
            allowance = float(emp["Allowance"])
            deduction = float(emp["Deduction"])

            gross = basic + allowance
            net = gross - deduction

            total_salary += net

            print("\nEmployee ID:", emp["ID"])
            print("Name:", emp["Name"])
            print("Gross Salary:", gross)
            print("Deduction:", deduction)
            print("Net Salary:", net)

        print("\n-----------------------------------")
        print("Total Salary:", total_salary)

except FileNotFoundError:
    print("Employee CSV file not found!")

except ValueError:
    print("Invalid salary data in CSV file!")
