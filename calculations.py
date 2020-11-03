import numpy
#calc_mode
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
my_mean = numpy.mean(test_scores)
print("the mean is: ", my_mean)

#cal_Median
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
my_mean=numpy.mean(test_scores)
my_median=numpy.median(test_scores)
print("The median is ", my_median)

#calc_inter-quartile_Range
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
x = numpy.percentile(test_scores, 75)
print("The 75% percentile for the marks is ", x)

#calc_variance
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
x = numpy.var(test_scores)
print("The variance of the marks is  ", x)

import scipy


from scipy import stats
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
my_mode = stats.mode(test_scores)
print("The mode is ", my_mode)

#Calc_Range
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
my_range=numpy.ptp(test_scores)
print("The range is ", my_range)

#calc_standard deviation
my_stdn = numpy.std(test_scores)
test_scores = [12,99,86,87,88,45,87,94,78,77,85,86]
print("The standard deviation is ", my_stdn)

import matplotlib.pyplot as plt
#bar_graphs
girls_age=[19, 24, 19, 17]
girls_names=["skylar", "Nadine", "zoe", "lelethu"]
x_pos=[i for i, _ in enumerate(girls_names)]
plt.bar(x_pos, girls_age, color="black")
plt.xticks(x_pos, girls_names)
plt.show()

test_scores = [12,99,65,85,42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo","Ziyaad" ]


