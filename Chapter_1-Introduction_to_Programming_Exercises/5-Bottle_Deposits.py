# In many jurisdictions a small deposit is added to drink containers to encourage 
# people to recycle them. 
# In one particular jurisdiction, drink containers holding one liter or less 
# have a $0.10 deposit, and drink containers holding more than one liter have 
# a $0.25 deposit.
# Write a program that reads the number of containers of each size from the user. 
# Your program should continue by computing and displaying the refund that will 
# be received for returning those containers. Format the output so that it includes 
# a dollar sign and always displays exactly two decimal places.


# <= 1 L == 0.10 deposit
# > 1L == 0.25 deposit

small = int(input("Inform the number of containers that holds 1 liter or less: "))
big = int(input("Inform the number of containers that holds more than one liter: "))

refund = (small * 0.10) + (big * 0.25)
print("The refund that will be received is: $ {:.2f}".format(refund))

