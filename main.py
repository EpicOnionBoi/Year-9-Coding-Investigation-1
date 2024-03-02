def compound_numbers():
    principal = float(input("Principal amount (in dollars): "))
    rate = float(input("Interest rate (in percent): "))
    time = input("Time unit for interest (year, quarter, month, week, day): ")
    compoundrate = input("Time unit for compounding (year, quarter, month, week, day, custom): ")
    return principal, rate, time, compoundrate

def simple_numbers():
    principal = float(input("Principal amount (in dollars): "))
    rate = float(input("Interest rate (in percent): "))
    time = input("Time unit for interest (year, quarter, month, week, day): ")
    return principal, rate, time

def projection():
    projectionunit = input("What unit is used to project into the future (year, quarter, month, week, day): ")
    projectiontime = float(input("Enter the amount of", projectionunit+"s", "to project into the future: "))
    return projectionunit, projectiontime