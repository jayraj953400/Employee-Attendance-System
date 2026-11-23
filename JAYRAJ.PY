import json
import os
from datetime import datetime

FILE = "attendance.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data():
    with open(FILE, "w") as f:
        json.dump(employees, f, indent=4)

employees = load_data()
def add_employee():
    name = input("Name: ").strip()
    if not name:
        print("Invalid name.")
        return
    emp_id = "E" + str(101 + len(employees))
    while emp_id in employees:
        emp_id = "E" + str(int(emp_id[1:]) + 1)
    employees[emp_id] = {
        "name": name,
        "records": {}
    }
    save_data()
    print(f"Employee added: {emp_id} | {name}")
    
def mark_attendance():
    emp_id = input("Employee ID:").strip().upper()
    if emp_id not in employees:
        print(f"Employee {emp_id} not found.")
        return
    date = input("Date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return
    status = input("Status (P/A/L):").strip().upper()

    if status not in ["P", "A", "L"]:
        print("Invalid status.Enter P, A or L.")
        return

    records = employees[emp_id]["records"]
    if date in records:
        print(f"Attendance for {date} is already marked.")
    records[date] = status
    save_data()
    print("Attendance marked succesfully.")

def show_report():
    emp_id = input("Employee ID: ").strip().upper()

    if emp_id not in employees:
        print(f"Employee {emp_id} not found.")
        return
    employee = employees[emp_id]
    records = employee["records"]

    present = list(records.values()).count("P")

    absent = list(records.values()).count("A")

    leave = list(records.values()).count("L")

    print(f"{employee['name']}: Present {present} | Absent {absent} | Leave {leave}")
    
    total = len(records)
    
    if total == 0:
        print("(no records)")  
    else:
        percentage = (present / total) * 100
        print(f"Attendance:{percentage:.2f}%")
            
    
while True:
    print("\n--- Employee Attendance system ---")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. View Report")
    print("4 Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_employee()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        show_report()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. please try again.")