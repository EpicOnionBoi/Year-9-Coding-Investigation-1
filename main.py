from tabulate import tabulate # imports tabulate to print tables
def compound_numbers(module): # creates a function
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
            return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate, "deposit amount":depositamount, "target amount":targetamount}
    else: # otherwise
        return {"principal":principal, "rate":rate, "time":time, "compound rate":compoundrate} # returns all the data

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
    if compoundaccount["compound rate"] in time_units:
        N = time_units[compoundaccount["compound rate"]]
    else:
        N = compoundaccount["compound rate"]
    T = future["projection time"]/time_units[future["projection unit"]]
    total = P*(1+(R/N))**(N*T)
    return round(total, 2)

def calculations235(currentamount, interestpercompound):
    interest = currentamount*interestpercompound
    currentamount += interest
    return currentamount

global time_units
time_units = {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}

print("WELCOME TO INTEREST CALCULATIONS AND STUFF\n\nTHIS PROGRAM HAS 5 MODULES\n\nMODULE 1: COMPARING SIMPLE AND COMPOUND INTEREST ACCOUNTS\nMODULE 2: HOW LONG IT WILL TAKE FOR A CI ACCOUNT TO REACH A TARGET\nMODULE 3: COMPARE 2 CI ACCOUNTS\nMODULE 4: MODEL A CI SAVINGS ACCOUNT WITH REGULAR DEPOSITS\nMODULE 5: A SIMULATION THAT COMPARES DIFFERENT COMPOUND RATES")
module = input("\nENTER NUMBERS 1-5, OR ANYTHING ELSE TO EXIT: ")
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
elif module == "2":
    compoundaccount = compound_numbers(module)
    currentamount = compoundaccount["principal"]
    periods = 0
    if compoundaccount["compound rate"] in time_units:
        interestpercompound = (compoundaccount["rate"]/(time_units[compoundaccount["compound rate"]]/time_units[compoundaccount["time"]]))/100
    else:
        interestpercompound = (compoundaccount["rate"]/(compoundaccount["compound rate"]/time_units[compoundaccount["time"]]))/100
    progression = []
    while currentamount < compoundaccount["target amount"]:
        periods += 1
        currentamount = calculations235(currentamount, interestpercompound)
        progression.append(round(currentamount, 2))
    print(f"\nHere is a list of the progression of the money until the garget was reached: {progression}\n")
    print(f"A total of {periods} compounds is needed to reach the target")
elif module == "3":
    print("\nCOMPOUND ACCOUNT 1:\n")
    account1 = compound_numbers(module)
    future1 = projection()
    print("\nCOMPOUND ACCOUNT 2:\n")
    account2 = compound_numbers(module)
    future2 = projection()
    if account1["compound rate"] in time_units:
        compoundrate1 = time_units[account1["compound rate"]]
    else:
        compoundrate1 = account1["compound rate"]
    interestpercompound1 = (account1["rate"]/(compoundrate1/time_units[account1["time"]]))/100
    currentamount1 = account1["principal"]
    progression1 = []
    for e in range(int((compoundrate1)*future1["projection time"])):
        currentamount1 = calculations235(currentamount1, interestpercompound1)
        progression1.append(round(currentamount1, 2))
    if account2["compound rate"] in time_units:
        compoundrate2 = time_units[account2["compound rate"]]
    else:
        compoundrate2 = account2["compound rate"]
    interestpercompound2 = (account2["rate"]/(compoundrate2/time_units[account2["time"]]))/100
    currentamount2 = account2["principal"]
    progression2 = []     
    for e in range(int((compoundrate2)*future2["projection time"])):
        currentamount2 = calculations235(currentamount2, interestpercompound2)
        progression2.append(round(currentamount2, 2))
    print(f"\nIn the first account, the progression throughout the projection is {progression1}\n\nThe total amount at the end is {progression1[-1]}\n\nIn the second account, the progression throughout the projection is {progression2}\n\nThe total amount at the end is {progression2[-1]}")
elif module == "4":
    account = compound_numbers(module)
    principals = []
    interests = []
    deposits = []
    finals = []
    currentamount = account["principal"]
    if account["compound rate"] in time_units:
        compoundrate = time_units[account["compound rate"]]
    else:
        compoundrate = account["compound rate"]
    interestpercompound = (account["rate"]/(compoundrate/time_units[account["time"]]))/100
    depositamount = account["deposit amount"]
    if account["target amount"] == 0:
        for e in range(int((compoundrate)*account["into future"])):
            principals.append(round(currentamount, 2))
            interest = currentamount * interestpercompound
            currentamount += interest + depositamount
            deposits.append(depositamount)
            finals.append(round(currentamount, 2))
            interests.append(round(interest, 2))
    else:
        while currentamount < account["target amount"]:
            principals.append(round(currentamount, 2))
            interest = currentamount * interestpercompound
            currentamount += interest + depositamount
            deposits.append(depositamount)
            finals.append(round(currentamount, 2))
            interests.append(round(interest, 2))
    data = principals, interests, deposits, finals
    data = list(map(list, zip(*data)))
    header = ["Principal", "Interest", "Deposit", "Final"]
    print("Here is a table of the progression of your money over time\n\n")
    print(tabulate(data, tablefmt="grid", headers=header))
elif module == "5":
    quarterly = {"principal":1000, "rate":100, "time":"year", "compound rate":"quarter", "projection unit":"year", "projection time":1}
    weekly = {"principal":1000, "rate":100, "time":"year", "compound rate":"week", "projection unit":"year", "projection time":1}
    daily = {"principal":1000, "rate":100, "time":"year", "compound rate":"day", "projection unit":"year", "projection time":1}
    hourly = {"principal":1000, "rate":100, "time":"year", "compound rate":8760, "projection unit":"year", "projection time":1}
    tenminutely = {"principal":1000, "rate":100, "time":"year", "compound rate":52704, "projection unit":"year", "projection time":1}
else:
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
    """)