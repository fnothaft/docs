from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

def plot (name, t, n, mpi, spark):

    mpi_speedup = []
    spark_speedup = []
    
    for m in mpi:
        
        mpi_speedup.append (mpi [0] / m)
        
    for s in spark:
        
        spark_speedup.append (mpi [0] / s)

    exp_n = [1, n [-1] / n [0]]
    l_n = [n [0], n [-1]]

    figure ()    
    loglog (l_n, exp_n, 'k-', basex=2, basey=2, label="Ideal Speedup")
    loglog (n, mpi_speedup, 'bx-', basex=2, basey=2, label="MPI")
    loglog (n, spark_speedup, 'g+-', basex=2, basey=2, label="Spark")

    locs,labels = xticks()
    xn = ["32", "64", "128", "256", "512"]
    xticks(locs, xn)

    yn = ["1", "2", "4", "8", "16"]
    locs,labels = yticks()
    yticks(locs, yn)

    ylabel ("Speedup")
    xlabel ("Number of Cores")
    legend (loc=2)
    title (t)
    grid (True)
    savefig (name)

n = [1, 4, 16]

mpi_madd = [373.59, 236.80, 292.93]
spark_madd = [132.17, 41.56, 33.10]

plot ("speedup_madd.pdf",
      "Speedup for mAdd",
      n, mpi_madd, spark_madd)
