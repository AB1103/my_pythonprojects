name = input("What is your name?:")
salary = float(input("What is your salary/:"))
bonus = float(input("What is your bonus?:"))
commission_rate = float(input("What is your commission rate {as a decimal}? "))
commission = salary*commission_rate

total_compensation =salary + bonus + commission
print(total_compensation)
