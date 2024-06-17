import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def indices(df:pd.DataFrame):
    """ Test indices syntax

    :param pd.DataFrame df: Unchanged DataFrame
    """
    #''' EX 1
    df_ind = df.set_index("Pivot Label")
    print(df_ind)
    # Pivot table using .pivot_table
    print((df_ind.loc["Antwerp (EBAW)"]).pivot_table(index=["Pivot Label", "YEAR"], values="FLT_TOT_1"))
    # '''


    #''' EX 2
    df_ind_2 = df.set_index(["STATE_NAME", "YEAR"])
    print(df_ind_2)
    # List of tuples
    rows_to_keep = [("Belgium", "2019"), ("Belgium", "2020")]
    # Subset for rows to keep NOTE: does not work for rows_to_keep as it should
    print(df_ind_2.loc[rows_to_keep])
    # '''


    #''' EX 3
    # Add a year column to the dataframe (If has yyyy-mm-dd format)
    #df["year"] = df["date"].dt.year
    df["year"] = df["date"].dt.year

    # Pivot flights by country and city vs year
    flights_by_country_city_vs_year = df.pivot_table(values="", index=["country", "city"], columns="year")

    # See the result
    print(flights_by_country_city_vs_year)
    # Get the worldwide mean flights by year
    mean_flights_by_year = flights_by_country_city_vs_year.mean()

    # Filter for the year that had the highest mean flights
    print(mean_flights_by_year[mean_flights_by_year == mean_flights_by_year.max()])

    # Get the mean flights by city
    mean_flights_by_city = flights_by_country_city_vs_year.mean(axis="columns")

    # Filter for the city that had the lowest mean flights
    print(mean_flights_by_city[mean_flights_by_city == mean_flights_by_city.min()])
    # '''



def visual(df:pd.DataFrame):
    #''' EX 1
    # Subset of state Belgium's flight total with 20 bins
    df[df["STATE_NAME"] == "Belgium"]["FLT_TOT_1"].hist(alpha=0.5, bins=20)

    # Subset of state Netherlands' flight total with 20 bins
    df[df["STATE_NAME"] == "Netherlands"]["FLT_TOT_1"].hist(alpha=0.5, bins=20)

    # Add a legend
    plt.legend(["Belgium", "Netherlands"])
    # '''


    #''' EX 2
    # From previous step
    cols_with_missing = ["FLT_ARR_1", "FLT_DEP_1", "FLT_TOT_1"]
    df[cols_with_missing].hist()
    plt.show()

    # Fill in missing values with 0
    avocados_filled = df.fillna(0)

    # Create histograms of the filled columns
    avocados_filled[cols_with_missing].hist()
    # '''


    plt.show()



def main():
    # Unchanged DataFrame from csv file
    df = pd.read_csv("C:/Users/ahns/Code/Test Programs/datasets/flights.csv")
    print(df)


    indices(df)


    visual(df)




main()