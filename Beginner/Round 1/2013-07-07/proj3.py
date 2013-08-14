# PROJECT 3
# Create function hotelCost that takes in number of days and nightly rate and returns the pre-tax total cost.
# Create getTax function that takes pre-tax total and a tax rate and returns the grand total.
def hotelCost(days, rate):
	return rate * days

def getTax(subtotal, tax):
	total = subtotal + (subtotal * tax)
	return total

bill = hotelCost(5, 140)
print getTax(bill, .08)