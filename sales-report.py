"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
# Could separate this program into two functions:  one to
# update the salespeople/melons sold information and one
# to print the report

salespeople = [] # don't use lists; use dictionaries!
melons_sold = []
# instead of keeping the salespeople and their melon sold tallies
# in two separate lists, can make one dictionary of salespeople
# with the key: value pairs being of each salesperson as the key
# and another nested dictionary as the value of the salesperson
# key.  Within that dictionary add the melons_sold and revenue
# generated as keys with their respective values specified.

# shouldn't hard-code the text file; if move into
# function can pass in the text as a paramater or use
# argv to specificy the text file in the shell
f = open("sales-report.txt")
# opens the file

for line in f:
    line = line.rstrip() # can combine this and the following line
    # of code into one line # entries = line.rstrip().split("|")
    entries = line.split("|")
    # Iterates through each line in the open file "f" and
    # strips the trailing white space, then generates a list
    # of words split on the "|"; list bound to entries variable
    # In each for loop, the list now is made of 3 items in this
    # order: [salesperson, melon price, melons sold]

    # Here you can unpack the list instead:
    # salesperson, revenue, melons = entries
    # then can reassign melons as an integer
    salesperson = entries[0]
    melons = int(entries[2])

    # In each loop, salesperson variable bound to the item at
    # index 0 of entries, which represents salesperson,
    # and melon variable bound to the item
    # at index 2 of entries, which represents melons sold.

    # If have dictionaries, you can:
    # create dictionary salesperson_info of salesperson
    # (salesperson_info) with their revenue and melons sold as keys
    # salespeople.setdefault(salesperson, salesperson_info) then update
    # the dictionary with revenue and tallies
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
        # Checks whether salesperson is in the salespeople list
        # if True, binds the index of salesperson in the
        # salespeople list to the position variable, then updates
        # the integer in the melons_sold list at same index as
        # salesperson.

    # Don't need this else statement if use setdefault above
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)
        # If salesperson is not in salespeople, then the
        # salesperson is added to the end of the salespeople
        # list, and melons is added to the end of the
        # melons_sold list.

# move this into another function
for i in range(len(salespeople)):
    print "%s sold %d melons" % (salespeople[i], melons_sold[i])
