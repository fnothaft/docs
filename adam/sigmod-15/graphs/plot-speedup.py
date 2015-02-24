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

    yn = ["1/16", "1/8", "1/4", "1/2", "1", "2", "4", "8", "16", "32", "64"]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Cores")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n = [32, 1024]

flagstat_n = [32, 512, 1024]
flagstat = [2.0 + 17.0 / 60.0, 49.0 / 60.0, 1.0 + 20.0 / 60.0]
markdup_n = [32, 512, 1024]
markdup = [419, 24.0 + 23.0 / 60.0, 18.0 + 19.0 / 60.0]
bqsr_n = [32, 1024]
bqsr = [1602.0, 25.0 + 59.0 / 60.0]
ir_n = [32, 1024]
ir = [509.0, 26.0 + 59.0 / 60.0]
sort_n = [32, 512, 1024]
sort = [108.0, 18.0 + 56.0 / 60.0, 10.0 + 31.0 / 60.0]

setup(n)

plot(flagstat_n, 6.0 + 11.0 / 60.0, flagstat, 'Flagstat', 'r+--')
plot(markdup_n, 44.0 + 50.0 / 60.0, markdup, 'Mark Duplicates', 'bx-')
plot(bqsr_n, 1283.0, bqsr, 'BQSR', 'mo-.')
plot(ir_n, 658.0, ir, 'INDEL Realignment', 'c.--')
plot(sort_n, 83.0, sort, 'Sort', 'y*-')

label("speedup_na12878.pdf",
      "Speedup on NA12878 (High Coverage)")

