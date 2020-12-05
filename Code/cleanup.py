# function to convert value in pandas object to int
def money_to_int(val):
    val1 = val.replace("$", "")
    val2 = val1.replace(",", "")
    return int(val2)