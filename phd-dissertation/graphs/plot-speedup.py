from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure, xlim, ylim

def setup(n):
    exp_n = [1, n [-1] / n [0]]
    l_n = [n [0], n [-1]]

    figure ()
    loglog (l_n, exp_n, 'k-', basex=2, basey=2, label="Ideal Speedup")

def plot (n, st, mt, label_name, pattern):

    speedup = []
    
    for m in mt:
        
        speedup.append (st / m)

    loglog (n, speedup, pattern, basex=2, basey=2, label=label_name)

def label(name, t):
    locs,labels = xticks()
    xn = ["", "32", "64", "128", "256", "512", "1024", ""]
    xticks(locs, xn)

    yn = ["", "1", "2", "4", "8", "16", "32", ""]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Threads")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n_ideal = [32, 1024]

n = [32, 128, 256, 512, 935]
markdup = [16639.22, 4438.37, 2005.25, 1247.36, 844.03]
bqsr = [27034.11, 7461.35, 4663.84, 2977.69, 2108.43]
ir = [23808.67, 6476.63, 3507.99, 3223.43, 1242.10]
bg = [25896.38, 6639.16, 3449.28, 1731.73, 920.95]

setup(n_ideal)

plot(n, markdup[0], markdup, 'Mark Duplicates', 'bx-')
plot(n, bqsr[0], bqsr, 'BQSR', 'mo-.')
plot(n, ir[0], ir, 'INDEL Realignment', 'c.--')
plot(n, bg[0], bg, 'Avocado', 'y*-')

label("speedup.pdf",
      "Speedup on NA12878 (High Coverage)")

