import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import DataFrame, Series
from matplotlib.ticker import MultipleLocator
import os
import sys
from datetime import datetime, timedelta
import csv

# Read CSV File

def readfile(year):
    df=pd.read_csv(f'/Users/sriram/Downloads/tennisanalytics/data/tennis_atp/atp_matches_{year}.csv')
    return df

#headers:tourney_id,tourney_name,surface,draw_size,tourney_level,tourney_date,match_num,winner_id,
#winner_seed,winner_entry,winner_name,winner_hand,winner_ht,winner_ioc,winner_age,loser_id,loser_seed,loser_entry,
#loser_name,loser_hand,loser_ht,loser_ioc,loser_age,score,best_of,round,minutes,w_ace,w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,
#w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced,winner_rank,
#winner_rank_points,loser_rank,loser_rank_points

def writefile(arr,filepath):
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(arr)
players=["Roger Federer","Novak Djokovic","Rafael Nadal"]
def headtohead():
    year=2004
    dict1={}
    data = {'Roger Federer': [0, 0, 0],
        'Novak Djokovic': [0, 0, 0],
        'Rafael Nadal': [0, 0, 0]}
    res = pd.DataFrame(data, index=['Roger Federer', 'Novak Djokovic', 'Rafael Nadal'])
    for j in players:
        for k in players:
            if j!=k:
                for i in range(2004,2023):
                    df=readfile(i)
                    df1=df[(df["winner_name"]==j)&(df["loser_name"]==k)]
                    res.at[j,k]+=df1.shape[0]               
        
    res.to_csv('/Users/sriram/Downloads/tennisanalytics/results/big3/headtohead.csv')



headtohead()