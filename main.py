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
    return total

global time_units
time_units = {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}
print("SIMPLE INTEREST SAVINGS ACCOUNT\n")
simpleaccount = simple_numbers()
compoundaccount = compound_numbers()
future = projection()
print(simple_calculations(simpleaccount, future))