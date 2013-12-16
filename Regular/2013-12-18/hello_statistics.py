import matplotlib.pyplot as plt
import pandas
import os, sys
import numpy as np

present_directory = os.path.dirname(sys.argv[0])
filename = present_directory + os.sep + 'ames_iowa_housing_dataset.txt'
data = pandas.read_csv( filename,  header=0, delimiter="\t")

print "Listing available columns:", data.columns
plt.subplot(2, 1, 1)
plt.plot(data["Lot Area"], data["SalePrice"], 'r.') #Uses MATLAB style data formatting: red dot for plotted points
plt.xlabel("Lot Area")
plt.ylabel("Sale Price ($)")

#Calculate some statistics about these houses:
mean_sale_price = np.mean(data["SalePrice"])
mean_lot_area = np.mean(data["Lot Area"])
plt.plot([mean_lot_area], [mean_sale_price], 'g*')

#Calculate and plot a correlation line using the numpy linear regression linalg library:
A = np.array([data["Lot Area"], np.ones(len(data["Lot Area"]))])
w = np.linalg.lstsq(A.T,data["SalePrice"])[0] # obtaining the parameters

line = w[0]*data["Lot Area"] +w[1] # regression line
plt.plot(data["Lot Area"],line,'g-')
  

#CDF for the Lot Area:
plt.subplot(2, 1, 2)
n_counts, bin_edges = np.histogram(data["Lot Area"],bins=40,normed=True) 
cdf = np.cumsum(n_counts)  # cdf not normalized, despite above
scale = 1.0/cdf[-1]
ncdf = scale * cdf 
plt.plot(bin_edges[1:], ncdf, 'm-')
plt.xlabel("Lot Area")
plt.ylabel("CDF")

plt.show()
