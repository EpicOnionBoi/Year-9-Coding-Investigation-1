def compound_numbers():
    principal = float(input("Principal amount (in dollars): "))
    rate = float(input("Interest rate (in percent): "))
    time = input("Time unit for interest (year, quarter, month, week, day): ")
    compoundrate = input("Time unit for compounding (year, quarter, month, week, day, custom): ")
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
print("SIMPLE INTEREST SAVINGS ACCOUNT\n")
simpleaccount = simple_numbers()
print("COMPOUND INTEREST SAVINGS ACCOUNT\n")
compoundaccount = compound_numbers()
future = projection()
simpleinterestearned = simple_calculations(simpleaccount, future) - simpleaccount["principal"]
compoundinterestearned = compound_calculations(compoundaccount, future) - compoundaccount["principal"]
print("In a simple interest account, with the data you entered, you would end up with", "$" + str(simple_calculations(simpleaccount, future))+".", "The total interest earned is", "$" + simpleinterestearned)
print("In a compound interest account, with the data you entered, you would end up with", "$" + str(compound_calculations(compoundaccount, future))".", "The total interest earned is", "$" + compoundinterestearned)