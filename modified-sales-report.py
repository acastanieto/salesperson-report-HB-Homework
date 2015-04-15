"""
modified-sales-report.py - Generates sales report showing the total number
of melons each sales person sold.
"""
from salespeople import salespeople # import the existing salespeople dictionary
from sys import argv

script, file_name = argv # unpacks argv - remember to specify the
                            # text file in the command line!
print salespeople["Anna Parker"]
def update_salespeople_data(file_name):
    """Updates salespeople dictionary with data from text report"""
    sales_data = open(file_name)

    for line in sales_data:
        salesperson_data = line.rstrip().split("|")
        salesperson, melon_revenue, melons_sold = salesperson_data
        melon_revenue = float(melon_revenue)
        melons_sold = int(melons_sold)
        # Loops through each line in the text file, splits the string
        # to a list of words, then unpacks the data in the list,
        # reassigning the variables of the tuple as float or
        # integers as necessary

        if salesperson not in salespeople:
            salesperson_dict = dict(revenue=melon_revenue,
                                    tally=melons_sold,
                                    )
            salespeople[salesperson] = salesperson_dict
            # if salesperson not in the salespeople dictionary,
            # creates a dictionary, with the salesperson's
            # data as key/value pairs, and adds to the salespeople
            # dictionary the salesperson as a key and the
            # dictionary of the salesperson's data as its value.

        else:
            salespeople[salesperson]["revenue"] += melon_revenue
            salespeople[salesperson]["tally"] += melons_sold
            # if the salesperson is in the salespeople dictionary,
            # updates the revenue and melons sold with the
            # variable values unpacked from the data list

    return salespeople
    # Returns the updated salespeople dictionary

def print_sales_report(salespeople):
    for salesperson, sales_data in salespeople.items():
        print "%s sold %d melons, making $%.2f" %  (salesperson,
                                                    sales_data["revenue"],
                                                    sales_data["tally"])


print_sales_report(update_salespeople_data(file_name))
