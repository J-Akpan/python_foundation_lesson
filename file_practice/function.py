#function that wiil calculate salary per day for 1 month
def salary_cal(wages, tax_per_wages, days_worked):
    return round((wages-tax_per_wages)*days_worked, 2)
print (salary_cal(10.23,1,22))



# calculator function jus tfor fun

#calculator function
def calc():
    x = float(input("enter a number  "))
    sign = str(input("enteer and operator  "))
    y = float(input("enter a second number  "))


    # condtitions logicals
    if sign == "+":
        print(x + y)
    elif sign == "-":
        print(x-y)
    elif sign == "*":
        print(x*y)
    elif sign == "/":
        print(x/y)
    else:
        print("program is waiting for ytour input")

calc()
    