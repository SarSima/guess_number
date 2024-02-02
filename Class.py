
# dovolena = {}
# class Employee():
#     vacation_days = 28
#     def __init__(self, first_name_value, second_name_value, genger_value):
#         self.first_name = first_name_value
#         self.second_name = second_name_value
#         self.genger = genger_value
#         self.remaining_vacation_days = self.vacation_days
#         #dovolena[first_name_value] = second_name_value
#
#
#     def consume_vacation(self,vac_days: int) -> int:
#         self.remaining_vacation_days -= vac_days
#
#
#     def get_vacation_details(self) -> int:
#         return self.remaining_vacation_days
#
#
#
#
# #name = str(input('Введите имя: '))
# #s_name = str(input('Введите фамилию: '))
# #pol = str(input('Введите пол: '))
#
# #employee1 = Employee(first_name_value=str(input('Введите имя: ')), second_name_value=str(input('Введите фамилию: ')), genger_value=str(input('Введите пол: ')))
# #print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.genger},', end='')
# #print(f'Отпускных дней в году: {employee1.vacation_days}')
# #print(dovolena)
# manager = Employee(first_name_value='Aнд', second_name_value='Sim', genger_value='m')
# #developer = Employee()
# manager.consume_vacation(5)
# print(f'Остаток отпускных дней: {manager.get_vacation_details()}.')


# class Phone:
#     line_type = 'Проводной'
#     def __init__(self,dial_type_value):
#         self.dial_type = dial_type_value
#
# rotary_phone = Phone(dial_type_value='дисковый')
# keypad_phone = Phone(dial_type_value='кнопочный')
# print(f'Тип линии: {rotary_phone.line_type}')
# print(f'Тип набора: {rotary_phone.dial_type}')
# print(f'Тип линии: {keypad_phone.line_type}')
# print(f'Тип набора: {keypad_phone.dial_type}')
#
# rotary_phone.dial_type = 'изменение значения атрибута обькта класса телефон'
# print(rotary_phone.dial_type)
# Phone.line_type = 'изменение атрибута класса'
# print(rotary_phone.line_type)
# rotary_phone.line_type = 'тест'
# print(rotary_phone.line_type)
# print(keypad_phone.line_type)


# class Phone:
#
#     line_type = 'проводной'
#
#     def __init__(self, dial_type_value):
#         self.dial_type = dial_type_value
#
#     def ring(self):
#         print('Дзззззыыыыыыыынь!')
#
#     # Это новый метод, уже с двумя параметрами.
#     def call(self, phone_number):
#         # Сначала в вывод подставляется значение параметра phone_number,
#         # а затем - атрибута класса Phone.
#         print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')
#
#
# rotary_phone = Phone(dial_type_value='дисковый')
#
# # Вызов метода call(). Передаётся аргумент '555-2368'
# # для параметра phone_number.
# rotary_phone.call('555-2368')
#
# # Выведется:
# # Звоню по номеру 555-2368! Тип связи - проводной.


class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    # Сюда добавьте методы consume_vacation и get_vacation_details.
    def consume_vacation(self, vac_days: int) -> int:
        self.remaining_vacation_days -= vac_days

    def get_vacation_details(self) -> int:
        return self.remaining_vacation_days

class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self,start_data: str, days: int) -> str:
        return f'Начало неоплачиваемого отпуска: {start_data}, продолжительность: {days} дней.'

class PartTimeEmployee(Employee):
    vacation_days = 14



    # Пример использования класса:

full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())

#employee = Employee('Роберт', 'Крузо', 'м')
#print(employee.vacation_days)
#print(employee.get_vacation_details())


class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee.
class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self,start_data: str, days: int) -> str:
        return f'Начало неоплачиваемого отпуска: {start_data}, продолжительность: {days} дней.'
class PartTimeEmployee(Employee):
    vacation_days = 14
    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days

# Пример использования:
#full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
#print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
#part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
#print(part_time_employee.get_vacation_details())


# class Phone:
#
#     line_type = 'проводной'
#
#     def __init__(self, dial_type_value):
#         self.dial_type = dial_type_value
#
#     def ring(self):
#         print('Дзззззыыыыыыыынь!')
#
#     def call(self, phone_number):
#         print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')
#
#     def dial_type_upgrade(self, new_dial_type):
#         self.dial_type = new_dial_type
#     def __str__(self):
#         return f'Это {self.line_type} телефон. Набор - {self.dial_type}.'
#
# rotary_phone = Phone(dial_type_value='дисковый')
#
# print(rotary_phone)


