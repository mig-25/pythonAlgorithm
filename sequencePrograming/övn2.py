""" 
Beräkna slutlönen, utgå att startlönen är 8000kr, 
Efter du säljer till ett värde för 100000 får du 
ett bonus på 9%.
Vad blir ditt slutlön?
"""


Salary = float(0.0)
Bonus = float(0.09)
Sales = int(100000)
StartSalary = int(8000)


def calc_salary():
    salary = (Bonus * Sales) + StartSalary
    return salary


print(f"Slutlönen är: {calc_salary()} kr")
