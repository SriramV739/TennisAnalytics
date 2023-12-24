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

# Read CSV File
df=pd.read_csv('/Users/sriram/Downloads/tennisanalytics/data/atp_matches_2022.csv',nrows=1000)

fout=open("winners.out","w")

#headers:tourney_id,tourney_name,surface,draw_size,tourney_level,tourney_date,match_num,winner_id,
#winner_seed,winner_entry,winner_name,winner_hand,winner_ht,winner_ioc,winner_age,loser_id,loser_seed,loser_entry,
#loser_name,loser_hand,loser_ht,loser_ioc,loser_age,score,best_of,round,minutes,w_ace,w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,
#w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced,winner_rank,
#winner_rank_points,loser_rank,loser_rank_points

df1=df[df['round']=='F']
subset=['tourney_name','winner_name','loser_name']
df1=df1[subset]
df1.to_csv('winners.csv')
