from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

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
    xn = ["32", "64", "128", "256", "512", "1024"]
    xticks(locs, xn)

    yn = ["1/2", "1", "2", "4", "8", "16", "32", "64", "128"]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Cores")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n = [32, 1024]

flagstat_n = [256, 1024]
flagstat = [1.0 / 60.0, 1.9 / 60.0]
markdup_n = [1024]
markdup = [19.0 / 60.0]
bqsr_n = [32, 256, 1024]
bqsr = [34.0, 2.0 + 0.7 / 60.0, 54.0 / 60.0]
ir_n = [32, 256, 1024]
ir = [16.0, 100.0 / 60.0, 24.0 / 60.0]
sort_n = [32, 256, 1024]
sort = [9.0, 32.0 / 60.0, 9.4 / 60.0]

setup(n)

plot(flagstat_n, 25.5 / 60.0, flagstat, 'Flagstat', 'r+--')
plot(markdup_n, 20.0 + 22 / 60.0, markdup, 'Mark Duplicates', 'bx-')
plot(bqsr_n, 12.9 + 18.4, bqsr, 'BQSR', 'mo-.')
plot(ir_n, 42.8, ir, 'INDEL Realignment', 'c.--')
plot(sort_n, 17.75, sort, 'Sort', 'y*-')

label("speedup_na12878.pdf",
      "Speedup on NA12878 (High Coverage)")

