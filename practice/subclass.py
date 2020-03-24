class AddrBookEntry: 
    'address book entry class' # define class 
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print("created instance for : " + self.name)

    def updatePhone(self, newph):
        self.phone = newph
        print("Updated Phone num for : ",self.phone)

class AddrBookEntrywithEmail(AddrBookEntry):
    'update address book entry class'
    def __init__(self,nm, ph, em):
        AddrBookEntry.__init__(self,nm, ph)
        self.email = em
    def updateEmail (self, newem):
        self.email = newem
        print("Updated Email address for :", self.email)


def main():
    john = AddrBookEntrywithEmail('John Doe', '123-456','john@naver.com')
    print(john.email)



if __name__ == '__main__':
    main()
