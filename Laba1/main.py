import json
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, id, first_name, last_name, age, email, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.age = age

    @abstractmethod
    def write_info(self, file):
        pass

    @abstractmethod
    def _get_json(self, file):
        with open(file, 'r') as f:
            info = json.load(f)
        return info


class Student(User):
    def __init__(self, id, first_name, last_name, age, email, phone, education, graduate_work, direction_of_training):
        super().__init__(id, first_name, last_name, age, email, phone)
        self.education = education
        self.graduate_work = graduate_work
        self.direction_of_training = direction_of_training

    def get_students_timetable(self):
        print('Получено студенческое расписание')

    def write_info(self, file):
        info = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'education': self.education,
            'graduate_work': self.graduate_work,
            'direction_of_training': self.direction_of_training
        }
        with open(file, 'w') as f:
            json.dump(info, f, indent=4)

    def _get_json(self, file):
        with open(file, 'r') as f:
            info = json.load(f)
        return info


class Teacher(User):
    def __init__(self, id, first_name, last_name, age, email, phone, department, work_experience, subjects):
        super().__init__(id, first_name, last_name, age, email, phone)
        self.department = department
        self.work_experience = work_experience
        self.subjects = subjects

    def get_teacher_timetable(self):
        print('Получено расписание для преподавателя')

    def write_info(self, file):
        info = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'department': self.department,
            'work_experience': self.work_experience,
            'subjects': self.subjects
        }
        with open(file, 'w') as f:
            json.dump(info, f, indent=4)

    def _get_json(self, file):
        with open(file, 'r') as f:
            info = json.load(f)
        return info


Elkin = Teacher(0, 'Alexandr', 'Elkin', 100, 'El@gmail.com', '+79084445569', 'Math', 99, ['math', 'linear algenra'])
Elkin.write_info('files\info.json')
