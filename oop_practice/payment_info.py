class payslip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + "has been paid " + str(self.amount)
        else:
            return self.name + "Has not been paid yet"

jay = payslip("Joseph Akpan ", "no ", 100000)
print(jay.status())

print ('payment done')
jay.pay()
print(jay.status())




