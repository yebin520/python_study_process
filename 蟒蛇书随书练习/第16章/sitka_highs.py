import csv
from matplotlib import pyplot as plt
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next (reader)
    #print (header_row)

    # for index,column_header in enumerate(header_row):
    #     print (index,column_header)
    highs = []
    for row in reader :
        high = int(row[5])
        highs.append(high)
    print (highs)

    plt.style.use('seaborn')
    fig,ax = plt.subplots()
    ax.plot(highs,c = 'red')

    ax.set_title("mei'ri'zui")