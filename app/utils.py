
def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about.
    What its responsibilities ar.
    What the params are ab9out.
    What datatypes the params are.
    What this function will return.
    Example of invoking the function.

    Invoke like this: to_usd(9.9999)
    """
    return '${:,.2f}'.format(my_price)




## if this code is in the global scope
## ... of a file we're trying to import from
## ... it will throw errors when we try to run those

#price = input("Please choose a price like 4.9999")

#print(to_usd(float(price)))





if __name__ == "__main__":

    ## if this code is in the global scope
    ## ... of a file we're trying to import from
    ## ... it will throw errors when we try to run those

    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))