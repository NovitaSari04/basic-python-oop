# This is class
class Employee:

    # This is class attribute
    MIN_SALARY = 5000000
    SALARY_RAISE = 10

    # This is instance method
    def __init__(self, name, salary):

        # Instance attribute
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY
    
    def benefit(self):
        print(f"{self.name} menerima benefit berupa Tunjangan Makan, Komputer, dan Asuransi")
    
    # This is class method
    @classmethod
    def set_salary_raise(cls, amount):
        cls.SALARY_RAISE = amount

    # This is overloading
    def tunjangan_keluarga(self, istri=1, anak=0):
        return istri*1000000 + anak*750000000

# This is inheritance
class Sales(Employee):
    def __init__(self, name, salary, item_sold):
        Employee.__init__(self, name, salary)
        self.item_sold = item_sold
            
    def take_home_pay(self):
        return self.salary + (self.item_sold * 100000)
    
    # Overriding from method benefit() in Employee class
    def benefit(self):
        print(f"{self.name} menerima benefit berupa Tunjangan Makan, Laptop, Motor, Handphone, dan Asuransi")


print(Employee.SALARY_RAISE)

# Object 1
employee1 = Employee('Maria', 6000000)
employee1.benefit()
print(employee1.tunjangan_keluarga())
print(employee1.SALARY_RAISE)

# Object 2
employee2 = Employee('Anita', 3000000)
print(employee1.tunjangan_keluarga(1))
Employee.set_salary_raise(15)
print(employee1.SALARY_RAISE)

# Object 3
employee3 = Employee('Darmawan', 7500000)
print(employee1.tunjangan_keluarga(1,3))

# Object 4
salesPerson1 = Sales("Maya", 10000000, 4)
salesPerson1.benefit()
print(salesPerson1.take_home_pay())
