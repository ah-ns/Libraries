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
    


def main():
    # Unchanged DataFrame from csv file
    df = pd.read_csv("C:/Users/ahns/Code/Test Programs/datasets/flights.csv")
    print(df)


    indices(df)




main()