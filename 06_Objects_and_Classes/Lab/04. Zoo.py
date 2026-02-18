class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result = f"Birds in {self.name}: {', '.join(self.birds)}"
        
        return f"{result}\nTotal animals: {Zoo.__animals}"

zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for _ in range(count):
    animal_data = input().split(" ")
    species = animal_data[0]
    name = animal_data[1]
    zoo.add_animal(species, name)

info_species = input()
print(zoo.get_info(info_species))
