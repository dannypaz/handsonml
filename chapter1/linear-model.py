import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

def prepare_country_stats(_bli, _gdp):
    """ Prepare stats to be used in regression """
    return print("yo")

def run_model():
    """ Method to run linear model against BLI and GDP data """

    # Stats grabbed from http://stats.oecd.org/index.aspx?DataSetCode=BLI
    # (Organization for Economic Co-op and Development)
    better_life_index = pd.read_csv("./better-life-index-2017.csv", thousands=',')

    # GDP stats grabbed from www.imf.org
    # (International Monetary Fund)
    gdp_per_capita = pd.read_csv(
        "./gdp-per-capita-2015.csv",
        thousands=',',
        delimiter='\t',
        encoding='latin1',
        na_values="n/a"
    )

    # TODO: Implement preparation function
    country_stats = prepare_country_stats(better_life_index, gdp_per_capita)
    x_gdp = np.c_[country_stats["GDP per capita"]]
    y_ls = np.c_[country_stats["Life satisfaction"]]

    # create plot to visualize data
    country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
    plt.show()

    lin_reg_model = sklearn.linear_model.LinearRegression()
    lin_reg_model.fit(x_gdp, y_ls)

    x_new = [[22587]] # Cyprus GDP per capita
    return print(lin_reg_model.predict(x_new))

run_model()
