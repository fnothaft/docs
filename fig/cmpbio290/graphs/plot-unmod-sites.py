
from pylab import xlabel, ylabel, title, savefig, figure, bar, xticks, show

figure()
xlabel("# of Unmodified TFBS")
ylabel("Region Count")
title("Number of TFBS That Were Not Modified per Region")


x = [13104, 2254, 4298, 2184, 2890, 8204, 6378, 2184, 0, 163, 2171, 2314, 6605, 1892, 49, 3343, 1708, 5193, 3460, 6616, 2020, 1663, 2126, 2173, 95, 145, 2093, 2195, 213, 337, 6200, 3034, 1110, 4, 2685, 3837, 1, 0, 553, 3, 2133, 2973, 2189, 1346, 28, 2325, 5, 2196, 2180, 24, 1643, 0, 1985, 0, 0, 0, 0, 0, 0, 425, 5, 1816, 0, 0, 2276, 0, 0, 4, 2220, 2000, 24, 2114, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1, 0, 0, 0, 16, 1037, 0, 0, 1130, 0, 0, 2, 0, 0, 3, 2172, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2182, 0, 0, 0, 0, 0, 0, 1, 5, 2178]

n = len(x)
width = 1
labelGap = 20
r = range(0, n, labelGap)
l = []
step = (121 - 0) / labelGap

for i in r:
	l.append("%d" % (0 + i))

bar(range(n), x, width, log = True)
xticks(r, l)

savefig("unmod-sites.pdf")

