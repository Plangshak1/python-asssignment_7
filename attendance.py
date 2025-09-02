"""
Attendance Register

Task: 
- Track attendance of students. 
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports. 
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True). 

// NOT FOR THIS ASSIGNMENT 
Future OOP Extension:
 - Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
 """ 

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent_days": []
        }
    else:
        print(f"Student ID {student_id} is already registered.")

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for sid in student_ids:
        if sid in attendance:
            if today not in attendance[sid]["present_days"]:
                attendance[sid]["present_days"].append(today)
            # Remove from absent if marked earlier
            if today in attendance[sid]["absent_days"]:
                attendance[sid]["absent_days"].remove(today)
        else:
            print(f"Student ID {sid} not found!")

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    for sid in student_ids:
        if sid in attendance:
            if today not in attendance[sid]["absent_days"]:
                attendance[sid]["absent_days"].append(today)
            # Remove from present if marked earlier
            if today in attendance[sid]["present_days"]:
                attendance[sid]["present_days"].remove(today)
        else:
            print(f"Student ID {sid} not found!")

def get_report(**kwargs):
    """
    Generate attendance report with optional filters.
    kwargs:
      - only_present=True → show only present students
      - only_absent=True → show only absent students
    """
    report = {}

    today = str(datetime.date.today())
    for sid, record in attendance.items():
        is_present_today = today in record["present_days"]
        is_absent_today = today in record["absent_days"]

        if kwargs.get("only_present") and not is_present_today:
            continue
        if kwargs.get("only_absent") and not is_absent_today:
            continue

        report[sid] = record

    return report


register_student("S001", "Alice")
register_student("S002", "Bob")
register_student("S003", "Charlie")

mark_present(["S001", "S002"])
mark_absent(["S003"])

print("\n--- Full Report ---")
print(get_report())

print("\n--- Only Present ---")
print(get_report(only_present=True))

print("\n--- Only Absent ---")
print(get_report(only_absent=True))

