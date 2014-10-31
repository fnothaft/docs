from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks
from numpy import arange

def plot (name, t, n, norm, adam, adammin, adamavg):
    adam_speedup = []
    adammin_speedup = []
    adamavg_speedup = []
    
    for a in adam:
        
        adam_speedup.append (norm / a)

    for a in adammin:
    
        adammin_speedup.append (norm / a)

    for a in adamavg:
        
        adamavg_speedup.append (norm / a)

    exp_n = [n [0], n [-1]]
    
    loglog (n, adam_speedup, 'g+-', basex=2, basey=2, label="ADAM")
    loglog (n, adammin_speedup, 'ro-', basex=2, basey=2, label="ADAM Min")
    loglog (n, adamavg_speedup, 'mD-', basex=2, basey=2, label="ADAM Avg")

    locs,labels = xticks()
    xn = ["", "1", "2", "4", "8"]
    xticks(locs, xn)

    locs,labels = yticks()
    yn = ["", "1", "2", "4"]
    yticks(locs, yn)

    ylabel ("Speedup (Normalized to Reading Without Predicate)")
    xlabel ("1/n")
    legend (loc=1)
    title (t)
    grid (True)
    savefig (name)

n = (1, 2, 4, 8)

normalize = 347771

adam = (344393.65, 268802.69, 232171.76, 208901.61)
adammin = (194427.50, 161077.63, 153326.84, 143381.75)
adamavg = (278014.56, 222766.20, 199353.10, 183846.99)

plot ("gapped_predicate_low_coverage.pdf",
      "Gapped Read Filtering Test (Low Coverage)",
      n, normalize, adam, adammin, adamavg)
