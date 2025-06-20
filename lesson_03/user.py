class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayfirst_name(self):
        print("Меня зовут: ", self.first_name)

    def saylast_name(self):
        print("Моя фамилия: ", self.last_name)

    def sayfull_name(self):
        print(f"Мое полное имя: {self.first_name} {self.last_name}")
