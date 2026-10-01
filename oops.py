# class product:
#     def __init__(self,make,model,year,prise):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.prise=prise

#     def display_info(self):
#         print(f"car:{self.make},{self.model},{self.year},{self.prise}")

# car1=product("swift","dizire",2021,"600000")
# car1.display_info()


class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def display_info(self):
        print(f"name:{self.name},salary:{self.__salary}")

    def add_money(self,new_amount):
        self.__salary += new_amount

emp=employee("irfan",40000)
emp.display_info()

emp.add_money(20000)
emp.display_info()

# print(emp.__salary)