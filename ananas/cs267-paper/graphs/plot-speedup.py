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
    xn = ["1", "2", "4", "8"]
    xticks(locs, xn)

    yn = ["1", "2", "4", "8"]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Cores")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n = [1, 8]

an = [2, 4]
a = [166, 81]

setup(n)

plot(an, 166 * 2, a, 'ananas', 'r+-')

label("speedup.pdf",
      "Speedup on E. coli Dataset")

