
from pylab import xlabel, ylabel, title, savefig, figure, bar, xticks, show

figure()
xlabel("# of 5bp Spacings Lost/Gained")
ylabel("Region Count")
title("Spacing Changes per Region")


x = [87, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 714, 9, 9, 0, 0, 0, 53, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 155, 0, 0, 240, 30, 2159, 237, 6, 36, 19, 1854, 128856, 319, 970, 0, 0, 515, 12, 1404, 1330, 336, 0, 0, 1, 401, 48, 303, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1233, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1982, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 784]

n = len(x)
width = 1
labelGap = 20
r = range(0, n, labelGap)
l = []
step = (102 - -39) / labelGap

for i in r:
	l.append("%d" % (-39 + i))

bar(range(n), x, width, log = True)
xticks(r, l)

savefig("spacing.pdf")

