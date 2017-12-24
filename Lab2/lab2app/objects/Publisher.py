class Publisher:
    def __init__(self, id, name, year, headquarter):
        self.id = id
        self.name = name
        self.year = year
        self.headquarter = headquarter

    def __str__(self):
        return str(self.id) + "//" + str(self.name) + "//" + str(self.year) + "//" + str(self.headquarter)
