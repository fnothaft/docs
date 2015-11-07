from pylab import ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure, hold, plot, xlim, ylim

def dateIdx(year, month):

    return year * 12 + month

def submit(id, subDate, reviewDate, accept):

    plot([subDate, reviewDate], [id, id], ":x", markersize = 0)
    plot([subDate], [id], "|")
    if accept:
        plot([reviewDate], [id], "*")
    else:
        plot([reviewDate], [id], "x")

def appear(id, subDate, appearDate):

    plot([subDate, appearDate], [id, id], "-D", markersize = 3)

def posted(id, date):

    plot([date], [id], 'o')

figure()
hold(True)
xlim(dateIdx(2010, 0), dateIdx(2015, 12))
ylim(0, 11)

# 1. malladi et al
# isca 2011
submit(1, dateIdx(2010, 12), dateIdx(2011, 2), False)

# micro 2011
submit(1, dateIdx(2011, 5), dateIdx(2011, 8), False)

# hpca 2012
submit(1, dateIdx(2011, 9), dateIdx(2011, 11), False)

# isca 2012
submit(1, dateIdx(2011, 12), dateIdx(2012, 2), True)
appear(1, dateIdx(2012, 4), dateIdx(2012, 6))

# 2. honors thesis
posted(2, dateIdx(2011, 6))

# 3. nothaft et al, emulation
# dac '13
submit(3, dateIdx(2012, 12), dateIdx(2013, 2), False)

# dac '14
submit(3, dateIdx(2013, 12), dateIdx(2014, 2), False)

# iccad '14
submit(3, dateIdx(2014, 4), dateIdx(2014, 6), True)
appear(3, dateIdx(2014, 7), dateIdx(2014, 11))

# 4. massie et al
posted(4, dateIdx(2013, 11))

# 5. nothaft et al, adam -> sigmod
submit(5, dateIdx(2014, 11), dateIdx(2014, 12), False)
submit(5, dateIdx(2014, 12), dateIdx(2014, 2), True)
appear(5, dateIdx(2014, 3), dateIdx(2014, 5))

# 6. nothaft et al, de bruijn graph
# recomb-seq '15
submit(6, dateIdx(2015, 1), dateIdx(2015, 2), False)

# 7. paten et al, jamia
submit(7, dateIdx(2015, 2), dateIdx(2015, 3), True)
appear(7, dateIdx(2015, 4), dateIdx(2015, 7))

# 8. zheng et al
# sc '15
submit(8, dateIdx(2015, 4), dateIdx(2015, 6), False)

# bigdata '15
submit(8, dateIdx(2015, 7), dateIdx(2015, 9), True)
appear(8, dateIdx(2015, 9), dateIdx(2015, 11))

# arxiv
posted(8, dateIdx(2015, 7))

# 9. masters thesis
posted(9, dateIdx(2015, 5))

# 10. nothaft & rael, power domain
submit(10, dateIdx(2015, 9), dateIdx(2015, 11), False)

xticks([dateIdx(2010, 1), dateIdx(2011, 1), dateIdx(2012, 1), dateIdx(2013, 1), dateIdx(2014, 1), dateIdx(2015, 1), dateIdx(2016, 1)],
       ["2010", "2011", "2012", "2013", "2014", "2015", "2016"])
yticks(range(1, 11),
       ["C1", "TH1", "C2", "TR1", "C3", "S1", "J1", "C4", "TH2", "S2"])

savefig("submissions.pdf")
