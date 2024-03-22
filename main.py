from tabulate import tabulate # imports tabulate to print tables
def compound_numbers(module): # creates a function for gathering data for compound interest
    principal = float(input("Principal amount (in dollars): ")) # asks for the principal amount
    rate = float(input("Interest rate (in percent): ")) # asks for the interest rate in %
    time = input("Time unit for interest (year, quarter, month, week, day): ") # asks for the time unit for interest
    compoundrate = input("Time unit for compounding (year, quarter, month, week, day, custom): ") # asks for the time unit for compounding
    if compoundrate == "custom": # if the user requests a compound rate
        compoundrate = float(input("Enter number of compoundings per year: ")) # the compound rate will be a number
    if module == "2": # if the user is doing module 2
        targetamount = float(input("Target amount (in dollars): ")) # asks for target amount
        return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate, "target amount":targetamount} # returns all the data
    elif module == "4": # if the user is doing module 4
        depositamount = float(input("Enter the regular deposit amount per compounding period ($): ")) # asks for deposit amount
        targetamount = float(input("Enter the dollar amount to project to (if you enter 0, you will be asked for the amount of time to project for): ")) # asks for target, or if they want to do a time frame instead
        if targetamount == 0: # if they want to project to a timeframe
            intofuture = float(input("In that case, enter the amount of time to project for: ")) # asks for amount of time to project for
            intofutureunit = input("Enter the projection time unit (year, quarter, month, week, day): ") # asks for the unit
            return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate, "deposit amount":depositamount, "target amount":targetamount, "into future":intofuture, "into future unit":intofutureunit} # returns all the data
        else:
            return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate, "deposit amount":depositamount, "target amount":targetamount} # returns all the data
    else: # otherwise
        return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate} # returns all the data

def simple_numbers(): # creates a function for gathering data for simple interest
    principal = float(input("Principal amount (in dollars): ")) # asks for the principal
    rate = float(input("Interest rate (in percent): ")) # asks for the interest rate in %
    time = input("Time unit for interest (year, quarter, month, week, day): ") # asks for the interest unit
    return {"principal":principal, "rate":rate, "time":time} # returns all the data

def projection(): # creates a function for projections
    projectionunit = input("What unit is used to project into the future (year, quarter, month, week, day): ") # asks for the projection unit
    projectiontime = float(input(f"Enter the amount of {projectionunit}s to project into the future: ")) # asks for the projection time
    return {"projection unit":projectionunit, "projection time":projectiontime} # returns all the data

def simple_calculations(simpleaccount, future): # creates a function for simple interest calculation
    interestrate = (simpleaccount["rate"]*time_units[simpleaccount["time"]])/100 # multiplies the interest rate (in %) by the number corresponding to the unit and then divides by 100 to get the interest rate per year in a decimal 
    interest = simpleaccount["principal"]*interestrate*(future["projection time"]/time_units[future["projection unit"]]) # calculates the total interest by multiplying the principal by the interest rate per year and then mutiplying that with the amount of time to project converted to years
    total = simpleaccount["principal"]+interest # calculates total by adding principal and interest
    return round(total, 2) # returns the total

def compound_calculations(compoundaccount,future): # creates a function for compound interest calculation
    yearlyinterestrate = (compoundaccount["rate"]*time_units[compoundaccount["time"]])/100 # calculates the yearly interest rate as a decimal by multiplying the interest rate and the corresponding number to the interest unit
    P = compoundaccount["principal"] # defines P as the principal
    R = yearlyinterestrate # defines R as the yearly interest rate
    if compoundaccount["compound rate"] in time_units: # if it is not a custom compound rate
        N = time_units[compoundaccount["compound rate"]] # the number of compounds per year is defined as the corresponding number in the time units dictionary to the compound unit
    else: # if it is a custom compound rate
        N = compoundaccount["compound rate"] # N is equals to the number the user inputted in the first function
    T = future["projection time"]/time_units[future["projection unit"]] # T is defined as the projection time converted to years by using the time units dictionary
    total = P*(1+(R/N))**(N*T) # calculates the total using the compound interest formula
    return round(total, 2) # returns the total

def calculations235(currentamount, interestpercompound): # creates a function for calculations in modules 2, 3 and 5 which will run in a loop
    interest = currentamount*interestpercompound # the interest in this compound (loop) is the current amount multiplied by the interest per compound (which will be calculated prior)
    currentamount += interest # adds the interest to the current amount
    return currentamount # returns the current amount

def loopington(account): # creates a loop function to be used in part 5
    if account["compound rate"] in time_units: # if the compound rate is not a custom compound rate
        compoundrate = time_units[account["compound rate"]] # sets the compound rate to the number of compounds per year
    else: # if the compound rate is custom
        compoundrate = account["compound rate"] # compound rate remains as a number
    currentamount = account["principal"] # the current amount is the principal
    interestpercompound = (account["rate"]/compoundrate)/100 # calculates the interest per compound
    for e in range(int(compoundrate)): # runs the loop until the timeframe ends
        currentamount = calculations235(currentamount, interestpercompound) # does the calculations required with a funcion
    return currentamount # returns the ending amount

global time_units # mades time units a global variable
time_units = {"year" : 1, "quarter" : 4, "month" : 12, "week" : 52, "day" : 365} # the dictionary used to convert a lot of data into per year format
loop = True # creates a true variable
while loop ==True: # while the variable above is true, the code will continue to run
    print("\nWELCOME TO INTEREST CALCULATIONS AND STUFF\n\nTHIS PROGRAM HAS 5 MODULES\n\nMODULE 1: COMPARING SIMPLE AND COMPOUND INTEREST ACCOUNTS\nMODULE 2: HOW LONG IT WILL TAKE FOR A CI ACCOUNT TO REACH A TARGET\nMODULE 3: COMPARE 2 CI ACCOUNTS\nMODULE 4: MODEL A CI SAVINGS ACCOUNT WITH REGULAR DEPOSITS\nMODULE 5: A SIMULATION THAT COMPARES DIFFERENT COMPOUND RATES") # homepage
    module = input("\nENTER NUMBERS 1-5, OR ANYTHING ELSE TO EXIT: ") # asks for which module the user wants
    if module == "1": # if the user wants module 1
        print("\nSIMPLE INTEREST SAVINGS ACCOUNT\n") # prints a heading
        simpleaccount = simple_numbers() # calls the function to gather data
        print("\nCOMPOUND INTEREST SAVINGS ACCOUNT\n") # prints a heading
        compoundaccount = compound_numbers(module) # calls the function to gather data
        print("\nPROJECTION INTO FUTURE\n") # prints a heading
        future = projection() # calls the function to get projection data
        simpleinterestearned = round(simple_calculations(simpleaccount, future) - simpleaccount["principal"], 2) # calculates the interest earned for the simple interest account
        compoundinterestearned = round(compound_calculations(compoundaccount, future) - compoundaccount["principal"], 2) # calculates the interest earned for the compound account
        print(f"\nThe SI account has a principal of ${simpleaccount['principal']}, and an interest rate of {simpleaccount['rate']}% per {simpleaccount['time']}\n\nThe CI account has a principal of ${compoundaccount['principal']} and an interest rate of {compoundaccount['rate']}% per {compoundaccount['time']}. The compound frequency is {compoundaccount['compound rate']}\n\nThe projected time frame is {future['projection time']} {future['projection unit']}s") # summarises data
        print(f"\nIn a simple intereset account, with the data you entered, you would end up with ${simple_calculations(simpleaccount, future)}. The total interest earned is $ {simpleinterestearned}.") # prints the data for simple interest account
        print(f"In a compound interest account, with the data you entered, you would end up with ${compound_calculations(compoundaccount, future)}. The total interest earned is ${compoundinterestearned}.") # prints the data for ccompound interest account
    elif module == "2": # if the user wants module 2
        compoundaccount = compound_numbers(module) # calls the function to gather data
        currentamount = compoundaccount["principal"] # defines the current amount as the principal
        periods = 0 # defines the number of compounds so far as 0
        if compoundaccount["compound rate"] in time_units: # if the user does not want a custom compound rate
            interestpercompound = (compoundaccount["rate"]/(time_units[compoundaccount["compound rate"]]/time_units[compoundaccount["time"]]))/100 # calculates the interest per compound
        else: # if the user wants  a custom compound rate
            interestpercompound = (compoundaccount["rate"]/(compoundaccount["compound rate"]/time_units[compoundaccount["time"]]))/100 # calculates interest per compound
        progression = [] # creates an empty list to put progressions in
        while currentamount < compoundaccount["target amount"]: # while the current amount is less than the target amount
            periods += 1 # adds one to the number of compounds
            currentamount = calculations235(currentamount, interestpercompound) # calls the function to do the calculations
            progression.append(round(currentamount, 2)) # adds the current amount to a list
        print(f"\nThe account has a principal of ${compoundaccount['principal']} and an interest rate of {compoundaccount['rate']}% per {compoundaccount['time']}. The compound frequency is {compoundaccount['compound rate']}\n\nThe target amount is ${compoundaccount['target amount']}") # summarises data
        print(f"\nHere is a list of the progression of the money until the target was reached: {progression}\n") # prints the list with the progressions in it
        print(f"A total of {periods} compounds are needed to reach the target") # prints the number of compounds needed to reach the target
    elif module == "3": # if the user wants module 3
        print("\nCOMPOUND ACCOUNT 1:\n") # prints heading
        account1 = compound_numbers(module) # gathers data for first account
        future1 = projection() # gathers projection data for first account
        print("\nCOMPOUND ACCOUNT 2:\n") # prints heading
        account2 = compound_numbers(module) # gathers data for second account
        future2 = projection() # gathers projection data for second account
        if account1["compound rate"] in time_units: # if it is not a custom compound rate
            compoundrate1 = time_units[account1["compound rate"]] # converts compound rate to the number of compounds per year
        else: # if it is a custom compound rate
            compoundrate1 = account1["compound rate"] # the compound rate is the same (a number)
        interestpercompound1 = (account1["rate"]/(compoundrate1/time_units[account1["time"]]))/100 # calculates the interest in each compound
        currentamount1 = account1["principal"] # the current amount is the principal
        progression1 = [] # empty list for progression
        for e in range(int((compoundrate1)*future1["projection time"])): # loop to do calculations for set amount of time
            currentamount1 = calculations235(currentamount1, interestpercompound1) # calls the function to do the calculations
            progression1.append(round(currentamount1, 2)) # adds the current amount to the empty list
        if account2["compound rate"] in time_units: # from this line to line 127 is the same as above, but for the second account
            compoundrate2 = time_units[account2["compound rate"]]
        else:
            compoundrate2 = account2["compound rate"]
        interestpercompound2 = (account2["rate"]/(compoundrate2/time_units[account2["time"]]))/100
        currentamount2 = account2["principal"]
        progression2 = []     
        for e in range(int((compoundrate2)*future2["projection time"])):
            currentamount2 = calculations235(currentamount2, interestpercompound2)
            progression2.append(round(currentamount2, 2))
        print(f"\nIn the first account, the progression throughout the projection is {progression1}\n\nThe total amount at the end is {progression1[-1]}\n\nIn the second account, the progression throughout the projection is {progression2}\n\nThe total amount at the end is {progression2[-1]}") # outputs all the data
    elif module == "4": # if the user wants module 4
        account = compound_numbers(module) # calls function to gather information
        principals = [] # empty list for each of the new principals
        interests = [] # empty list for each of the interests
        deposits = [] # empty list for the deposits
        finals = [] # empty list for the final amounts
        currentamount = account["principal"] # the current amount is the principal
        if account["compound rate"] in time_units: # if it is not a custom compound rate
            compoundrate = time_units[account["compound rate"]] # sets the compound rate to the number of compounds per year
        else: # if it is a custom compound rate
            compoundrate = account["compound rate"] # the compound rate is the same (number)
        interestpercompound = (account["rate"]/(compoundrate/time_units[account["time"]]))/100 # calculates the interest per compound
        depositamount = account["deposit amount"] # sets the deposit amount
        if account["target amount"] == 0: # if the user wants to run until a projected time
            for e in range(int((compoundrate)*account["into future"])): # runs loop until the projected time ends
                principals.append(round(currentamount, 2)) # adds principal to list
                interest = currentamount * interestpercompound # calculates the interest
                currentamount += interest + depositamount # adds interest and deposit to current amount
                deposits.append(depositamount) # adds deposit amount to list
                finals.append(round(currentamount, 2)) # adds final amount to list
                interests.append(round(interest, 2)) # adds the interest amount list
        else: # if the user wants to run until a target is met
            while currentamount < account["target amount"]: # while the current amount is less than the target amount
                principals.append(round(currentamount, 2)) # from this line to line 157 does the same as the loop above
                interest = currentamount * interestpercompound
                currentamount += interest + depositamount
                deposits.append(depositamount)
                finals.append(round(currentamount, 2))
                interests.append(round(interest, 2))
        data = principals, interests, deposits, finals # puts the 4 lists into a variable
        data = list(map(list, zip(*data))) # uses the data in the table
        header = ["Principal", "Interest", "Deposit", "Final"] # headings for the table
        print("Here is a table of the progression of your money over time\n\n") # prints an output
        print(tabulate(data, tablefmt="grid", headers=header)) # prints the table
    elif module == "5": # if the user wants module 5
        quarterly = {"principal":1000, "rate":100, "time":"year", "compound rate":"quarter", "projection unit":"year", "projection time":1} # creates dictionary for quarterly compound
        weekly = {"principal":1000, "rate":100, "time":"year", "compound rate":"week", "projection unit":"year", "projection time":1} # creates dictionary for weekly compound
        daily = {"principal":1000, "rate":100, "time":"year", "compound rate":"day", "projection unit":"year", "projection time":1} # creates dictionary for daily compound
        hourly = {"principal":1000, "rate":100, "time":"year", "compound rate":8760, "projection unit":"year", "projection time":1} # creates dictionary for hourly compound
        tenminutely = {"principal":1000, "rate":100, "time":"year", "compound rate":52704, "projection unit":"year", "projection time":1} # creates dictionary for compounding every 10 minutes
        quarterlyamount = round(loopington(quarterly), 2) # calls the function to do calculations in a loop
        weeklyamount = round(loopington(weekly), 2) # calls the function to do calculations in a loop
        dailyamount = round(loopington(daily), 2) # calls the function to do calculations in a loop
        hourlyamount = round(loopington(hourly), 2) # calls the function to do calculations in a loop
        tenminutelyamount = round(loopington(tenminutely), 2) # calls the function to do calculations in a loop
        print(f"\nIf you compound quarterly, you would end up with ${quarterlyamount}\nIf you compound weekly, you would end up with${weeklyamount}\nIf you compound daily, you would end up with ${dailyamount}\nIf you compound hourly, you would end up with ${hourlyamount}\nIf you compound every ten minutes, you would end up with ${tenminutelyamount}") # outputs all the information
    else: # if the user wants to exit
        print("""
                                    µçççççççµ
                            µ▄æ╧╜╩ññ.  ▄▄▄æ##æ▄▓▀▄,
                        ▄#╜²         ¿ççç▄▄▄▄▄▄▄▄▄,;▀gµ
                    ▄▀²                               ▀▄
                ▄▀         ,▄æ▀╨▀▀▀æ▄,               ²▀
                ,▀         ▄▀          _▀▄          ▄▀╜ñ²▀
                ▄▀         █              "▌        █      █
            █`         ▄ææM▀╩ñññññ╙▀%▄,                 ╘▌
            ¿▀      ,▄██▌                ²▀▄,µ,    ▄#▀╨╨╨╨╨▀█æwçµ
            ▐Ö      █▓╜ ▐¿                  ▐.  a/╙▓         Ñ▄   ²%,
        ▐Ö     ▄▓▀    ▓  ▐╨▀▒▄▄çñ▀%▄    ▓▐   ²▀▓⌂,▄▄gæææµ Ñ     ▓▓█
        ▌    ▄▓▀      "█,▓▄▓▓▓▓▓▄æ#▀╙   ▌╨"       ²█▓▓▓  ▓  █    ▓▓"
        █    █▀          _²²╙╩╙╨▀▀════#█▒▄æ▀▀       ▓  ¡²²└  ╙▄  ▐▓
        ▓  J▀                         ▌    ,¿▄µ      ²▀▄²ñ╙╩╩█▌╙╙▓_
        ]M #"                          ▓   █▓▓▓▀   ▄▓██ _█     ²▌▌
        ]▄▀                            ▀ç,╘▀▀░_     ▀▀å¿▀        █
        ]&                                ²²        ╨╨▀;          ▌
        ]«                                                        Ñ
        ]«                                   µççççççµ              █
        ]«                              ▄#▀▓« ▌  ▐  ▐M▀▄           ÑΩ
        ]«                           ¿▌²Ñ, ▄██▓▓▓▓██▓▄▌╙▌           ▓
        ]«                          ▀╙▐▄█▓▓▓▓▓▓▓▓▓▓▓▓═▓g▓           ]Ω
        ]M    ,█              ▄    ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀#█▒▓           ▐
        ,█▌  ñ▒M,▄M           █    ▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌           ▌
    ²░]▄▓██▓▌_ ¿          ▐╜    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓M  ▌       █
        ▐▌█▓ñ▒▌█╩          ▐`    ]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓M  ▓     *▓█*
    æ▀ç▓▀▒▒▄▀▄█          ▌    ,█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   Ñ     ▐▓▄²
    ²ñ²_▓▓▓▓▓▀ç▄#╛       █     ]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   Ñ    ▓▓▓▌
        ,▄▓▓ ,╬&          ÑΩ    ]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌   ▓    ▓▓█╙
        ,,,▄▓▌▀█▓══         ▌     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   █    █▓▓▀*
        _µ▄▓▓▄▄▄                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓M  ]&   █▓▒_
        ¿▄█▓▓▓▓▀                  ▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌       ]▓▀▀
        "▀▀▓█▀▄▄▓▀               ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ]▓█▌
            ▐▄▓▒▄▀▄    $█M#┘       ▐▓╓▓▓▓▓▓▓▓▓▓▓▓▒▓▓_       ▐▒▓▓
        æ▀▓▓▀▓▄▄Ö╙╩▀▓▓▓▓ç▄▄æ      ╙▓█ÖÅ▓▀▓▀█▀▌▄█▀        ▐▓▓▓▀
        ¿▄Ö² ]M.▓▌▐█▄▄▓æææ▓▓`          ²▀▀▀██▓▀▀╙     g█▄ ▐▓▓██▌
    ¿#Ö    µ█#Öµ▓█▓▓ πçç█▄▒▓▓Ö`                    ▐g▓▌ j▓▐▓█▄æ
    ¿#▀_    ╙╩` #▀▓▓▀▓▓▓▓▓▓█▄]▀▒▄▄▌∩                ▀▄▓▓²▀▄▓▓▀▀▀²╙%▄
    ▄▀▀_          ╓█▓▀▀▀▀░█▓▓å▄▓²ñ)▓▓▌ ¡▄       ¿    ██Ñ▓▒▀]▓▄▓▓█µ▄   :▀▀æç
                *æææ▀▀╢▓█▓▄▄»▄▓═▀▀▓▓▄▄▓]▄µ▌▓▓▄█▌▄▓▓⌂█ ¢▓╙▀æ∞           :ñ╩╨¼æ▄µ
                    ▐█▀▓▓▓▓▓██▓M▄²░²²▓▀Q▓▄MÑM  ▓  ²▓▒▓▓▌æ
                    ² ╘╙Ñ▀▓▓%∩ ▌▌┌Ö▀▀▀╨▀.        ∞░▓▓▓▓▓▀╨
                        ═▀░█,▒██▓▓▀ ╥ ▌,  ¡,,▌█▓▓▓▒▒▒ç
                        ]æ#Ö  └▀▓▓▓▄▄▓██▄▓▄▄▓▓▓▓▓▄
                            ²▄▄▓▓▀▀█▓▒▓▀▀█▄ç Ñ
                                    ╙*    ╛
        """) # soyjak
        loop = False # turns off the loop