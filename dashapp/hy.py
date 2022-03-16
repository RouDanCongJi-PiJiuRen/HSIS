import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#pip install pandasql
from pandasql import sqldf

import streamlit as st
import plotly.express as px

def app():

    acc_data = pd.read_csv('../hsis-full/hsis-csv/wa13acc.csv')
    road_data = pd.read_csv('../hsis-full/hsis-csv/wa13road.csv')
    veh_data = pd.read_csv('../hsis-full/hsis-csv/wa13veh.csv')
    occ_data = pd.read_csv('../hsis-full/hsis-csv/wa13occ.csv')
    acc_veh_all = pd.read_csv('acc_veh_all.csv')
    acc_rd = pd.read_csv('acc_rd.csv')
    #图1
    plt.figure(figsize=(10, 8), dpi=80)
    m = np.array(acc_veh_all['spdlimit'])
    plt.hist(m, bins =np.arange(0.5,7.5), edgecolor = 'black', facecolor = 'red', alpha = 0.7)
    plt.title("SPEEDLIMIT AND CRASH NUMBER", size = 20)
    plt.xlabel('SPEEDLIMIT')
    plt.ylabel('THE NUMBER OF CRASH')
    plt.ylim(0)
    plt.xlim(0)
    # plt.show()


    fig1 = px.histogram(acc_veh_all['spdlimit'], x='spdlimit', labels='THE NUMBER OF CRASH', title="SPEEDLIMIT AND CRASH NUMBER", nbins=10)
    #st.plotly_chart(fig1)






    #图2
    plt.figure(figsize=(10, 8), dpi=80)
    m = np.array(acc_rd['AADT'])
    plt.hist(m, bins = 10, edgecolor = 'black', facecolor = 'red', alpha = 0.7)
    plt.title("AADT AND CRASH NUMBER", size = 20)
    plt.xlabel('AADT')
    plt.ylabel('THE NUMBER OF CRASH')
    plt.ylim(0)
    plt.xlim(0)
    #plt.show()

    fig2 = px.histogram(acc_rd['AADT'], x='AADT', labels='THE NUMBER OF CRASH', title="AADT AND CRASH NUMBER", nbins=10)
    #st.plotly_chart(fig2)

    #图3
    plt.figure(figsize=(10, 8), dpi=80)
    n = np.array(acc_rd['FUNC_CLS'])
    plt.hist(n, bins = 5,edgecolor = 'black', facecolor = 'red', alpha = 0.7)
    plt.title("FUNCTIONAL CLASSIFICATION OF ROAD AND CRASH NUMBER", size = 20)
    plt.xlabel('FUNCTIONAL CLASSIFICATION OF ROAD')
    plt.ylabel('THE NUMBER OF CRASH')
    plt.ylim(0)
    plt.xlim(0)
    #plt.show()

    fig3 = px.histogram(acc_rd['FUNC_CLS'], x='FUNC_CLS', labels='THE NUMBER OF CRASH', title="FUNCTIONAL CLASSIFICATION OF ROAD AND CRASH NUMBER", nbins=10)
    #st.plotly_chart(fig3)


    #图4
    plt.figure(figsize=(10, 8), dpi=80)
    p = np.array(acc_data['RDSURF'])   ###############speedlimit and the number of crash
    plt.hist(p, bins = 10,edgecolor = 'black', facecolor = 'red', alpha = 0.7)
    plt.title("RDSURF AND CRASH NUMBER", size = 20)
    plt.xlabel('RDSURF')
    plt.ylabel('THE NUMBER OF CRASH')
    plt.xticks([0, 1.00, 3.00, 4.00, 2.00], ['NOT STATED','DRY','SNOW','ICE','WET'])
    plt.ylim(0)
    plt.xlim(0)
    #plt.show()

    fig4 = px.histogram(acc_data['RDSURF'], x='RDSURF', labels='THE NUMBER OF CRASH', title="RDSURF AND CRASH NUMBER", nbins=10)
    #st.plotly_chart(fig4)

    acc_occ_data = acc_data.merge(occ_data, on = 'CASENO', how ='left')
    acc_occ_data.drop_duplicates(['CASENO'], inplace = True)




    #图5
    plt.figure(figsize=(10, 8), dpi=80)
    q = np.array(acc_occ_data['SEX'])   ###############speedlimit and the number of crash
    plt.hist(q, bins = 5, edgecolor = 'black', facecolor = 'red', alpha = 0.7)
    plt.title("SEX AND CRASH NUMBER", size = 5)
    plt.xlabel('SEX')
    plt.ylabel('THE NUMBER OF CRASH')
    plt.xticks([0, 1.00, 2.00], ['NOT STATED', 'MALE','FEMALE'])
    plt.ylim(0)
    plt.xlim(0)
    #plt.show()

    fig5 = px.histogram(acc_occ_data['SEX'], x='SEX', labels='THE NUMBER OF CRASH', title="SEX AND CRASH NUMBER", nbins=10)
    #st.plotly_chart(fig5)

    #图6
    plt.figure(figsize=(10, 8), dpi=80)
    r = np.array(acc_occ_data['AGE'])
    plt.hist(r, bins = 10, edgecolor = 'black', facecolor = 'red', alpha = 0.7)
    plt.title("AGE AND CRASH NUMBER", size = 20)
    plt.xlabel('AGE')
    plt.ylabel('THE NUMBER OF CRASH')
    plt.ylim(0)
    plt.xlim(0)
    #plt.show()


    fig6 = px.histogram(acc_occ_data['AGE'], x='AGE', labels='THE NUMBER OF CRASH', title="AGE AND CRASH NUMBER", nbins=10)
    #st.plotly_chart(fig6)


    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Figure 1")
        st.plotly_chart(fig1)
        st.subheader("Figure 4")
        st.plotly_chart(fig4)
    with c2:
        st.subheader("Figure 2")
        st.plotly_chart(fig2)
        st.subheader("Figure 5")
        st.plotly_chart(fig5)
    with c3:
        st.subheader("Figure 3")
        st.plotly_chart(fig3)
        st.subheader("Figure 6")
        st.plotly_chart(fig6)
