import os
import csv

students = [
  {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
  {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
  {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
  {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
  {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
  {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
  {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
]

new_student = {
  'id': 5,
  'name': 'Demetre',
  'age': 18,
  'grade': 'A',
  'subject_name': 'Informatic',
  'mark': 94
}

folder = "folder"
filename = "students.csv"
os.makedirs(folder, exist_ok=True)
filenamepath = os.path.join(folder, filename)


fields = list(students[0].keys())

sorted_by_id = sorted(students, key=lambda student: student["id"])
with open(filenamepath, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(sorted_by_id)



def add_student(path, student_dict):
    with open(path, mode="r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))

    data.append(student_dict)
    data.sort(key=lambda x: int(x['id'])) 
    
    with open(path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)



def read_students_info(path, student_id=None):
    with open(path, mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))
        
        
        if student_id is not None:
            for row in reader:
                if int(row["id"]) == student_id:
                    return [row]
            return []
        return reader


def print_table(data_list):
    
    print("=" * 59)
    print(f"  {'id':<6} {'name':<8} {'age':<6} {'grade':<6} {'subject_name':<16} {'mark'}")
    print("=" * 59)
    for row in data_list:
        print(f"  {row['id']:<6} {row['name']:<8} {row['age']:<6} {row['grade']:<6} {row['subject_name']:<16} {row['mark']}")
    print("=" * 59)


def avgFinder(path):
    with open(path, mode="r", encoding="utf-8") as file:
        students_list = list(csv.DictReader(file))
        
    subjects = {}
    for student in students_list:
        subject = student["subject_name"]
        if subject not in subjects:
            subjects[subject] = []
        subjects[subject].append(int(student["mark"]))
        
    averages = {}
    for sub, marks in subjects.items():
        averages[sub] = round(sum(marks) / len(marks), 2) # დამრგვალება სილამაზისთვის
    return averages



def updater(path, stud_id, subject_name, new_mark):
    with open(path, mode="r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))

    found = False
    for student in data:
        if int(student["id"]) == stud_id and student["subject_name"].lower() == subject_name.lower():
            student["mark"] = str(new_mark)
            found = True
            break

    if not found:
        return "სტუდენტი ამ ID-ით და საგნით ვერ მოიძებნა!"

    with open(path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    return "წარმატებით განახლდა!"



add_student(filenamepath, new_student)


print("ყველა სტუდენტი (Demetre-ს ჩათვლით და დასორტირებული):")
print_table(read_students_info(filenamepath))

print("\nმხოლოდ ID 11 სტუდენტის ძებნა:")
print_table(read_students_info(filenamepath, student_id=11))


print("\nქულის განახლება:")
print(updater(filenamepath, 8, "Physic", 10))


print("\nსაშუალო ქულები საგნების მიხედვით:")
for sub, avg in avgFinder(filenamepath).items():
    print(f"{sub}: {avg}")