
import os.path as P
import os
import yaml

import pandas as pd
import numpy as np

project_dir = '/Users/doayakut/Desktop/third'
immutable_dir = P.join(project_dir, 'data', 'immutable')

def load_csv(fname: str) -> object:
    df = pd.read_csv(P.join(immutable_dir, fname))
    
    print(fname[:-4], ':')
    print('  shape:', df.shape)
    print('  columns:', df.dtypes)
    print('  first 3 rows:', df.head(3))
    
    return df

def check_field_types(df1, df2):
    print('\n\n')
    fields = {}
    for col in df1.columns: 
        fields[col] = (df1[col].dtype, None)
    for col in df2.columns: 
        if col not in fields:
            fields[col] = (None, df2[col].dtype)
        else:
            fields[col] = (df1[col].dtype, df2[col].dtype)
    for k, v in fields.items():
        print(k, v[0], v[1])
    
    print('\n\n')
        

def unify_reviewer_data():
    """
    The 4 datasets needed to be merged are:
    - yelpHotelNewData_reviewer.csv
    - yelpHotelData_reviewer.csv
    - yelpResNewData_reviewer.csv
    - yelpResData_reviewer.csv

    Common key is "reviewerID"
    """
    
    

def unify_seeded_datasets():
    # yelpHotelData_hotel.csv
    # yelpHotelData_review.csv
    # yelpHotelData_reviewer.csv
    # yelpHotelNewData_review.csv
    # yelpHotelNewData_reviewer.csv

    yelpHotelData_hotel = load_csv('yelpHotelData_hotel.csv')
    yelpHotelData_review = load_csv('yelpHotelData_review.csv')
    yelpHotelData_reviewer = load_csv('yelpHotelData_reviewer.csv')
    yelpHotelNewData_review = load_csv('yelpHotelNewData_review.csv')
    yelpHotelNewData_reviewer = load_csv('yelpHotelNewData_reviewer.csv')

    # unify_reviewer_data()
    

    
    


if __name__ == "__main__":
    unify_seeded_datasets()