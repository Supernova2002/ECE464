def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def overwrite_file(filename: str, contents: str):
    with open(filename, "w") as f:
        f.write(contents)


MY_DATABASE = "my_database.txt"
STUDENTS = "students.txt"
COURSES = "courses.txt"
REGISTRATION = "registration.txt"

students = {
    1: {"name": "John"},
    2: {"name": "Steve"},
    3: {"name": "Bill"},
    4: {"name": "Bob"},
    5: {"name": "Joe"},
}
courses = {
    1: {
        "name": "Databases",
        "course_number": 465,
        "instructor": "Katz",
        "num_seats": 3,
    },
    2: {
        "name": "Compilers",
        "course_number": 466,
        "instructor": "Hak",
        "num_seats": 3,
    }
}


registrations = [
    {"student_id":1, "course_id":1},
    {"student_id":1, "course_id":2},
    {"student_id":2, "course_id":1},
]

def get_courses(student_id: int) -> list[int]:
    return [registration["course_id"] for registration in registrations if registration["student_id"] == student_id]

def num_registered_students(course_id: int)->int:
    return len([registration for registration in registrations if registration["student_id"] == course_id])


def remaining_seats(course_id: int)->int:
    return courses[course_id]["num_seats"] - num_registered_students(course_id=course_id)

def register_student(student_id: int, course_id: int) -> bool:
     """Returns false if the class is full"""
     n_seats = remaining_seats(course_id)
     if n_seats <=0:
         return False
     registrations.append({"student_id": student_id, "course_id" : course_id})
     return True

def drop_student(student_id: int, course_id: int) -> bool:
    record = [registration for registration in registrations if registration["student_id"] == student_id and registration["course_id"] = course_id]
    if not record:
        return False
    registrations.remove(record[0])
    return True

def load_registrations():
    filename = MY_DATABASE
    with open(filename,'r') as f:
        for line in f:
            student_id, course_id = line.split(",")
            register_student(int(student_id), int(course_id))
        

    

if __name__ == "__main__":
    load_registrations()
    print(registrations)