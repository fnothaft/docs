from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks

def plot (name, t, n, bam, adam, adammin, adamavg):

    bam_speedup = []
    adam_speedup = []
    adammin_speedup = []
    adamavg_speedup = []
    
    for b in bam:
        
        bam_speedup.append (bam [0] / b)
        
    for a in adam:
        
        adam_speedup.append (bam [0] / a)

    for a in adammin:
    
        adammin_speedup.append (bam [0] / a)

    for a in adamavg:
        
        adamavg_speedup.append (bam [0] / a)

    exp_n = [n [0], n [-1]]
    exp_bam = [bam_speedup [0], (bam_speedup [0] * 16)]
    exp_adam = [adam_speedup [0], (adam_speedup [0] * 16)]
    exp_adammin = [adammin_speedup [0], (adammin_speedup [0] * 16)]
    exp_adamavg = [adamavg_speedup [0], (adamavg_speedup [0] * 16)]
    
    loglog (n, bam_speedup, 'bx-', basex=2, basey=2, label="BAM")
    loglog (exp_n, exp_bam, 'b--', basex=2, basey=2)
    loglog (n, adam_speedup, 'g+-', basex=2, basey=2, label="ADAM")
    loglog (exp_n, exp_adam, 'g--', basex=2, basey=2)
    loglog (n, adammin_speedup, 'ro-', basex=2, basey=2, label="ADAM Min")
    loglog (exp_n, exp_adammin, 'r--', basex=2, basey=2)
    loglog (n, adamavg_speedup, 'mD-', basex=2, basey=2, label="ADAM Avg")
    loglog (exp_n, exp_adamavg, 'm--', basex=2, basey=2)

    locs,labels = xticks()
    xn = ["", "1", "2", "4", "8", "16", ""]
    xticks(locs, xn)

    yn = ["", "", "1/2", "1", "2", "4", "8", "16", "32", "64", "128"]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup (Normalized to BAM)")
    xlabel ("Number of Machines")
    legend (loc=4)
    title (t)
    grid (True)
    savefig (name)

n = [1, 2, 4, 8, 16]

bam = [100306.24, 37519.54, 26141.39, 21954.62, 23908.54]
adam = [207254.19, 90511.94, 48233.65, 27379.37, 17105.28]
adammin = [13993.29, 6732.12, 3827.07, 2821.94, 1805.70]
adamavg = [104459.28, 49473.29, 26884.38, 15768.56, 9990.21]

plot ("length_and_quality_low_coverage.pdf",
      "Speedup on Length/Quality Statistic Test (Low Coverage)",
      n, bam, adam, adammin, adamavg)
