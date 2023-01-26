class A:

    def display(self):

        print("Class A")

        

class B:

    def display(self):

        print("Class B")

        

class C(A, B):

    def __init__(self):

        super().__init__()

                

    def display(self):

        super().display()