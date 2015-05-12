from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

def setup(n):
    exp_n = [1, n [-1] / n [0]]
    l_n = [n [0], n [-1]]

    figure ()

def plot (n, mt, label_name, pattern):

    loglog (n, mt, pattern, basex=2, basey=2)

def label(name, t):
    locs,labels = xticks()
    xn = ["2", "4", "8"]
    xticks(locs, xn)

    ylabel ("Runtime (min)")
    xlabel ("Number of Buckets")
    title (t)
    grid (True)
    savefig (name)

n = [2, 4, 8]
a = [9.666, 25, 53]

setup(n)

plot(n, a, 'ananas', 'r+-')

label("overlap.pdf",
      "Overlapping Runtime on E. coli Dataset")

