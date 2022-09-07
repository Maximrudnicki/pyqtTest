class Film:

    def __init__(self, name, year, duration):
        self.name = name
        self.year = year
        self.duration = duration

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_duration(self, duration):
        self.duration = duration

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_duration(self):
        return self.duration

    def __str__(self) -> str:
        return f"""
        Name - "{self.name}". Year of publishing is {self.year}. 
        Duration - {self.duration} minutes.
        
        """
