class Subject:
    """Subject class"""

    def __init__(self, code, name, description, ECTS):
        self.code = code
        self.name = name
        self.description = description
        self.ECTS = ECTS
    
    def getSubject(self):
        return("Nazwa przedmiotu: " + self.name + "\nKod przedmiotu: " + self.code + "\nLiczba punktów ECTS: " + self.ECTS + "\nOpis przedmiotu: " + self.description + "\n")
