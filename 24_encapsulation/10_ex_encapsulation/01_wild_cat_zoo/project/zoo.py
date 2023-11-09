from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__worker_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for el in self.workers:
            if el.name == worker_name:
                self.workers.remove(el)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            left_budget = self.__budget
            return f"You payed your workers. They are happy. Budget left: {left_budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animal(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care

        if self.__budget >= needed_money:
            self.__budget -= needed_money
            left_budget = self.__budget
            return f"You tended all the animals. They are happy. Budget left: {left_budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_animal_str('Lion')
        result += self.__build_animal_str('Tiger')
        result += self.__build_animal_str('Cheetah')
        return result

    def __build_animal_str(self, animal_type):
        counter = 0
        result = ''
        for animal in self.animals:
            if animal.__class__.__name__ == animal_type:
                counter += 1
                result += repr(animal) + '\n'
        return f'----- {counter} {animal_type}s:\n'

