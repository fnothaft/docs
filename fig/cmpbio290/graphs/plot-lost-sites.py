
from pylab import xlabel, ylabel, title, savefig, figure, bar, xticks, show

figure()
xlabel("# of Lost TFBS")
ylabel("Region Count")
title("Number of TFBS Lost per Region")


x = [143214, 888, 0, 19, 23]

n = len(x)
width = 1
labelGap = 1
r = range(0, n, labelGap)
l = []
step = (4 - 0) / labelGap

for i in r:
	l.append("%d" % (0 + i))

bar(range(n), x, width, log = True)
xticks(r, l)

savefig("lost-sites.pdf")

