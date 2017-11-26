from datetime import date
from pylab import hist, stackplot, ylabel, xlabel, title, grid, savefig, show, legend, xticks, yticks, figure, xlim, ylim
from matplotlib.patches import Patch

start_date = date(2013, 1, 1)
dates = [0]
adam_core = [0]
adam_apis = [0]
adam_cli = [0]
adam_python = [0]
adam_r = [0]
avocado_core = [0]
avocado_cli = [0]
cannoli = [0]
formats = [0]
utils = [0]

fp = open("source.txt")

for line in fp:

    line = line.strip().rstrip().split()

    project = line[0]
    commit_date = line[1]
    lines = int(line[2])

    # parse date...
    commit_date = commit_date.split('T')[0].split('-')
    year = int(commit_date[0])
    month = int(commit_date[1])
    day = int(commit_date[2])

    commit_date = date(year, month, day)

    days = abs(commit_date - start_date).days

    if days != dates[-1]:
        dates.append(days)
        adam_core.append(adam_core[-1])
        adam_apis.append(adam_apis[-1])
        adam_cli.append(adam_cli[-1])
        adam_python.append(adam_python[-1])
        adam_r.append(adam_r[-1])
        avocado_core.append(avocado_core[-1])
        avocado_cli.append(avocado_cli[-1])
        cannoli.append(cannoli[-1])
        formats.append(formats[-1])
        utils.append(utils[-1])

        dates.append(days)
    
    if project == 'adam-core':
        adam_core.append(lines)
    if project == 'adam-apis':
        adam_apis.append(lines)
    if project == 'adam-cli':
        adam_cli.append(lines)
    if project == 'adam-python':
        adam_python.append(lines)
    if project == 'adam-r':
        adam_r.append(lines)

    if project == 'avocado-core':
        avocado_core.append(lines)
    if project == 'avocado-cli':
        avocado_cli.append(lines)

    if project == 'cannoli':
        cannoli.append(lines)

    if project == 'bdg-formats':
        formats.append(lines)

    if project == 'utils':
        utils.append(lines)

last_date = date(2018, 1, 1)

days = abs(last_date - start_date).days

dates.append(days)

adam_core.append(adam_core[-1])
adam_apis.append(adam_apis[-1])
adam_cli.append(adam_cli[-1])
adam_python.append(adam_python[-1])
adam_r.append(adam_r[-1])
avocado_core.append(avocado_core[-1])
avocado_cli.append(avocado_cli[-1])
cannoli.append(cannoli[-1])
formats.append(formats[-1])
utils.append(utils[-1])

def pad(l):

    difference = len(adam_core) - len(l)

    if difference != 0:

        pad_by = [0] * difference
        pad_by.extend(l)
        return pad_by
    else:
        return l

adam_apis = pad(adam_apis)
adam_cli = pad(adam_cli)
adam_python = pad(adam_python)
adam_r = pad(adam_r)
avocado_core = pad(avocado_core)
avocado_cli = pad(avocado_cli)
cannoli = pad(cannoli)
formats = pad(formats)
utils = pad(utils)

labels = ['ADAM',
          'Avocado',
          'Cannoli',
          'BDG-Formats',
          'Utils']
        
figure()
title('Lines of code across the BDG projects over time')
xlabel('Time')
ylabel('Lines of source code')
stackplot(dates,
          adam_core, adam_apis, adam_cli, adam_python, adam_r,
          avocado_core, avocado_cli, cannoli, formats, utils,
          colors = ["#FF0000", "#EE0000", "#DD0000", "#CC0000", "#BB0000",
                    "#00FF00", "#00DD00",
                    "#0000FF",
                    "#FF00FF",
                    "#808080"], edgecolor='none')
legend([Patch(color="#FF0000"),
        Patch(color="#00FF00"),
        Patch(color="#0000FF"),
        Patch(color="#FF00FF"),
        Patch(color="#808080")],
       labels,
       loc=2)
xlim(0, (last_date - start_date).days)
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
savefig('source.pdf')
