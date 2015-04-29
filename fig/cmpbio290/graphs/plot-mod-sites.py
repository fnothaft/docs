
from pylab import xlabel, ylabel, title, savefig, figure, bar, xticks, show

figure()
xlabel("# of Modified TFBS")
ylabel("Region Count")
title("Number of TFBS Modified per Region")


x = [130954, 7722, 4013, 254, 115, 34, 121, 149, 83, 53, 0, 0, 0, 567, 10, 17, 1, 0, 0, 48, 0, 0, 0, 2, 1]

n = len(x)
width = 1
labelGap = 5
r = range(0, n, labelGap)
l = []
step = (21 - 0) / labelGap

for i in r:
	l.append("%d" % (0 + i))

bar(range(n), x, width, log = True)
xticks(r, l)

savefig("mod-sites.pdf")

