income = float(input("Enter the annual income: "))

#if income <= 85,528 thalers, tax is 18% of the income minus 556 thalers and 2 cents.
#if calculated tax < 0, it only means no tax at all. 
if income <= 85528:
    tax = income * (18/100) - 556.02
    if tax < 0: tax = 0.0
#if income > 85,528, tax is 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
else:
    tax = (income - 85528) * (32/100) + 14839.02 
    if tax < 0: tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
