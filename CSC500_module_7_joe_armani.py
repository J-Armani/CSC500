# CSC500 Module 7 CTA - Working with Dictionaries - Joe Armani
# CTA Prompt: Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet.
# It should also create a dictionary containing course numbers and the names of the instructors that teach each course.
# It should also create a dictionary containing course numbers and the meeting times of each course.

# This get_course_num() function is used for all methods.
def get_course_num(course_dict):
    while True:
        course_num = input('Enter a course number for course details. Example: CSC101: ').upper()
        if course_num in course_dict:
            return course_num
        else:
            print('Error: Course not found. Valid course numbers are:', end=' ')
            for course_num in course_to_room_dict:
                print(course_num, end=' ')
            print()

# method 1: create three separate dictionaries per the CTA prompt
course_to_room_dict = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411,
}

course_to_instructor_dict = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee',
}

course_to_meeting_time_dict = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.',
}

print('Method 1: create three separate dictionaries')
course_num = get_course_num(course_to_room_dict)
room_num = course_to_room_dict[course_num]
instructor_name = course_to_instructor_dict[course_num]
meeting_time = course_to_meeting_time_dict[course_num]
print(f'Course details: {course_num} | Room number: {room_num} | Instructor: {instructor_name} | Time: {meeting_time}')
print()

#######################################################################################################################

# method 2: create a dictionary of dictionaries
course_dict = {
    'CSC101': {
        'room_num': 3004,
        'instructor_name': 'Haynes',
        'meeting_time': '8:00 a.m.',
    },
    'CSC102': {
        'room_num': 4501,
        'instructor_name': 'Alvarado',
        'meeting_time': '9:00 a.m.',
    },
    'CSC103': {
        'room_num': 6755,
        'instructor_name': 'Rich',
        'meeting_time': '10:00 a.m.',
    },
    'NET110': {
        'room_num': 1244,
        'instructor_name': 'Burke',
        'meeting_time': '11:00 a.m.',
    },
    'COM241': {
        'room_num': 1411,
        'instructor_name': 'Lee',
        'meeting_time': '1:00 p.m.',
    },
}

print('Method 2: create a dictionary of dictionaries')
course_num = get_course_num(course_dict)
room_num = course_dict[course_num]['room_num']
instructor_name = course_dict[course_num]['instructor_name']
meeting_time = course_dict[course_num]['meeting_time']
print(f'Course details: {course_num} | Room number: {room_num} | Instructor: {instructor_name} | Time: {meeting_time}')
print()

#######################################################################################################################

# method 3: create a dictionary of lists
course_dict = {
    'CSC101': [3004, 'Haynes', '8:00 a.m.'],
    'CSC102': [4501, 'Alvarado', '9:00 a.m.'],
    'CSC103': [6755, 'Rich', '10:00 a.m.'],
    'NET110': [1244, 'Burke', '11:00 a.m.'],
    'COM241': [1411, 'Lee', '1:00 p.m.'],
}

print('Method 3: create a dictionary of lists')
course_num = get_course_num(course_dict)
room_num = course_dict[course_num][0]
instructor_name = course_dict[course_num][1]
meeting_time = course_dict[course_num][2]
print(f'Course details: {course_num} | Room number: {room_num} | Instructor: {instructor_name} | Time: {meeting_time}')
print()

#######################################################################################################################

# method 4: create a dictionary of objects
class Course:
    def __init__(self, room_num, instructor_name, meeting_time):
        self.room_num = room_num
        self.instructor_name = instructor_name
        self.meeting_time = meeting_time
        
course_dict = {
    'CSC101': Course(3004, 'Haynes', '8:00 a.m.'),
    'CSC102': Course(4501, 'Alvarado', '9:00 a.m.'),
    'CSC103': Course(6755, 'Rich', '10:00 a.m.'),
    'NET110': Course(1244, 'Burke', '11:00 a.m.'),
    'COM241': Course(1411, 'Lee', '1:00 p.m.'),
}

print('Method 4: create a dictionary of objects')
course_num = get_course_num(course_dict)
room_num = course_dict[course_num].room_num
instructor_name = course_dict[course_num].instructor_name
meeting_time = course_dict[course_num].meeting_time
print(f'Course details: {course_num} | Room number: {room_num} | Instructor: {instructor_name} | Time: {meeting_time}')
print()