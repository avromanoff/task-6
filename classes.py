class JoePets:
    def __init__(self, owner = 'Joe', hunger = 'голодный', weigth = 0):
        self.owner = owner
        self.hunger = hunger
        self.weigth = weigth
    def feed(self):
        self.hunger = 'сытый'

class Birds(JoePets):
    eggs = 0
    def eggs_gathering(self):
        self.eggs += 1

class Goose(Birds):
    voice = 'gagaga'

class Chicken(Birds):
    voice = 'kokoko'

class Duck(Birds):
    voice = 'Кря-кря-кря!'

class Milk(JoePets):
    # Класс животных, которых нужно доить
    milk_out = 0
    def milking (self):
        self.milk_out += 5
#
class Cow(Milk):
    voice = 'Муууууу'

class Nanny(Milk):
    voice = 'Меееееее'

class Wool(JoePets):
    voice = 'Беееееее'
    pet_wool = 'лохматый'
    def clep_sheep (self):
        self.clep_sheep = 'стриженый'

# Представители классов
all_joe_pets = []
# Список понадобится для циклов в 3 задании
goose0 = Goose()
goose0.name = 'Серый'
goose0.weigth = 10
all_joe_pets.append({'pet_name': goose0.name, 'pet_weigth': goose0.weigth})

goose1 = Goose()
goose1.name = 'Белый'
goose1.weigth = 9
all_joe_pets.append({'pet_name': goose1.name, 'pet_weigth': goose1.weigth})

chicken0 = Chicken()
chicken0.name = 'Ко-Ко'
chicken0.weigth = 2
all_joe_pets.append({'pet_name': chicken0.name, 'pet_weigth': chicken0.weigth})

duck0 = Duck()
duck0.name = 'Кряква'
duck0.weigth = 3
all_joe_pets.append({'pet_name': duck0.name, 'pet_weigth': duck0.weigth})

cow0 = Cow()
cow0.name = 'Манька'
cow0.weigth = 500
all_joe_pets.append({'pet_name': cow0.name, 'pet_weigth': cow0.weigth})

nanny0 = Nanny()
nanny0.name = 'Рога'
nanny0.weigth = 30
all_joe_pets.append({'pet_name': nanny0.name, 'pet_weigth': nanny0.weigth})

sheep0 = Wool()
sheep0.name = 'Барашек'
sheep0.weigth = 32
all_joe_pets.append({'pet_name': sheep0.name, 'pet_weigth': sheep0.weigth})


# 3.1
total_weigth = 0
for pet in all_joe_pets:
    total_weigth += pet['pet_weigth']
print (f'Общий вес животных - {total_weigth} килограммов')

#3.2
max_weigth = 0
max_weigth_name = ''
for pet in all_joe_pets:
    if pet['pet_weigth'] > max_weigth:
        max_weigth = pet['pet_weigth']
        max_weigth_name = pet['pet_name']
print (f'Самое тяжелое животное - {max_weigth_name} ({max_weigth} кг)')

