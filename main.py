from tabulate import tabulate
def compound_numbers(module):
    principal = float(input("Principal amount (in dollars): "))
    rate = float(input("Interest rate (in percent): "))
    time = input("Time unit for interest (year, quarter, month, week, day): ")
    compoundrate = input("Time unit for compounding (year, quarter, month, week, day, custom): ")
    if module == "2":
        targetamount = float(input("Target amount (in dollars): "))
        return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate, "target amount":targetamount}
    elif module == "4":
        depositamount = float(input("Enter the regular deposit amount per compounding period ($): "))
        targetamount = float(input("Enter the dollar amount to project to (if you enter 0, you will be asked for the amount of time to project for): "))
        if targetamount == 0:
            intofuture = float(input("In that case, enter the amount of time to project for: "))
            intofutureunit = input("Enter the projection time unit (year, quarter, month, week, day): ")
            return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate, "deposit amount":depositamount, "target amount":targetamount, "into future":intofuture, "into future unit":intofutureunit}
        else:
            return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate, "deposit amount":depositamount, "target amount":targetamount}
    else:
        return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate}

def simple_numbers():
    principal = float(input("Principal amount (in dollars): "))
    rate = float(input("Interest rate (in percent): "))
    time = input("Time unit for interest (year, quarter, month, week, day): ")
    return {"principal":principal, "rate":rate, "time":time}

def projection():
    projectionunit = input("What unit is used to project into the future (year, quarter, month, week, day): ")
    projectiontime = float(input(f"Enter the amount of {projectionunit}s to project into the future: "))
    return {"projection unit":projectionunit, "projection time":projectiontime}

def simple_calculations(simpleaccount, future):
    interestrate = (simpleaccount["rate"]*time_units[simpleaccount["time"]])/100
    interest = simpleaccount["principal"]*interestrate*(future["projection time"]/time_units[future["projection unit"]])
    total = simpleaccount["principal"]+interest
    return round(total, 2)

def compound_calculations(compoundaccount,future):
    yearlyinterestrate = (compoundaccount["rate"]*time_units[compoundaccount["time"]])/100
    P = compoundaccount["principal"]
    R = yearlyinterestrate
    N = time_units[compoundaccount["compound rate"]]
    T = future["projection time"]/time_units[future["projection unit"]]
    total = P*(1+(R/N))**(N*T)
    return round(total, 2)

global time_units
time_units = {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}

print("WELCOME TO INTEREST CALCULATIONS AND STUFF\nTHIS PROGRAM HAS 5 MODULES\nMODULE 1: COMPARING SIMPLE AND COMPOUND INTEREST ACCOUNTS\nMODULE 2: HOW LONG IT WILL TAKE FOR A CI ACCOUNT TO REACH A TARGET\nMODULE 3: COMPARE 2 CI ACCOUNTS\nMODULE 4: MODEL A CI SAVINGS ACCOUNT WITH REGULAR DEPOSITS\nMODULE 5: MODEL INCREASES IN COMPOUNDING FREQUENCY")
module = input("ENTER NUMBERS 1-5, OR 'QUIT' TO EXIT: ")
if module == "1":
    print("SIMPLE INTEREST SAVINGS ACCOUNT\n") 
    simpleaccount = simple_numbers()
    print("COMPOUND INTEREST SAVINGS ACCOUNT\n")
    compoundaccount = compound_numbers()
    print("PROJECTION INTO FUTURE\n")
    future = projection()
    simpleinterestearned = simple_calculations(simpleaccount, future) - simpleaccount["principal"]
    compoundinterestearned = compound_calculations(compoundaccount, future) - compoundaccount["principal"]
    print(f"In a simple intereset account, with the data you entered, you would end up with ${simple_calculations(simpleaccount, future)}. The total interest earned is $ {simpleinterestearned}.")
    print(f"In a compound interest account, with the data you entered, you would end up with ${compound_calculations(compoundaccount, future)}. The total interest earned is ${compoundinterestearned}.")
if module == "2":
    compoundaccount = compound_numbers(module)
    currentamount = compoundaccount["principal"]
    periods = 0
    interestpercompound = (compoundaccount["rate"]/(time_units[compoundaccount["compound rate"]]/time_units[compoundaccount["time"]]))/100
    progression = []
    while currentamount < compoundaccount["target amount"]:
        periods += 1
        interest = currentamount*interestpercompound
        currentamount += interest
        progression.append(round(currentamount, 2))
    print(progression)
    print(periods)
if module == "3":
    print("COMPOUND ACCOUNT 1:\n")
    account1 = compound_numbers(module)
    future1 = projection()
    print("COMPOUND ACCOUNT 2:\n")
    account2 = compound_numbers(module)
    future2 = projection()
    interestpercompound1 = (account1["rate"]/(time_units[account1["compound rate"]]/time_units[account1["time"]]))/100
    currentamount1 = account1["principal"]
    progression1 = []
    for e in range(int((time_units[account1["compound rate"]])*future1["projection time"])):
        interest1 = currentamount1*interestpercompound1
        currentamount1 += interest1
        progression1.append(round(currentamount1, 2))
    interestpercompound2 = (account2["rate"]/(time_units[account2["compound rate"]]/time_units[account2["time"]]))/100
    currentamount2 = account2["principal"]
    progression2 = []     
    for e in range(int((time_units[account2["compound rate"]])*future2["projection time"])):
        interest2 = currentamount2*interestpercompound2
        currentamount2 += interest2
        progression2.append(round(currentamount2, 2))
    print(f"In the first account, the progression throughout the projection is {progression1}\nThe total amount at the end is {progression1[-1]}\nIn the second account, the progression throughout the projection is {progression2}\nThe total amount at the end is {progression2[-1]}")
if module == "4":
    account = compound_numbers(module)
    principals = []
    interests = []
    deposits = []
    finals = []
    currentamount = account["principal"]
    interestpercompound = (account["rate"]/(time_units[account["compound rate"]]/time_units[account["time"]]))/100
    depositamount = account["deposit amount"]
    if account["target amount"] == 0:
        for e in range(int((time_units[account["compound rate"]])*account["into future"])):
            principals.append(round(currentamount, 2))
            interest = currentamount * interestpercompound
            currentamount += interest + depositamount
            deposits.append(depositamount)
            finals.append(round(currentamount, 2))
            interests.append(round(interest, 2))
        data = principals, interests, deposits, finals
        data = list(map(list, zip(*data)))
        header = ["Principal", "Interest", "Deposit", "Final"]
        print(tabulate(data, tablefmt="grid", headers=header))
    else:
        while 