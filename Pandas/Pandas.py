import pandas as pd
import numpy as np



def indices(df:pd.DataFrame):
    """ Test indices syntax

    :param pd.DataFrame df: Unchanged DataFrame
    """
    # EX 1
    df_ind = df.set_index("Pivot Label")
    print(df_ind)
    # Pivot table using .pivot_table
    print((df_ind.loc["Antwerp (EBAW)"]).pivot_table(index=["Pivot Label", "YEAR"], values="FLT_TOT_1"))

    '''
    # EX 2
    df_ind_2 = df.set_index(["YEAR", "STATE_NAME"])
    print(df_ind_2)
    # List of tuples
    rows_to_keep = [("2019", "Belgium"), ("2020", "Belgium")]
    # Subset for rows to keep NOTE: does not work for rows_to_keep as it should
    print(df_ind_2.loc[("2022", "Belgium")])
    '''

    # EX 3
    # Add a year column to the dataframe
    df["year"] = df["date"].dt.year

    # Pivot avg_flights_c by country and city vs year
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


def main():
    # Unchanged DataFrame from csv file
    df = pd.read_csv("C:/Users/ahns/Code/Test Programs/datasets/flights.csv")
    print(df)


    indices(df)




main()