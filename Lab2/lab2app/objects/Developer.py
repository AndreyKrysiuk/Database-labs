class Developer:
    def __init__(self, id, name, year, headquarter, count_employees):
        self.id = id
        self.name = name
        self.year = year
        self.headquarter = headquarter
        self.count_employees = count_employees

    def __str__(self):
        return str(self.id) + "//" + str(self.name) + "//" + str(self.year) + "//" + str(self.headquarter) + "//" + str(self.count_employees)
