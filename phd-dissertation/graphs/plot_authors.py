from datetime import date
from pylab import stackplot, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure, xlim
from matplotlib.patches import Patch

start_date = date(2013, 1, 1)
dates = [0]
adam = [0]
avocado = [0]
cannoli = [0]
formats = [0]
utils = [0]

fp = open("authors.date.txt")

for line in fp:

    line = line.strip().rstrip().split()

    project = line[0]
    commit_date = line[2]

    # parse date...
    commit_date = commit_date.split('T')[0].split('-')
    year = int(commit_date[0])
    month = int(commit_date[1])
    day = int(commit_date[2])

    commit_date = date(year, month, day)

    days = abs(commit_date - start_date).days

    dates.append(days)
    adam.append(adam[-1])
    avocado.append(avocado[-1])
    cannoli.append(cannoli[-1])
    formats.append(formats[-1])
    utils.append(utils[-1])

    dates.append(days)
    
    if project == 'ADAM':
        adam.append(adam[-1] + 1)
    else:
        adam.append(adam[-1])

    if project == 'Avocado':
        avocado.append(avocado[-1] + 1)
    else:
        avocado.append(avocado[-1])

    if project == 'Cannoli':
        cannoli.append(cannoli[-1] + 1)
    else:
        cannoli.append(cannoli[-1])

    if project == 'Formats':
        formats.append(formats[-1] + 1)
    else:
        formats.append(formats[-1])

    if project == 'Utils':
        utils.append(utils[-1] + 1)
    else:
        utils.append(utils[-1])

last_date = date(2018, 1, 1)

days = abs(last_date - start_date).days

dates.append(days)
adam.append(adam[-1])
avocado.append(avocado[-1])
cannoli.append(cannoli[-1])
formats.append(formats[-1])
utils.append(utils[-1])
        
labels = ['ADAM',
          'Avocado',
          'Cannoli',
          'BDG-Formats',
          'Utils']
        
figure()
title('Unique contributors across the BDG projects over time')
xlabel('Time')
ylabel('Unique contributors')
stackplot(dates, adam, avocado, cannoli, formats, utils,
          colors = ["#FF0000",
                    "#00FF00",
                    "#0000FF",
                    "#FF00FF",
                    "#808080"])
xlim(0, (last_date - start_date).days)
legend([Patch(color="#FF0000"),
        Patch(color="#00FF00"),
        Patch(color="#0000FF"),
        Patch(color="#FF00FF"),
        Patch(color="#808080")],
       ['ADAM', 'Avocado', 'Cannoli', 'bdg-formats', 'bdg-utils'],
       loc=2)
xticks([0,
        (date(2014, 1, 1) - start_date).days,
        (date(2015, 1, 1) - start_date).days,
        (date(2016, 1, 1) - start_date).days,
        (date(2017, 1, 1) - start_date).days,
        (date(2018, 1, 1) - start_date).days],
       ['1/1/2013',
        '1/1/2014',
        '1/1/2015',
        '1/1/2016',
        '1/1/2017',
        '1/1/2018'])
savefig('authors.pdf')
