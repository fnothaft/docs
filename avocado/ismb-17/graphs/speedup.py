from pylab import loglog, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure

cores = [ 896, 512, 256, 128, 64, 32, 16 ]
ideal = [ 1024, 16 ]

indel = [ ((39.0 + 56.0 / 60.0) - (34.0 + 15.0 / 60.0)), # 896
          ((20.0 + 31.0 / 60.0) - (14.0 + 59.0 / 60.0)), # 512
          ((64.0 + 55.0 / 60.0) - (55.0 + 13.0 / 60.0)), # 256
          ((25.0 + 50.0 / 60.0) - (8.0 + 39.0 / 60.0)), # 128
          ((54.0 + 59.0 / 60.0) - (22.0 + 13.0 / 60.0)), # 64
          ((159.0 + 19.0 / 60.0) - (36.0 + 51.0 / 60.0)), # 32
          ((18.0 * 60.0 + 6.0 + 56.0 / 60.0) - (15.0 * 60.0 + 52.0 + 0.0)), # 16
          ]
r_indel_ideal = [ 1024.0 / (16.0 * indel[6]), # 1024
                  1.0 / indel[6]
                ]
vc_no_mask = [ (34.0 + 55.0 / 60.0), # 896
               ((55.0 + 10.0 / 60.0) - (20.0 + 35.0 / 60.0)), # 512
               ((68.0 + 35.0 / 60.0) - (5.0 + 0.0 / 60.0)), # 256
               ((142.0 + 9.0 / 60.0) - (25.0 + 53.0 / 60.0)), # 128
               ((4.0 * 120.0 + 36.0 / 60.0) - (55.0 + 3.0 / 60.0)), # 64
               ((15.0 * 60.0 + 46.0 + 2.0 / 60.0) - (5.0 * 60.0 + 50.0 + 7.0 / 60.0)), # 32
               (((24.0 + 13.0) * 60.0 + 18.0 + 13.0 / 60.0) - (18.0 * 60.0 + 7.0 + 0.0)), # 16
               ]
r_vc_no_mask_ideal = [ 1024.0 / (16.0 * vc_no_mask[6]), # 1024
                       1.0 / vc_no_mask[6] # 64
                       ]

r_indel = []
r_vc_no_mask = []

for i in range(len(indel)):

    r_indel.append(1.0 / indel[i])
    r_vc_no_mask.append(1.0 / vc_no_mask[i])

figure()

title("Runtime vs. number of cores for high coverage NA12878")
ylabel("Runtime (minutes)")
xlabel("Number of cores")
loglog(cores, r_indel, color='orange', basex=2, basey=2, label="Realignment")
loglog(ideal, r_indel_ideal, color='orange', linestyle='dotted', basex=2, basey=2)
loglog(cores, r_vc_no_mask, color='blue', basex=2, basey=2, label="Genotyping")
loglog(ideal, r_vc_no_mask_ideal, color='blue', linestyle='dotted', basex=2, basey=2)
legend(loc=2)

xl = [ 64, 128, 256, 512, 1024 ]
xn = [ "64", "128", "256", "512", "1024" ]
xticks(xl, xn)

yl = [1.0 / 4.0, 1.0 / 8.0, 1.0 / 16.0, 1.0 / 32.0,
      1.0 / 64.0, 1.0 / 128.0, 1.0 / 256.0, 1.0 / 512.0 ]
yn = ["4", "8", "16", "32", "64", "128", "256", "512"]
yticks(yl, yn)

savefig("speedup.pdf")
