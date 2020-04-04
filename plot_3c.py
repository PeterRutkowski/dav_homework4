import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def prepare_data():
    data = pd.read_csv("data/temperatures_clean.csv")
    countries = np.asarray(data['country_id'])
    average_temp_celsius = np.asarray(data['AverageTemperatureCelsius'])
    del data

    country_codes = ['BRA', 'FRA', 'JAP', 'NEW', 'POL', 'SOU', 'SWE', 'UKR']

    temp_indices = []
    for i in range(len(country_codes)):
        temp_indices.append([])
    for i in range(len(countries)):
        for j in range(len(country_codes)):
            if countries[i] == country_codes[j]:
                temp_indices[j].append(i)

    average_temp_celsius_split = []
    for i in range(len(temp_indices)):
        temp_single_country = []
        for j in range(len(temp_indices[i])):
            temp_single_country.append(average_temp_celsius[temp_indices[i][j]])
        average_temp_celsius_split.append(temp_single_country)

    return country_codes, average_temp_celsius_split

def plot(average_temp_celsius, countries):
    fig, ax = plt.subplots()

    plt.ylabel('AverageTemperatureCelsius')
    plt.xlabel('country_id')
    plt.tight_layout()
    plt.grid(True, zorder=0, color='white')

    major_x_ticks = np.arange(1, 9, 1)
    major_y_ticks = np.arange(-10, 32, 10)
    minor_y_ticks = np.arange(-15, 32, 5)

    ax.set_facecolor((0.88,0.88,0.88))
    ax.set_xlim(0.5, 8.5)
    ax.set_ylim(-18, 32)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticks(major_x_ticks)
    ax.set_xticklabels(countries)
    ax.set_yticks(major_y_ticks)
    ax.set_yticks(minor_y_ticks, minor=True)
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
    ax.tick_params(axis='y', colors='grey', which='minor')
    ax.grid(True, zorder=0, color='white', which='minor', linewidth=0.4)
    ax.grid(True, zorder=0, color='white', which='major', linewidth=1)
    ax.set_axisbelow(True)

    ax.violinplot(average_temp_celsius, showmeans=False, showmedians=False, showextrema=False, widths=0.8)

    plt.savefig('plots/3c.png', dpi=200)
    plt.clf()

countries, average_temp_celsius = prepare_data()

plot(average_temp_celsius, countries)