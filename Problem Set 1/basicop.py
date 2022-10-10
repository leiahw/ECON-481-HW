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
# I solve for the number of years to double Bill's money by inversing
# the compounding interest equation (years to double = log_(1+ir)(2000/1000)).
# I then used the same round() function to round the number of years to two
# places

# Question 3:
jack_acct = float(input('Jacks starting account value: '))
ir_jack = float(input('Jacks interest rate: '))
years_jack = 6
n = 1
jack_tot_wealth = jack_acct*((1+ir_jack/n)**(years*n))
if jack_tot_wealth >= 2*jack_acct:
    print("True")
else:
    print("False")
# Using the same formula as seen in Question 1 to calculate total wealth
# with compounding interest, I added an if statement to determine if Jack's
# total wealth would be doubled in 6 years and printed the boolean statement.

# Question 4:
acct_list = ["Bill", 1000, "Jack", 5000, "Amy", 6700, "Cindy", 5699, "Harry",
             6700]
print(acct_list)
# I created a list using [] symbols to indicate a list. I also put quotations
# around the names to indicate they are strings.

# Question 5:

Accounts = {}
for i in range(len(acct_list)):
    if i % 2 == 0:
        Accounts[acct_list[i]] = acct_list[i+1]
print(Accounts)
# I used a for loop and an if statement to iterate through acct_list and detect
# even and odd indexes in order to assign them as a key or value in Accounts

# Question 6:
items = Accounts.items()
print(items)
