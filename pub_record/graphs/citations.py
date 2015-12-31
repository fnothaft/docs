from matplotlib.pyplot import ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure, hold, plot, xlim, ylim, subplot, semilogy
import matplotlib.gridspec as gridspec

def dateIdx(year, month):

    return year * 12 + (month - 1)

fig = figure()
fig.set_size_inches(8, 12)
print fig.get_size_inches()
gs = gridspec.GridSpec(3, 1, height_ratios=[3,3,1])

citeAx = subplot(gs[0])
xlim(dateIdx(2010, 1), dateIdx(2016, 1))
xticks([dateIdx(2010, 1), dateIdx(2011, 1), dateIdx(2012, 1), dateIdx(2013, 1), dateIdx(2014, 1), dateIdx(2015, 1), dateIdx(2016, 1)],
       ["2010", "2011", "2012", "2013", "2014", "2015", "2016"])
ylim(0, 120)
citeAx.hold(True)

logCiteAx = subplot(gs[1])
xlim(dateIdx(2010, 1), dateIdx(2016, 1))
xticks([dateIdx(2010, 1), dateIdx(2011, 1), dateIdx(2012, 1), dateIdx(2013, 1), dateIdx(2014, 1), dateIdx(2015, 1), dateIdx(2016, 1)],
       ["2010", "2011", "2012", "2013", "2014", "2015", "2016"])
ylim(1, 120)
logCiteAx.hold(True)

metricAx = subplot(gs[2])
xlim(dateIdx(2010, 1), dateIdx(2016, 1))
xticks([dateIdx(2010, 1), dateIdx(2011, 1), dateIdx(2012, 1), dateIdx(2013, 1), dateIdx(2014, 1), dateIdx(2015, 1), dateIdx(2016, 1)],
       ["2010", "2011", "2012", "2013", "2014", "2015", "2016"])
ylim(0, 5)
yticks(range(6), ["0", "1", "2", "3", "4", "5"])
metricAx.hold(True)

startDate = dateIdx(2011, 6)
curDate = dateIdx(2016, 1)
venues = {}
articleCitations = {}
citations = [0] * (curDate - startDate + 1)
h = []
i10 = [0] * (curDate - startDate + 1)

def printStats():

    month = curDate % 12
    year = curDate / 12
    print "As of %d/%d, %d citations, h-index of %d, i10 of %d." % (month + 1, year, citations[-1], h[-1], i10[-1])
    print ""
    print "Articles:"
    
    for (key, value) in articleCitations.iteritems():
        print "%s -> %d citations" % (key, value[1][-1])

def hIndex(array, h = 0):
    
    count = 0
    for a in array:
        if a >= h:
            count += 1

    if count >= h:
        return hIndex(array, h + 1)
    else:
        return h - 1

def plotMetrics():

    for i in range(startDate, curDate + 1):
        
        c = []
        
        for key, value in articleCitations.iteritems():

            (start, ac) = value
            
            if start <= i:
                
                if ac[i - start] >= 10:
                    i10[i - startDate] += 1
                
                c.append(ac[i - start])
                
        h.append(hIndex(c))

    metricAx.plot(range(startDate, curDate + 1), i10, "--", label = "i10")
    metricAx.plot(range(startDate, curDate + 1), h, "-", label = "h")

def plotPaper(appeared,
              citedBy,
              pubLabel):
    hold(True)

    yrange = range(appeared, curDate + 1)
    months = len(yrange)
    cites = [0] * months
    citeVenues = {}

    for citation in citedBy:
        
        (venue, date) = citation
        
        if venue in citeVenues:
            citeVenues[venue] += 1
        else:
            citeVenues[venue] = 1
            
        for i in range(date - appeared, months):
            cites[i] += 1
            
        for i in range(date - startDate, curDate - startDate + 1):
            citations[i] += 1

    citeAx.plot(yrange,
                cites,
                label = pubLabel)

    logCiteAx.semilogy(yrange,
                       cites,
                       label = pubLabel)

    venues[pubLabel] = citeVenues
    articleCitations[pubLabel] = (appeared, cites)

# malladi et al, power proportionality, C1
# appeared june 2012
# total: 79
# 3 extra in scholar, neel12, tabkhi14esl is duplicated, ali15 is duplicated, pinel68
plotPaper(dateIdx(2012, 6),
          [("IJHPSA", dateIdx(2012, 12)), # mittal12
           ("MICRO", dateIdx(2012, 12)), # wong12
           ("MICRO", dateIdx(2012, 12)), # jiang12
           ("MICRO", dateIdx(2012, 12)), # malladi12
           ("MICRO", dateIdx(2012, 12)), # chatterjee12
           ("TACO", dateIdx(2013, 1)), # du13
           ("HPCA", dateIdx(2013, 2)), # guevara13
           ("HPCA", dateIdx(2013, 2)), # sampson13hpca
           ("HPCA", dateIdx(2013, 2)), # ham13
           ("HPCA", dateIdx(2013, 2)), # li13
           ("HPCA", dateIdx(2013, 2)), # hou13
           ("DATE", dateIdx(2013, 3)), # kozyrakis13
           ("ISPASS", dateIdx(2013, 4)), # hardy13
           ("ISCA", dateIdx(2013, 6)), # sanchez13
           ("ISCA", dateIdx(2013, 6)), # wu13
           ("SIGMETRICS", dateIdx(2013, 6)), # tudor13
           ("ICS", dateIdx(2013, 6)), # fang13
           ("IUS", dateIdx(2013, 7)), # sampson13ius
           ("ACN", dateIdx(2013, 8)), # bauknecht13
           ("thesis", dateIdx(2013, 10)), # fang13
           ("thesis", dateIdx(2013, 11)), # stutsman13
           ("thesis", dateIdx(2013, 11)), # tudor13thesis
           ("TOCS", dateIdx(2014, 2)), # guevara14tocs
           ("HPCA", dateIdx(2014, 2)), # guevara14hpca
           ("ISSCC", dateIdx(2014, 2)), # horowitz14
           ("ISPASS", dateIdx(2014, 3)), # hansson14
           ("Micro", dateIdx(2014, 3)), # wu14micro
           ("ESL", dateIdx(2014, 5)), # tabkhi14esl
           ("thesis", dateIdx(2014, 5)), # deng14
           ("thesis", dateIdx(2014, 5)), # zhang14thesis
           ("HPDC", dateIdx(2014, 6)), # zhang14hpdc
           ("DSN", dateIdx(2014, 6)), # luo14
           ("ISCA", dateIdx(2014, 6)), # arelakis14
           ("ISCA", dateIdx(2014, 6)), # zhang14isca
           ("ISCA", dateIdx(2014, 6)), # jiang14
           ("ISCA", dateIdx(2014, 6)), # chen14
           ("VLSI", dateIdx(2014, 6)), # doller14
           ("ASAP", dateIdx(2014, 6)), # tabkhi14asap
           ("SIGGRAPH", dateIdx(2014, 7)), # hegarty14
           ("ICPP", dateIdx(2014, 9)), # ramapantulu14
           ("HPEC", dateIdx(2014, 9)), # tran14
           ("thesis", dateIdx(2014, 9)), # mayap14
           ("iThings", dateIdx(2014, 9)), # takouna14
           ("TOCS", dateIdx(2014, 9)), # wu14tocs
           ("HotPower", dateIdx(2014, 10)), # li14
           ("SoCC", dateIdx(2014, 11)), # zhang14
           ("MICRO", dateIdx(2014, 12)), # volos14
           ("MICRO", dateIdx(2014, 12)), # mckeown14
           ("thesis", dateIdx(2014, 12)), # nguyen14
           ("thesis", dateIdx(2014, 12)), # jiang14
           ("TOSP", dateIdx(2015, 1)), # yang15
           ("TACO", dateIdx(2015, 1)), # wang15taco
           ("TOPDS", dateIdx(2015, 1)), # abad15
           ("C&DT", dateIdx(2015, 1)), # tabkhi15cdt
           ("HPCA", dateIdx(2015, 2)), # petruci15
           ("book", dateIdx(2015, 3)), # careglio15
           ("TOC", dateIdx(2015, 3)), # lu15
           ("FECCS", dateIdx(2015, 4)), # gung15
           ("thesis", dateIdx(2015, 5)), # yang15
           ("thesis", dateIdx(2015, 5)), # liu15
           ("ICS", dateIdx(2015, 6)), # gao15
           ("WBDB", dateIdx(2015, 6)), # boissier15
           ("ISCA", dateIdx(2015, 6)), # kanev15
           ("ISCA", dateIdx(2015, 6)), # lo15
           ("ENOC", dateIdx(2015, 6)), # ali15
           ("TOC", dateIdx(2015, 7)), # goossens15
           ("SAMOS", dateIdx(2015, 7)), # manoochehri15
           ("ISLPED", dateIdx(2015, 7)), # wang15ispled
           ("TOCC", dateIdx(2015, 8)), # luo15
           ("ADMS", dateIdx(2015, 8)), # meyer15
           ("CS&T", dateIdx(2015, 9)), # dayarathna15
           ("OOPSLA", dateIdx(2015, 10)), # jantz15
           ("ISSWC", dateIdx(2015, 10)), # wong15
           ("ISSWC", dateIdx(2015, 10)), # begum15
           ("HotPower", dateIdx(2015, 10)), # wang15hotpower
           ("JMicpro", dateIdx(2015, 11)), # tabhki15jmicpro
           ("JSPS", dateIdx(2015, 11)), # tabkhi15jsps
           ("TACO", dateIdx(2015, 11)), # lee15
           ("MASCOTS", dateIdx(2015, 11)), # malladi15
           ("TOADES", dateIdx(2015, 12)), # jung15
           ("CICC", dateIdx(2015, 12)), # lee15cicc
           ("ICCD", dateIdx(2015, 12)), # begum15
           ],
          "C1")

# massie et al, adam TR, TR1
# appeared november 2013
# total: 13
# 2 extra in scholar (nothaft15cs267, hyve poster)
plotPaper(dateIdx(2013, 11),
          [("CloudCom", dateIdx(2014, 12)), # amos14
           ("thesis", dateIdx(2014, 12)), # lipka14
           ("CIDR", dateIdx(2015, 1)), # diao15
           ("ArXiv", dateIdx(2015, 1)), # luckow15
           ("CEUR", dateIdx(2015, 3)), # brandt15
           ("CancerInform", dateIdx(2015, 4)), # agarwal14
           ("SIGMOD", dateIdx(2015, 5)), # nothaft15sigmod
           ("thesis", dateIdx(2015, 5)), # nothaft15thesis
           ("thesis", dateIdx(2015, 5)), # leo15
           ("GigaScience", dateIdx(2015, 6)), # siretskiy15
           ("ArXiv", dateIdx(2015, 6)), # roguski15
           ("thesis", dateIdx(2015, 10)), # curtis15
           ("SC", dateIdx(2015, 11)), # kovatch15
           ("PyHPC", dateIdx(2015, 11)), # zynda15
           ("BMC Genomics", dateIdx(2015, 12)), # obrien15
           ("book", dateIdx(2016, 1)), # szczerba16
           ],
          "TR1")

# nothaft et al, ana emulation, C2
# appeared november 2014
# total: 0
plotPaper(dateIdx(2014, 11),
          [],
          "C2")

# nothaft et al, adam -> sigmod, C3
# appeared may 2015
# total: 6
plotPaper(dateIdx(2015, 5),
          [("SIGMOD", dateIdx(2015, 5)), # armbrust15sigmod
           ("thesis", dateIdx(2015, 5)), # nothaft15thesis
           ("BigData", dateIdx(2015, 7)), # zhang15
           ("VLDB", dateIdx(2015, 8)), # armbrust15vldb
           ("DMAH", dateIdx(2015, 8)), # bessani15
           ("thesis", dateIdx(2015, 10)) # curtis15thesis
           ],
          "C3")

# nothaft, masters thesis, TH2
# appeared may 2015
# total: 0
plotPaper(dateIdx(2015, 5),
          [],
          "TH2")

# paten et al, BD2K, J1
# appeared july 2015
# total: 1
plotPaper(dateIdx(2015, 7),
          [("Cancer Discovery", dateIdx(2015, 11)), # lawler15
           ("BMC Genomics", dateIdx(2015, 12)), # obrien15
           ],
          "J1")

# zhang et al, Kira, C4
# appeared on arxiv july 2015, published at conference november 2015
# total: 0
plotPaper(dateIdx(2015, 7),
          [],
          "C4")

citeAx.plot(range(startDate, curDate + 1), citations, ":k", label = "Total")
citeAx.legend(loc = 2)
citeAx.grid(True)

logCiteAx.plot(range(startDate, curDate + 1), citations, ":k", label = "Total")
logCiteAx.legend(loc = 2)
logCiteAx.grid(True)

metricAx.grid(True)
plotMetrics()
metricAx.legend(loc = 2)

savefig("citations.pdf")

printStats()
