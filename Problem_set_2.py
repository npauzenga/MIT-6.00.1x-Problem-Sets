balance = 5000
interestRate = 0.18
minimumPaymentRate = 0.02
monthlyInterestRate = interestRate / 12.0
month = 1
totalPaid = 0.0


while month <= 12:

    interestPaid = monthlyInterestRate * balance
    minimumPayment = minimumPaymentRate * balance
    principlePaid = minimumPayment - interestPaid
    balance = balance - principlePaid
    totalPaid += minimumPayment

    print "Month: ", month, ":"
    print " Minimum monthly payment: ", round(minimumPaymentRate, 2)
    print " Remaining balance: ", round(balance, 2)
    month += 1
    
print "TOTAL: "
print " Total amount paid: ", round(totalPaid, 2)
print " Remaining balance: ", round(balance, 2)
    
## monthlyPayment = 10.0
## is balance <= 0.0 on or before 12 months?
## if not, add 10.0 to monthly payment and repeat
## balance = 1200, monthly payment = 100, months = 12

##originalBalance = float(raw_input("What is your balance? "))
##balance = originalBalance
##interestRate = float(raw_input("What is the interest rate? "))
##monthlyInterestRate = interestRate / 12.0
##monthlyPayment = 10.0
##month = 0
##
##while balance > 0.0:
##    balance = balance * (1 + monthlyInterestRate) - monthlyPayment
##    month += 1
##    if month > 12:
##        monthlyPayment += 10.0
##        balance = originalBalance * (1 + monthlyInterestRate) - monthlyPayment
##        month = 1
##print "Result: "
##print "Monthly payment to pay off debt in 1 year: ", monthlyPayment
##print "Number of months needed: ", month
##print "Balance: ", round(balance, 2)

## searching for the smallest monthly payment to pay off balance within 12 mos.
## using bisection search to set the upper and lower ranges, then testing
## the mid-point to see if it will pay off the debt. If we're paying too much
## set the monthly_payment to be the high_payment, otherwise set it to
## the low_payment

## Retrieve user input
#original_balance = float(raw_input("Enter the balance on your CC: "))
#interest_rate = float(raw_input("Enter the annual CC interest rate: "))
#
## Initialize state variables
#
#balance = original_balance
#low_payment = balance / 12
#high_payment = (balance*(1+(interest_rate/12))**12)/12
#
## Use bisection search until the search space is sufficiently small
#
#while True:
#    balance = original_balance
#    monthly_payment = (low_payment + high_payment)/2
#    
#    # Simulate passage of time until outstanding balance is paid
#    # Each iteration represents 1 month
#
#    for month in range(1,13):
#        balance = balance * (1 + interest_rate /12) - monthly_payment
#        if balance <= 0:
#            break
#    # check if the search space is sufficiently small
#    if(high_payment - low_payment < 0.005):
#        print "Result: "
#
#        monthly_payment = round(monthly_payment + 0.004999, 2)
#        print "Monthly payment to pay off debt in 1 year: ", monthly_payment
#        print "Month as determined by first for loop: ", month
#        print "Balance as determined by first for loop: ", balance
#
#    # once we've figured out the monthly payment, run the for loop again
#    # with that figure, to determine the balance
#        balance = original_balance
#        for month in range(1, 13):
#            balance = balance * (1 + interest_rate/12) - monthly_payment
#            if balance <= 0:
#                break
#        print "Balance: ", round(balance, 2)
#        break
#    # if we're paying too much, set high_payment to monthly_payment
#    elif balance < 0:
#        high_payment = monthly_payment
#    else:
#        low_payment = monthly_payment
#        
#        
#
#
#
#
#
#
