import streamlit as st 
import settings
import pandas as pd
import numpy as np
import datetime
import filters

def filterdata(data,see_ph,ph,see_yea,yea,see_m,m,see_weekday,w,
                    see_hour,h,see_w,wea,see_l,li,see_rdsurf,rdsurf,
                    see_pav,pav,see_acctyp,acctyp):
    if see_yea:
        data = data.loc[data['Yearly'] == yea]

    
    if see_m:
        data = data.loc[data['Monthly'] == m]
       
    
    if see_weekday:
        data = data.loc[data['Weekday'] == w]


    if see_hour:
        data = data.loc[data['Hourly'] == h]
        #st.header("Hour Filter is Applied")


    if see_ph:
        if ph == "Peak hour":
            data = data.loc[(data['Datetime'].dt.time >= datetime.time(7, 00, 00)) &
                            (data['Datetime'].dt.time <= datetime.time(9, 00, 00)) |
                            (data['Datetime'].dt.time >= datetime.time(17, 00, 00)) &
                            (data['Datetime'].dt.time <= datetime.time(19, 00, 00))]

        else:
            data = data.loc[~((data['Datetime'].dt.time >= datetime.time(7, 00, 00)) &
                              (data['Datetime'].dt.time <= datetime.time(9, 00, 00)) |
                              (data['Datetime'].dt.time >= datetime.time(17, 00, 00)) &
                              (data['Datetime'].dt.time <= datetime.time(19, 00, 00)))]


    if see_w:
        data = data.loc[data['weather'] == wea]



    if see_l:
        data = data.loc[data['LIGHT'] == li]


    if see_rdsurf:
        data = data.loc[data['RDSURF'] == rdsurf]


    if see_pav:  
        data = data.loc[data['SURF_TYP'] == pav]

    if see_acctyp:
        data = data.loc[data['ACCTYPE'] == acctyp]


    return data


def applyfilter():

    data = settings.get_data()
    see_ph,ph,see_yea,yea,see_m,m,see_weekday,w,see_hour,h,see_w,wea,see_l,li,see_rdsurf,rdsurf,see_pav,pav,see_acctyp,acctyp = [0]*20
 
    ###########################################################
    ###filter widgets
    #cof = st.sidebar.radio("Crashes or Fatalities", ('Crashes', 'Fatalities'))
    
    st.sidebar.subheader("Choose Time based Filters")
    see_yea = st.sidebar.checkbox("Select Year")
    if see_yea:
        yea = st.sidebar.radio("Year", (2013, 2014, 2015, 2016, 2017))
        #data = data.loc[data['Yearly'] == yea]
        st.header("Year Filter is Applied")
    
    see_m = st.sidebar.checkbox("Select Month")
    if see_m:
        m = st.sidebar.radio("Month", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
        #data = data.loc[data['Monthly'] == m]
        #st.header("Monthly filter applied")
        st.header("Month Filter is Applied")
    
    see_weekday = st.sidebar.checkbox("Select Weekday")
    if see_weekday:
        w = st.sidebar.radio("weekday, 0 is monday and 6 is sunday", (0, 1, 2, 3, 4, 5, 6))
        #data = data.loc[data['Weekday'] == w]
        #st.header("Weekly filter applied")
        st.header("Weekday Filter is Applied")

    see_hour = st.sidebar.checkbox("Select Hour")
    if see_hour:
        h = st.sidebar.slider('time', 0, 23, 17)
        #data = data.loc[data['Hourly'] == h]
        st.header("Hourly filter applied")
        #st.header("Hour Filter is Applied")

    st.sidebar.subheader("Choose Condition based Filters")
    see_ph = st.sidebar.checkbox('Apply peak hour filter')
    if see_ph:
        ph = st.sidebar.radio("Peak vs Off-peak", ("Peak hour", "Off-peak hour"))
        if ph == "Peak hour":
            #data = data.loc[(data['Datetime'].dt.time >= datetime.time(7, 00, 00)) &
                            # (data['Datetime'].dt.time <= datetime.time(9, 00, 00)) |
                            # (data['Datetime'].dt.time >= datetime.time(17, 00, 00)) &
                            # (data['Datetime'].dt.time <= datetime.time(19, 00, 00))]
            st.header("Office Peak Hour filter applied")
        else:
            #data = data.loc[~((data['Datetime'].dt.time >= datetime.time(7, 00, 00)) &
                            #   (data['Datetime'].dt.time <= datetime.time(9, 00, 00)) |
                            #   (data['Datetime'].dt.time >= datetime.time(17, 00, 00)) &
                            #   (data['Datetime'].dt.time <= datetime.time(19, 00, 00)))]
            st.header("Off peak hour filter applied")

    see_w = st.sidebar.checkbox('Apply weather filter')
    if see_w:
        wea = st.sidebar.radio("Weather", ('Clear or Partly Cloudy', 'Raining', 
                                    'Snowing', 'Fog/Smog/Smoke','Sleet/Hail/Freezing Rain'))
        #data = data.loc[data['weather'] == wea]
        st.header("Weather filter applied")

    see_l = st.sidebar.checkbox('Apply lighting filter')
    if see_l:
        li = st.sidebar.radio("Lighting condition",
                  ("Dawn or dusk", "Dark street", "Dark, Street Lights On", "Daylight"))
        #data = data.loc[data['LIGHT'] == li]
        st.header("Lighting Conditions filter applied")

    see_rdsurf = st.sidebar.checkbox("Apply Road Surface (wet/dry) filter")
    if see_rdsurf:
        rdsurf = st.sidebar.radio("Surface", ("Dry", "Wet", "Snow/Slush", "Sand/Mud/Dirt", "Standing Water"))
        #data = data.loc[data['RDSURF'] == rdsurf]
        st.header("Temporary road surface condition filter applied")

    see_pav = st.sidebar.checkbox("Apply Road Pavement Type filter")
    if see_pav:
        pav = st.sidebar.radio("Pavement",
                        ("Asphalt", "Bituminous", "Gravel", "Other", "Portland Concrete Cement", "Soil"))
        #data = data.loc[data['SURF_TYP'] == pav]
        st.header("Pavement type filter applied")

    see_acctyp = st.sidebar.checkbox("Select for Vehicle to Vehicle Collision")
    if see_acctyp:
        acctyp = st.sidebar.radio("Vehicle only", ("Vehicle to Vehicle"))
        #data = data.loc[data['ACCTYPE'] == acctyp]
        st.header("Only Vehicle to Vehicle Collision filter applied")

    # if see_trfcntl:
    #    data = data.loc[data['TRF_CNTL'] == trfcntl]

    
    settings.see_ph,settings.ph,settings.see_yea,settings.yea,settings.see_m,settings.m,settings.see_weekday,settings.w,settings.see_hour,settings.h,settings.see_w,settings.wea,settings.see_l,settings.li,settings.see_rdsurf,settings.rdsurf,settings.see_pav,settings.pav,settings.see_acctyp,settings.acctyp = see_ph,ph,see_yea,yea,see_m,m,see_weekday,w,see_hour,h,see_w,wea,see_l,li,see_rdsurf,rdsurf,see_pav,pav,see_acctyp,acctyp