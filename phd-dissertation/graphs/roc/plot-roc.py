from pylab import plot, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure, ylim

def read_roc(filename, take=1):

    recall = []
    precision = []

    fp = open(filename)

    idx = 0
    lastidx = 2
    
    for line in fp:

        idx += 1
        
        if idx >= 2:

            if ((idx == lastidx) or
                (idx == lastidx + take)):

                lastidx = idx
                
                line = line.strip().rstrip().split(',')

                try:
                    r = float(line[7])
                    p = float(line[8])
                    recall.append(r)
                    precision.append(p)
                except:
                    pass

    return (recall, precision)

# snps
(avo_r, avo_p) = read_roc('avocado.snp.roc.csv', take=1)
(gatk_r, gatk_p) = read_roc('gatk.snp.roc.csv', take=1)
(sam_r, sam_p) = read_roc('mpileup.snp.roc.csv', take=1)
(fb_r, fb_p) = read_roc('freebayes.snp.roc.csv', take=1)

figure()

plot(avo_r, avo_p, 'b--', label='Avocado')
plot(gatk_r, gatk_p, 'g-', label='GATK HC')
plot(sam_r, sam_p, 'r-.', label='Mpileup/Call')
plot(fb_r, fb_p, 'k--', label='FreeBayes')
legend(loc=3)
ylim(0.6, 1.0)
xlabel('Recall')
ylabel('Precision')
title('SNP Calling Precision/Recall Curve')
savefig('snp.pdf')

# indels
(avo_r, avo_p) = read_roc('avocado.indel.roc.csv', take=1)
(gatk_r, gatk_p) = read_roc('gatk.indel.roc.csv', take=1)
(sam_r, sam_p) = read_roc('mpileup.indel.roc.csv', take=1)
(fb_r, fb_p) = read_roc('freebayes.indel.roc.csv', take=1)

figure()

plot(avo_r, avo_p, 'b--', label='Avocado')
plot(gatk_r, gatk_p, 'g-', label='GATK HC')
plot(sam_r, sam_p, 'r-.', label='Mpileup/Call')
plot(fb_r, fb_p, 'k--', label='FreeBayes')
legend(loc=3)
ylim(0.6, 1.0)
xlabel('Recall')
ylabel('Precision')
title('INDEL Calling Precision/Recall Curve')
savefig('indel.pdf')
