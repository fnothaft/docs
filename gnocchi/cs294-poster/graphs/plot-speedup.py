from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

def setup(n):
    exp_n = [1, n [-1] / n [0]]
    l_n = [n [0], n [-1]]

    figure ()
    loglog (l_n, exp_n, 'k-', basex=2, basey=2, label="Ideal Speedup")

def plot (n, mt, label_name, pattern):

    st = mt[0]
    speedup = []
    
    for m in mt:
        
        speedup.append (st / m)

    loglog (n, speedup, pattern, basex=2, basey=2, label=label_name)

def label(name, t):
    locs,labels = xticks()
    xn = ["64", "128", "256", "512", "1024"]
    xticks(locs, xn)

    yn = ["1/2", "1", "2", "4", "8", "16"]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Cores")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n = [64, 256, 1024]

fill = list(reversed([53.7677, 33.3888, 42.5564]))
dim = list(reversed([40.9316, 25.2168, 31.4274]))
sim = list(reversed([54.0453, 30.189, 39.2588]))
reg = list(reversed([53.8249, 40.9535, 42.3662]))

setup(n)

plot(n, fill, 'Impute', 'r+--')
plot(n, dim, 'PCA', 'bx-')
plot(n, sim, 'Similarity', 'mo-.')
plot(n, reg, 'GWA', 'c.--')

label("speedup.pdf",
      "Speedup on NCI-60")

