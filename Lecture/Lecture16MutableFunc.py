def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance        #Declare the name "balance" nonlocal at the top of the body of the function in which it is re-assigned
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount      #Re-bind balance in the first non-local frame in which it was bound previously
        return balance
    return withdraw

def make_withdraw_list(balance):
    b = [balance]       #Name bound outside of withdraw def
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount        #Element assignment changes a list
        return b[0]
    return withdraw