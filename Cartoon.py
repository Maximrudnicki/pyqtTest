from Film import Film


class Cartoon(Film):
    def __init__(self, name, year, duration, producer):
        super().__init__(name, year, duration)
        self.producer = producer

    def get_producer(self):
        return self.producer

    def set_producer(self, producer):
        self.producer = producer

    def copy(self):
        cartoon = [self.get_name(), self.get_year(), self.get_duration(), self.get_producer()]
        return cartoon

    def __str__(self) -> str:
        return f"""
        Name - "{self.name}". Year of publishing is {self.year}. 
        Duration - {self.duration} minutes.
        Producer - {self.producer}.
        """
