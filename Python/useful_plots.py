
# MATPLOTLIB TUTORIAL
# April 20, 2020

# Load Necessary Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Basic Graph
# go to the matplotlib documentation
x = [0,1,2,3,4,5]
y = [1,2,4,8,16,32]

# resize your graph
# plt.figure(figsize=(4,3), dpi=300)

# plt.plot(x, y, label='2^x', 
# 	color='red', linewidth=2, linestyle='--',
# 	marker='.', markersize=10, markeredgecolor='blue')

# shorthand notation: fmt = '[color][marker][line]'
plt.plot(x, y, 'ko-', label='$2^x$')

# add a second line to our graph
x2 = np.arange(0, 5.25, 0.25)
# plt.plot(x2, x2**2, 'rs-', label='$x^2$')

# plot some data with solid line and the other with dotted (like future values)
plt.plot(x2[:6], x2[:6]**2, 'r-', label='$x^2$')
plt.plot(x2[5:], x2[5:]**2, 'r--')

# there is a link in the video with more fonts
# plt.title('Exponential Growth', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.title('Exponential Growth', fontdict={'fontsize': 20})

# plt.xlabel('x-axis label', fontdict={'fontname': 'Arial'})
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')

# edit the tickmarks
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10,20,30,40])

# add in a legend
plt.legend()

# save your graph (dpi=300 is a good rule of thumb)
plt.savefig('myPlot1.png', dpi=300)
plt.savefig('myPlot2.svg', dpi=300, format='svg')

plt.show()



# 2. Bar Charts
labels = ['A', 'B', 'C']
values = [1, 4, 2]

# plt.figure(figsize=(6,4))

bars = plt.bar(labels, values)

# A
patterns = ['/', 'O', '*']
for bar in bars:
	bar.set_hatch(patterns.pop(0))

# B
# bars[0].set_hatch('/')
# bars[1].set_hatch('O')
# bars[2].set_hatch('*')

# plt.legend()

# I think figsize is in INCHES (check this)

plt.show()


