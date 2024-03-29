class Student:
    def __init__(self, id):
        self.id = id

class Class:
    '''
     * Declare a constructor with a parameter n which is the total number of
     * students in the *class*. The constructor should create n Student
     * instances and initialized with student id from 0 ~ n-1
    '''
    def __init__(self, n):
        self.students = [Student(i) for i in range(n)]