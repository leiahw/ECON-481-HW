import math
# Question 1:
bill_acct = int(input('Bills starting account value: '))
ir = float(input('interest rate: '))
years = 10
n = 1
tot_wealth = bill_acct*((1+ir/n)**(years*n))
tot_wealth_r = round(tot_wealth, 2)
final_tot_wealth = format(tot_wealth_r, ",")
print("Bill's total wealth is $" + str(final_tot_wealth))
# In Question 1, I used input() to enter Bill's starting account value and the
# interest rate. I used the annual compounding interest formula to use these
# inputs and the number of years to calculate Bill's total wealth after 10
# years to answer the question. I also used the round()
# function as well as format() to give the desired formatting
# of the assignment.

# Question 2:
years_to_double = math.log(2, 1 + ir)
years_to_double_rounded = round(years_to_double, 2)
print("It takes " + str(years_to_double_rounded)
      + " years to double Bill's money.")
