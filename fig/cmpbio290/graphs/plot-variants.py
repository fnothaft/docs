
from pylab import xlabel, ylabel, title, savefig, figure, bar, xticks, show

figure()
xlabel("Variants")
ylabel("Region Count")
title("Number of Variants Per Annotated Region")


x = [62210, 34947, 22680, 12198, 5849, 2419, 1910, 1208, 320, 119, 23, 82, 25, 25, 94, 32, 3]

n = len(x)
width = 1
labelGap = 3
r = range(0, n, labelGap)
l = []
step = (16 - 0) / labelGap

for i in r:
	l.append("%d" % (0 + i))

bar(range(n), x, width, log = True)
xticks(r, l)

savefig("variants.pdf")

