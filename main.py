from package.data.salary import calculate_salary
from package.data.people import get_employees
from datetime import date

cur = date.today()
print(cur)
print()

if __name__ == '__main__':
    def main_function():
        while True:
            command = input('Введите номер команды: ')
            if command == "1":
                calculate_salary()
                break
            elif command == "2":
                get_employees()
                break
            else:
                print("Введите корректный номер функции")

main_function()

