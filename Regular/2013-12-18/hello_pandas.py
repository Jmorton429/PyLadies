import matplotlib.pyplot as plt
import pandas
import os, sys

#Numpy complains about data with text labels. It also just wants rows and columns-
#It skips header rows completely. For more useful IO of data,
# we can use a more powerful library created just for  data processing and 
# statistics: Pandas                 
present_directory = os.path.dirname(sys.argv[0])
data = pandas.read_csv(present_directory + os.sep + 'ames_iowa_housing_dataset.txt', header=0,delimiter="\t")

print "Listing available columns:", data.columns

plt.plot(data["Lot Area"], data["SalePrice"], 'r.') #Uses MATLAB style data formatting: red dot for plotted points
plt.xlabel("Lot Area")
plt.ylabel("Sale Price ($)")
plt.show()