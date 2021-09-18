class School:

    def __init__(self):
        self.__name = ""

    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''
    def setName(self, name):
        self.__name = name

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''
    def getName(self):
        return self.__name

if __name__ == '__main__':
    school = School()
    school.setName("MIT")
    print(school.getName())  # should return "MIT" as a result.