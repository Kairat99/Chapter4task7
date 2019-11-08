# import re 
# txt =  "The rain in Spain"
# x = re.search("^The.*Spain$*",txt)
# print(x)

# import re


# born = "05-03-1987 "

# # Удалим комментарий из строки
# dob = re.sub(r'#.*$', "", born)
# print("Дата рождения:", dob)

# # Заменим дефисы на точки
# f_dob = re.sub(r'-', ".", born)    
# print(f_dob)


class Students:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        
    def read(self):
          
        print(
            f"name: {self.name}, age: {self.age}, major: {self.major}"
            )
        
Steve = Students("Sutanbekov Kairat", "20", "PY")
Steve.read()

    
    