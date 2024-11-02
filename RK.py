'''
Хрипков Т.А. ИУ5-35Б
'''
'''
Вариант: 5
Класс 1: Музыкант
Класс 2: Оркестр
'''


"""
Вариант Д.
«Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список всех сотрудников, у которых фамилия заканчивается на «ов», и названия их отделов.
«Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список отделов со средней зарплатой сотрудников в каждом отделе, отсортированный по средней зарплате (отдельной функции вычисления среднего значения в Python нет, нужно использовать комбинацию функций вычисления суммы и количества значений).
«Отдел» и «Сотрудник» связаны соотношением многие-ко-многим. Выведите список всех отделов, у которых название начинается с буквы «А», и список работающих в них сотрудников.
"""
class Orchestra:
    def __init__(self, name):
        self.name = name
        self.musicians = []
    def mus_add(self, musician):
        if musician not in self.musicians:
            self.musicians.append(musician)
            musician.orch_add(self)
    def avrg_salary(self):
        if not self.musicians:
            return 0  
        united_salary = sum(musician.salary for musician in self.musicians)
        mus_count = len(self.musicians)
        return united_salary / mus_count
class Musician:
    def __init__(self, surname, salary):
        self.surname = surname
        self.salary = salary
        self.orchs = []
    def orch_add(self, orchestra):
        if orchestra not in self.orchs:
            self.orchs.append(orchestra)

orchestra1 = Orchestra("Академический оркестр")
orchestra2 = Orchestra("Симфонический оркестр")
orchestra3 = Orchestra("Аркестр Анатолия")
orchestra4 = Orchestra("Духовой оркестр")

musician1 = Musician("Иванов", 50000)
musician2 = Musician("Мушкарин", 180000)
musician3 = Musician("Сидоров", 40000)
musician4 = Musician("Бронникова", 100000)
musician5 = Musician("Тихонов", 60000)
musician6 = Musician("Герасимович", 130000)
musician7 = Musician("Тенишев", 130000)

orchestra1.mus_add(musician1)
orchestra1.mus_add(musician2)
orchestra2.mus_add(musician3)
orchestra3.mus_add(musician4)
orchestra3.mus_add(musician5)
orchestra1.mus_add(musician6)
orchestra4.mus_add(musician7)
def mus_endswith_ov(orchs):
    print("Все музыканты с фамилией, заканчивающейся на ов:")
    for orchestra in orchs:
        for musician in orchestra.musicians:
            if musician.surname.endswith("ов"):
                print(f'  Музыкант: {musician.surname} (Оркестр: {orchestra.name})')

def avrg_orch_salary(orchs):
    print("Средние зарплаты оркестров:")
    avrg_salaries = []
    for orchestra in orchs:
        avrg = orchestra.avrg_salary()
        avrg_salaries.append((orchestra.name, avrg))

    avrg_salaries.sort(key=lambda x: x[1], reverse=True)

    for name, avrg in avrg_salaries:
        print(f'  Оркестр: {name}, средняя зарплата: {avrg:.2f}')

def orch_startswith_A(orchs):
    print("Все аркестры, начинающиеся на А:")
    for orchestra in orchs:
        if orchestra.name.startswith("А"):
            print(f' Оркестр: {orchestra.name}')
            for musician in orchestra.musicians:
                print(f'\tМузыкант: {musician.surname}')

orchs = [orchestra1, orchestra2, orchestra3, orchestra4]


mus_endswith_ov(orchs)
print("\n")
avrg_orch_salary(orchs)
print("\n")
orch_startswith_A(orchs)
