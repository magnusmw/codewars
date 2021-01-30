import math

def loose_change(cents):
    pennies = 0
    nickels = 0
    dimes = 0
    quarters = 0
    if type(cents) != int and type(cents) != float:
        return 0
    elif type(cents) == float:
        cents = math.floor(cents)
    while cents > 0:
        if (cents / 1) > 4:
            if (cents / 5) >= 2:
                if (cents / 10) > 2.4:
                    quarters = quarters + math.floor((cents / 25))
                    cents = (cents - (math.floor(cents / 25) * 25))
                else:
                    dimes = dimes + math.floor((cents / 10))
                    cents = (cents - (math.floor(cents / 10) * 10))
            else:
                nickels = nickels + math.floor((cents / 5))
                cents = (cents - (math.floor(cents / 5) * 5))
        else:
            pennies = pennies + (cents / 1)
            cents = 0
    change_dict = {
        'Nickels': int(nickels),
        'Pennies': int(pennies),
        'Dimes': int(dimes),
        'Quarters': int(quarters)
    }

    return(change_dict)