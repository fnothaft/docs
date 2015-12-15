from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

def setup(n):
    exp_n = [1, n [-1] / n [0]]
    l_n = [n [0], n [-1]]

    figure ()
    loglog (l_n, exp_n, 'k-', basex=2, basey=2, label="Ideal Speedup")

def plot (n, mt, label_name, pattern):

    speedup = []

    st = mt[0]
    
    for m in mt:
        
        speedup.append (st / m)

    loglog (n, speedup, pattern, basex=2, basey=2, label=label_name)

def label(name, t, n):
    locs,labels = xticks()
    xn = []
    for i in n:
        xn.append(str(i))
    xticks(locs, xn)

    yn = ["1", "2", "4", "8", "16", "32", "64", "128"]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Cores")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n = [8, 16, 32, 64, 128, 256, 512, 960]

convert = [28.5, 17.9, 15.1, 16.4, 21.2, 16.8, 24.1, 16.4]
fill = [154.0, 96.0, 59.2, 44.7, 32.1, 29.9, 33.7, 43.5]
pca = [117.4, 51.8, 37.1, 25.4, 21.7, 24.8, 33.9, 38.5]
ssex = [90.8, 82.4, 38.2, 33.6, 30.1, 24.7, 31.8, 43.4]
ssap = [89.5, 55.7, 38.2, 29.4, 27.6, 25.9, 29.6, 44.3]

setup([8, 1024])

plot(n, convert, 'Convert', 'r+--')
plot(n, fill, 'Fill In', 'bx-')
plot(n, pca, 'PCA', 'mo-.')
plot(n, ssex, 'Exact Sim.', 'c.--')
plot(n, ssap, 'Approx. Sim.', 'y*-')

label("speedup_nci-60.pdf",
      "Speedup on NCI-60 Dataset",
      [8, 16, 32, 64, 128, 256, 512, 1024])

n = [64, 128, 256, 512, 960]

ssap = [7324.47, 3766.4, 2022.7, 1155.8, 1455.8]

setup([64, 1024])

plot(n, ssap, 'Approx. Sim.', 'y*-')

label("speedup_1kg.pdf",
      "Speedup on 1,000 Genomes Dataset",
      [64, 128, 256, 512, 1024])
