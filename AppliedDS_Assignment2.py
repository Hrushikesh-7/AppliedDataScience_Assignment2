# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def _readcleandata(path):
    """
    This function reads desired path as input paramter and returns the data 
    after cleaning data from the file by replacing blank data with 0 and 
    tranposing the values.
    """
    base=pd.read_csv(path,header=2)
    base.replace('..',0,inplace=True)
    base=base.fillna(0)
    baset=base
    baset=baset.set_index('Country Name') 
    basey=baset.transpose()
    return base,basey


def _heatmap_germany():
    """
    Generates Correlation Heatmap of Germany country considering few parameters
    such as Access to electricity, Electricity production from Coal, 
    hydroelectric sources, natural gas sources & nuclear sources data from 
    Rural land area where elevation is below 5 meters (sq. km) csv file.
    """
    data = mathdf1.iloc[10:15,10:15]
    np.random.seed(123)
    replace_zero = lambda x: np.random.randint(1, 5) if x == 0 else x
    data = data.apply(lambda x: x.apply(replace_zero))
    ct = [ 'Access to electricity \n(% of population)',
           'Electricity production from \n coal sources (% of total)',
           'Electricity production from \n hydroelectric sources (% of total)',
           'Electricity production from \n natural gas sources (% of total)',
           'Electricity production from \n nuclear sources (% of total)']
    dtcorr = data.corr()
    dtcorr = np.round(dtcorr,decimals=2)
    # create a heatmap using the 'hot' colormap
    heatmap = plt.imshow(dtcorr, cmap='gnuplot')
    # add a colorbar to the plot
    plt.colorbar(heatmap)
    #data = np.round(data).astype(int)
    #Add the annotations to each square
    for i in range(dtcorr.shape[0]):
        for j in range(dtcorr.shape[1]):
            plt.text(j, i, dtcorr.iloc[i, j], ha='center', va='center', 
                     color='white')
    # set the values that to be displayed on x and y axis, title plot
    plt.xticks(np.arange(0.5, 5.5), ct, rotation=90)
    plt.yticks(np.arange(0.5, 5.5),ct )
    plt.title('Correlative Heatmap of Germany')
    plt.show()
    return


def _ruralLandarea():
    """
    Show cases Multiple bar chart & Scatter plot of Rural land area where 
    elevation is below 5 meters of total percentage of Land.
    """
    #Plot's the grouped barchart for each set of y values
    x = framen['Country Name'].values[70:90]
    y1 = mathdf2['1990'].values[70:90]
    y2 = mathdf2['2000'].values[70:90]
    y3 = mathdf2['2015'].values[70:90]
    plt.bar(x, y1, width=0.2, align='center', label='1990')
    plt.bar([i + 0.2 for i in range(len(x))], y2, width=0.2, align='center', 
            label='2000')
    plt.bar([i + 0.4 for i in range(len(x))], y3, width=0.2, align='center', 
            label='2015')
    
    # Add labels,legend & show the plot
    plt.xlabel('coutries')
    plt.ylabel('values')
    plt.title('Rural landarea where elevation below 5 meters(% of total land)')
    plt.legend(title='Years', loc = "upper left", edgecolor = "black")
    plt.xticks(rotation=90)
    plt.show()
    #Plot the Scatter plot of various countries in 2015 year.
    x = framen['Country Name'].values[0:13]
    y = mathdf2['2015'].values[0:13]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    # Add labels and title
    ax.set_xlabel('Countries')
    ax.set_ylabel('Year-2015 Values')
    title = 'Rural landarea where elevation below 5 meters(% of total land)'
    ax.set_title(title)
    plt.xticks(rotation=90)
    plt.show()
    return
    

def _urbanLandarea():
    """
    Interprets horizontal stacked bar graph of Urban land area where elevation 
    is below 5 meters in the year 2015 & Rural land area where elevation is 
    below 5 meters in the years 1990 & 2000
    """
    #print(mathdf3.describe())
    y = np.arange(10)
    x1 = mathdf3['2015'].values[80:90]
    x2 = mathdf3['2015'].values[90:100]
    x3 = mathdf3['2015'].values[100:110]
    
    # Create horizontal bar plot
    fig, ax = plt.subplots()
    ax.barh(y, x1, label='2015 80,90')
    ax.barh(y, x2, left=x1, label='2015 90,100')
    ax.barh(y, x3, left=[sum(x) for x in zip(x1, x2)], label='2015 100,110')
    
    # Add labels and legend
    ax.set_xlabel('Years')
    ax.set_ylabel('Progression')
    title = 'Urban landarea where elevation below 5 meters(% of total land)'
    ax.set_title(title)
    ax.legend()
    plt.show()
    
    # Plot the bars for each set of y values
    x = framen1['Country Name'].values[50:70]
    y1 = mathdf3['1990'].values[50:70]
    y2 = mathdf3['2000'].values[50:70]
    plt.bar(x, y1, width=0.2, align='center', label='1990')
    plt.bar([i + 0.2 for i in range(len(x))], y2, width=0.2, align='center', 
            label='2000')
    # Add labels and legend
    plt.xlabel('Coutries')
    plt.ylabel('Elevation')
    title = "Rural landarea where elevation is below 5 meters(% of total land)"
    plt.title(title)
    plt.legend(title='Years', loc = "upper right", edgecolor = "black")
    plt.xticks(rotation=90)
    # Show the plot
    plt.show()
    return


def _heatmap_France():
    """
    Generates Heatmap of France country by considering few paramters such as 
    Rural and urban population living elev >5m, Population living elm5 and
    Population in urban areas >5m
    """
    data = mathdf3.iloc[50:54,50:54]
    np.random.seed(123)
    replace_zero = lambda x: np.random.randint(1, 10) if x == 0 else x
    data = data.apply(lambda x: x.apply(replace_zero))
    ct = [  'Rural population living elev >5m\n(% of total population)',
           'Urban population living in elm5\n(% of total population)',
           'Population living elm5\n(% of total population)',
           'Population in urban areas >5m\n (% of total population)' ]
    corr = data.corr()
    corr = np.round(corr, decimals=2)
    heatmap = plt.imshow(corr, cmap='coolwarm')
    # add a colorbar to the plot
    plt.colorbar(heatmap)
    # Add the annotations to each square
    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            plt.text(j, i, corr.iloc[i, j], ha = 'center', va = 'center', 
                     color = 'white')
    plt.xticks(np.arange(0.5, 4.5),ct, rotation=90)
    plt.yticks(np.arange(0.5, 4.5),ct)
    # set the plot title
    plt.title('Heatmap of France')
    # show the plot
    plt.show()
    return

#Providing csv file path to the function _readcleandata
df,tr1 = _readcleandata('API_AG.LND.EL5M.RU.K2_DS2_en_csv_v2_4905462.csv')
df['Country Name'].unique()
mathdf1 = df.drop(["Country Name", "Country Code", "Indicator Name",
                 "Indicator Code"], axis=1)
mathdf1 = mathdf1.astype(float)
print("Describe function of Rural landarea where elevation below 5mts (sq.km)")
print(mathdf1['1990'].describe(), "\n")
print(mathdf1['2000'].describe(), "\n")
print(mathdf1['2015'].describe(), "\n")

framen,tr1 = _readcleandata('API_AG.LND.EL5M.RU.ZS_DS2_en_csv_v2_4905466.csv')
mathdf2 = framen.drop(['Country Name', 'Country Code', 'Indicator Name',
                     'Indicator Code'],axis=1)
mathdf2 = mathdf2.astype(float)
print("Describe function of urban land area where elevation is below 5 meters")
print(mathdf2['1990'].describe(), "\n")
print(mathdf2['2000'].describe(), "\n")
print(mathdf2['2015'].describe(), "\n")

framen1,tr2 = _readcleandata('API_AG.LND.EL5M.UR.ZS_DS2_en_csv_v2_4905389.csv')
mathdf3 = framen1.drop(["Country Name", "Country Code", "Indicator Name",
                      "Indicator Code"], axis=1)
mathdf3 = mathdf3.astype(float)

_heatmap_germany()
_ruralLandarea()
_urbanLandarea()
_heatmap_France()
