""" 
Beräkna lönen om din start lön är 8000kr, 
Om du säljer till ett värde för 100000 får du 
ett bonus på 9%.
Vad blir ditt slutlön?
"""


Salary = float(0.0)
Bonus = float(0.09)
Sales = int(100000)
StartSalary = int(8000)


def CalcSalary():
    Salary = (Bonus * Sales) + StartSalary
    return Salary


print(f"Slutlönen är: {CalcSalary()} kr")
