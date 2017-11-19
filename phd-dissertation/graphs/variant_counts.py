from pylab import plot, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

idx = [0]
variants = [0]

fp = open('variant_counts.txt')

for line in fp:

    line = line.strip().rstrip().split()

    idx.append(int(line[0]))
    variants.append(int(line[1]))

figure()
plot(idx, variants)
title('Variants seen as a function of samples observed')
xlabel('Samples observed')
ylabel('Variants observed')
savefig('variant_counts.pdf')
