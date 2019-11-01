import random

def initFloatVariable(message):
    x = 0;
    while x == 0:
        try:
            x = float(input(message))
        except:
            x = 0
    return x

def initIntVariable(message):
    x = 0;
    while x == 0:
        try:
            x = int(input(message))
        except:
            x = 0
    return x

def main():
    currency = "RON"
    showPayments = input('Show payments? (Y/n) ')
    while showPayments != 'Y' and showPayments != 'n':
        showPayments = input('Show payments? (Y/n) ')

    deposit = 1 - 0
    loan = initFloatVariable('Loan amount? ')
    loan = loan * deposit
    loanAux = loan;

    t = initIntVariable('No. of payments? ')
    k = numberOfPayments = int(t)

    rate = initFloatVariable('Annual Interest? (%) ')

    r = rate/100
    interest = r/12
    
    if (showPayments == 'Y'):
        print('Luna XXX | SOLD | RATA | DOBANDA | CAPITAL | DAE \n')

    for i in range(0, numberOfPayments):
        rate = loan * (interest * (1 + interest) ** k) / ((1 + interest) ** k - 1)
        compound = loanAux * interest
        loanAux = abs(loanAux - (rate - compound))
        x = "Luna %.3d | %.2f | %.2f | %.2f | %.2f | %.2f" % (i + 1, loanAux, rate, compound, rate - compound, r*100) + '%'
        
        if (showPayments == 'Y'):
            print(x)

    monthlyPayments = loan * (interest * (1 + interest) ** numberOfPayments) / ((1 + interest) ** numberOfPayments - 1)
    japcaTotala = monthlyPayments*numberOfPayments - loan

    print("\n")
    print("Montly Payment: \n %s %.2f" % (currency, monthlyPayments))
    print("Total Paid: \n %s %.2f = %s %.2f + %s %.2f" % (currency, loan + japcaTotala, currency, loan, currency, japcaTotala))

    return input('Exit? (Y/n) ');

if __name__ == "__main__":
    exitVar = 'n';
    while exitVar == 'n':
        exitVar = main();
    exit
