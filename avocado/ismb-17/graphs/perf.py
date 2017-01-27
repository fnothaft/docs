# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 2
discovery = (2, 2)
score = (18, 43)
call = (0.5, 7)
precall = (20, 45)
ind = np.arange(N)    # the x locations for the groups
width = 0.5       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, discovery, width, color='#ff0000')
p2 = plt.bar(ind, score, width, bottom=discovery, color='#00ff00')
p3 = plt.bar(ind, call, width, bottom=precall, color='#0000ff')

plt.ylabel('Time (min)')
plt.title('Runtime per stage')
plt.xlim(-0.4, 2.0)
plt.xticks((0.25, 1.25), ('Single', 'gVCF'))
plt.yticks(np.arange(0, 56, 5))
plt.legend((p1[0], p2[0], p3[0]), ('Discovery', 'Scoring', 'Call & Filter'), loc = 2)

plt.savefig("perf.pdf")
