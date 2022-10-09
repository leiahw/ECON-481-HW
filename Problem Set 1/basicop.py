bill_acct = int(input('Bills starting account value: '))
ir = float(input('interest rate: '))
years = 10
n = 1
tot_wealth = bill_acct*((1+ir/n)**(years*n))
tot_wealth_r = round(tot_wealth, 2)
final_tot_wealth = format(tot_wealth_r, ",")
print("Bill's total wealth is $" + str(final_tot_wealth))
