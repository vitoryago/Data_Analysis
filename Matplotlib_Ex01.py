#This is an exemple of exercise using Matplotlib
#Data provides sales information for a store located in a city of 1,500,000 people
#The store sells adult and children's prodcuts and is located in a large shopping mall in the city
#Which quick conclusions can you reach just using Matplotlib?

import matplotlib.pyplot as plt

#DATAS
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
total_sales = [17320, 16850, 18925, 19543, 21153, 22340, 24750, 28472, 23740, 20118, 19850, 17102]
kids_sales = [8324, 7817, 9432, 10781, 11102, 14308, 15821, 19820, 12897, 11879, 9769, 7583]

#Using graphs to do the analysis, I'll use the bar graph and the linear graph

#Creating subplots
#First subplot using bar graph
plt.subplot(1, 2, 1)
plt.bar(months, total_sales, color = 'red')
plt.plot(months, kids_sales, color = 'blue')
plt.axis('auto')
plt.title('Sales information')
plt.legend(['Kids Sales', 'Total Sales'], fontsize = 8, loc = 'upper left')
plt.xlabel('Months')
plt.ylabel('Sales')

#Second subplot using linear graph
plt.subplot(1, 2, 2)
plt.plot(months, total_sales, color = 'red')
plt.plot(months, kids_sales, color = 'blue')
plt.axis('auto')
plt.title('Sales information')
plt.legend(['Kids Sales', 'Total Sales'], fontsize = 8, loc = 'upper left')
plt.xlabel('Months')
plt.ylabel('Sales')

#Showing the results
plt.show()