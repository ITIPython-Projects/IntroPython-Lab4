import re
#class Person
class Person:
    healthRate = 100
    __moods = ("happy","tired","lazy")
    mood = __moods[0]
    def __init__(self, name, money):
        self.name = name
        self.money = money
    # mood Setter Getter
    @property
    def Mood(self):
        return self.mood

    @mood.setter
    def Mood(self, mood):
        if mood in Person.__moods:
            self.mood = mood
        else:
            raise SyntaxError("Mood Must be (happy,tired,or lazy)")

    # HealthRate Setter Getter
    @property
    def healthRate(self):
        return self.healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        if 0 <= healthRate < 101:
            self.healthRate = healthRate
        else:
            raise ValueError("healthRate must be between 0 and 100")
    def sleep(self, hours):
        if hours == 7:
            self.mood = Person.__moods[0]
        elif hours > 7:
            self.mood = Person.__moods[1]
        else:
            self.mood = Person.__moods[2]
    def eat(self, meals):
        mealsNum = len(meals)
        if mealsNum == 3:
            self.healthRate = 100
        elif mealsNum == 2:
            self.healthRate = 75
        elif mealsNum == 1:
            self.healthRate = 50

    def buy(self, items):
        price = len(items) * 10
        self.money -= price


#class Employee
class Employee(Person):
    employeeEmails = []
    def __init__(self, id,name,money, car,salary, email, distanceToWork):
        super().__init__(name, money)
        self.id = id
        self.car = car
        self.distanceToWork = distanceToWork
        self.workMood = Person.mood
        Employee.employeeEmails.append(email)
        #Email And Salary Set By Condetion
        self.Email = email
        self.Salary = salary

# Salary Setter Getter
    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self, salary):
        if (salary >= 1000):
            self.__salary = salary
        else:
            print("salary Must be > 1000")
# Email Setter Getter
    @property
    def Email(self):
        return self.__email
    @Email.setter
    def Email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        match = re.match(regex, email)
        if (match != None):
            self.__email = match.string
        else:
            print('email Not Valid')

    #Methods
    def work(self, hours):
        if hours == 8:
            self.workMood = Person.__moods[0]
        elif hours > 8:
            self.workMood = Person.__moods[1]
        else:
            self.workMood = Person.__moods[2]
    @classmethod
    def send_All_mail(cls):
        for email in cls.employeeEmails:
            print(f"email sent successfully to{email}")

    def send_mail(self, to, subject, msg, receiver_name):
        email_tamplate = open(f"{receiver_name}_{subject}.txt", "w")
        email_tamplate.write(f"From: {self.Email}\n")
        email_tamplate.write(f"To: {to}\n")
        email_tamplate.write("\n")
        email_tamplate.write(f"Hi,{receiver_name}\n")
        email_tamplate.write(f"this is your Massage: {msg}\n")
        email_tamplate.close()
    def drive(self, distance):
        self.car.run(self.car.velocity, distance)
    def refuel(self, gasAmount=100):
        self.car.fuelRate = gasAmount

#class Office
class Office:
    employeesNum=0
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        Office.employeesNum+=1
    def get_all_employees(self):
        return self.employees
    def get_employee(self, empId):
        for employee in self.employees:
            if (employee.id == empId):
                return employee
    def hire(self, newEmployee):
        self.employees.append(newEmployee)
    def fire(self, empId):
        for employee in self.employees:
            if (employee.id == empId):
                self.employees.remove(employee)
                break
    def deduct(self, empId, deduction):
        for employee in self.employees:
            if (employee.id == empId):
                employee.Salary -= deduction
                break
    def reward(self, empId, reward):
        for employee in self.employees:
            if (employee.id == empId):
                employee.Salary += reward
                break

    @staticmethod
    def __Check_lateness(targetHour, moveHour, distance, velocity):
        timeToArrive=distance/velocity
        return  (moveHour+timeToArrive)-targetHour
    def calculate_lateness(self, empId, moveHour):
        for employee in self.employees:
            if (employee.id == empId):
                result=Office.__Check_lateness(self.targetHour, moveHour, employee.distance,employee.car.velocity)
                if(result<0):
                   self.deduct(empId,10)
                else:self.reward(empId,10)
                break
    @classmethod
    def change_emps_num(cls, num):
        if 0 <= num:
            cls.employeesNum = num
        else:
            raise ValueError(f"Num Must be > 0")
#class Car
class Car:
    __fuelRate = 100
    __velocity = 0
    def __init__(self, name, velocity):
        self.name = name
        self.Velocity = velocity

    #Velocity Setter and Getter
    @property
    def Velocity(self):
        return self.__velocity
    @Velocity.setter
    def Velocity(self, velocity):
        if (velocity > 0 and velocity < 201):
            self.__velocity = velocity
            return True
        else:
            raise ValueError("Velocity Must be Bettwen 0 and 200")
    #FuelRate Setter and Getter
    @property
    def FuelRate(self):
        return self.__fuelRate

    @FuelRate.setter
    def FuelRate(self, fuelRate):
        if (fuelRate > 0 and fuelRate < 101):
            self.__fuelRate = fuelRate
            return True
        else:
            print("fuel Out Of Range Must be >= 0 and  <= 100")
            return False
    def run(self, velocity, distance):
        self.Velocity = velocity
        fuelrate = self.FuelRate-(distance / self.Velocity)
        if(self.FuelRate(fuelrate)):
            self.stop(0)
        else:
            self.stop(distance)
    def stop(self, distance):
        self.Velocity = 0
        if distance > 0:
            print(f"the {self.FuelRate} Not Enough for distance {distance}")
        else:
            print(f"Car has arrived with {self.FuelRate} Fual")