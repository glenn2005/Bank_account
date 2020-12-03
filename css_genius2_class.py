# Python program to show that we can create
#instance variables inside methods

#Class for Computer Science Student
class CSSGenius2:

    #Class Variable
    stream = 'Computer Science'

    # The init method or constructor
    def _init_(self, classCode):

        #Instance Variable
        self.classCode = classCode

    # Adds an instance variable
    def setAddress(self,address):
        self.address = address

    #Retrieves instance variable
        def getAddress(self):
            return self.address

#Driver Code
a = CSSGenius2
a.setAddress("Noida, Up)
print(a.getAddress())

    
