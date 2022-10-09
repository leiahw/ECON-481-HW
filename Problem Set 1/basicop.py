bill_acct = int(input('Bills starting account value: '))
ir = float(input('interest rate: '))
years = 10
n = 1
tot_wealth = bill_acct*((1+ir/n)**(years*n))
print("Bill's total wealth is $" + str(tot_wealth))
