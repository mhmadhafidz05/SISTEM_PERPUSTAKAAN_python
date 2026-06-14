from person import Person

class User(Person):
    def __init__(self, name, user_id):
        super().__init__(name)
        self.user_id = user_id

    def display_info(self):
        print(f"ID User : {self.user_id}")
        print(f"Nama    : {self.name}")