from matplotlib.pyplot import barh, xlabel, title, figure, savefig, ylim, xlim, legend, xticks, yticks, grid, subplot

figure()
ax = subplot(111)
ax.set_axisbelow(True)
#ax.set_aspect(5.0)

sort = ( 865, 0 )
mkdup = ( 1869, 0 )
sd = ( 15, 0 )
indel = ( 2379, 0 )
recal = ( 494, 0 )
bqsr = ( 1195, 0 )
preprocess = ( 0, 198 )
hc = ( 2389, 2389 )

def merge(one, two):

    return (one[0] + two[0], one[1] + two[1])

b1 = merge(sort, mkdup)
b2 = merge(b1, sd)
b3 = merge(b2, indel)
b4 = merge(b3, recal)
b5 = merge(b4, bqsr)
b6 = merge(b5, preprocess)

r = range(2)

yticks([0.4, 1.4], ["GATK", "ADAM"])
ylim(-0.2, 2)

xloc = []
xnam = []

for i in range(17):
    xloc.append(i * 600)
    xnam.append("%s" % (i * 10))

xticks(xloc, xnam)
xlim(0, 9600)
title("Runtime for ADAM and GATK Best Practices Pipelines")

grid(True)
xlabel("Runtime (hours)")

barh(r, sort, label = "Sort", color = "red")
barh(r, mkdup, left = sort, label = "MkDup", color = "orange")
barh(r, sd, left = b1, label = "SeqDict", color = "yellow")
barh(r, indel, left = b2, label = "Indel", color = "green")
barh(r, recal, left = b3, label = "BQSR Table", color = "blue")
barh(r, bqsr, left = b4, label = "Apply BQSR", color = "cyan")
barh(r, preprocess, left = b5, label = "ADAM", color = "purple")
barh(r, hc, left = b6, label = "HapCaller", color = "grey")

legend()


savefig("perf.pdf")
