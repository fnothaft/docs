from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

def plot (name, t, n, sort, markdup):

    sort_speedup = []
    markdup_speedup = []
    
    for s in sort:
        
        sort_speedup.append (sort [0] / s)
        
    for m in markdup:
        
        markdup_speedup.append (markdup [0] / m)

    exp_n = [1, n [-1] / n [0]]
    l_n = [n [0], n [-1]]

    figure ()    
    loglog (l_n, exp_n, 'b--', basex=2, basey=2, label="Ideal Speedup")
    loglog (n, sort_speedup, 'bx-', basex=2, basey=2, label="Sort")
    loglog (n, markdup_speedup, 'g+-', basex=2, basey=2, label="Mark Duplicates")

    locs,labels = xticks()
    locs = locs[1:-1]
    xn = ["16", "32", "64", "128"]
    xticks(locs, xn)

    yn = ["1", "2", "4", "8"]
    locs,labels = yticks()
    locs = locs[1:-1]
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Machines")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n = [16, 32, 64, 82]

na12878_sort = [29.6625, 17.046, 11.56, 8.8]
na12878_markdup = [50.29, 34.835, 15.14, 14]
hg00096_sort = [3.82, 3.36, 3.54, 3.51]
hg00096_markdup = [4.87, 3.08, 2.37, 2.45]

plot ("speedup_na12878.pdf",
      "Speedup on NA12878 (High Coverage)",
      n, na12878_sort, na12878_markdup)

plot ("speedup_hg00096.pdf",
      "Speedup on HG00096 (Low Coverage)",
      n, hg00096_sort, hg00096_markdup)
