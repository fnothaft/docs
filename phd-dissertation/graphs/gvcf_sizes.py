from pylab import hist, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

sizes = []

fp = open("gvcf_sizes.txt")

total_size = 0.0
for line in fp:

    sample_size = float(line.strip().rstrip())
    total_size += sample_size
    sizes.append(sample_size)

print "Total size was: %f" % total_size

figure()
hist(sizes)
title("Distribution of Parquet-encoded gVCF sizes across all samples")
ylabel("Samples")
xlabel("Size (GB)")

savefig("gvcf_sizes.pdf")
