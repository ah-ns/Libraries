import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
import json

def encode_continent(df:pd.DataFrame) -> pd.DataFrame:
    """ Sorts each flight by continent and one-hot encodes

    :param pd.DataFrame df: original dataframe
    :return:                new dataframe
    :rtype:                 pd.DataFrame
    """
    raise NotImplementedError()
    continents = 
    
    df['CONTINENT'] = df

def mean_flights(df:pd.DataFrame) -> pd.DataFrame:
    """ Creates a mean column for flight counts
    
    :param pd.DataFrame df: original dataframe
    :return:                new dataframe
    :rtype:                 pd.DataFrame
    """


def main():
    df = pd.read_csv("C:/Users/ahns/Code/Test Programs/datasets/flights.csv")
    
    df.columns = [column.title() for column in df.columns]
    print(df)

    df = encode_continent(df)
    df = mean_flights(df)



main()