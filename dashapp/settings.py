import pandas as pd
import streamlit as st

#@st.cache
def init():
    #global df,cof
    global see_ph,ph,see_yea,yea,see_m,m,see_weekday,w,see_hour,h,see_w,wea,see_l,li,see_rdsurf,rdsurf,see_pav,pav,see_acctyp,acctyp

@st.cache(allow_output_mutation=True)
def get_data():
    # url='https://drive.google.com/file/d/1TO8iTr_dCE3ZqGTvJg8ibRvq2RRb9dOx/view?usp=sharing'
    # url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    # df = pd.read_csv(url)   
    df = pd.read_csv('appnd_acc_rd.csv')

    ###########################################################
    ### initial manipulations
    df['Hour'] = df['TIME'].astype(str).str[-4:-2]
    df['Minute'] = df['TIME'].astype(str).str[-2:]
    df.rename(columns={"DAYMTH": "Day", "MONTH": "Month", "ACCYR": "Year"}, inplace=True)
    df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    df['Weekday'] = df['Datetime'].dt.weekday
    df['Hourly'] = df['Datetime'].dt.hour
    df['Monthly'] = df['Datetime'].dt.month
    df['Yearly'] = df['Datetime'].dt.year

    ###convert  different variables into categories
    ##weather
    # df['weather']= df['weather'].astype(int)
    df.replace({'weather': {0: "Unknown", 1: "Clear or Partly Cloudy", 2: "Overcast", 3: "Raining",
                                4: "Snowing", 5: "Fog/Smog/Smoke", 6: "Sleet/Hail/Freezing Rain", 7: "Severe Crosswind",
                                8: "Blowing Sand or Dirt or Snow", 9: "Other", 10: "Foggy",
                                '0': "Unknown", '1': "Clear or Partly Cloudy", '2': "Overcast", '3': "Raining",
                                '4': "Snowing", '5': "Fog/Smog/Smoke", '6': "Sleet/Hail/Freezing Rain",
                                '7': "Severe Crosswind",
                                '8': "Blowing Sand or Dirt or Snow", '9': "Other",
                                '00': "Unknown", '01': "Clear or Partly Cloudy", '02': "Overcast", '03': "Raining",
                                '04': "Snowing", '05': "Fog/Smog/Smoke", '06': "Sleet/Hail/Freezing Rain",
                                '07': "Severe Crosswind",
                                '08': "Blowing Sand or Dirt or Snow", '09': "Other", '10': "Foggy"
                                }}, inplace=True)
    ##light
    df.replace({'LIGHT': {1: "Daylight", 2: "Dawn or dusk", 3: "Dawn or dusk", 4: "Dark, Street Lights On",
                            5: "Dark street", 6: "Dark street", 7: "Other", 9: "Unknown"}}, inplace=True)
    ##road surface temporary
    df.replace({'RDSURF': {1: "Dry", 2: "Wet", 3: "Snow/Slush", 4: "Snow/Slush", 5: "Sand/Mud/Dirt",
                                6: "Oil", 7: "Standing Water", 8: "Other", 9: "Unknown"}}, inplace=True)
    #### road surface permanent
    df.replace({'SURF_TYP': {'A': "Asphalt", 'B': "Bituminous", 'G': "Gravel", 'O': "Other",
                                'P': "Portland Concrete Cement", 'S': "Soil"}}, inplace=True)
    #ACCTYPE
    df.replace({'ACCTYPE': {i: "Vehicle to Vehicle" for i in range(18)}}, inplace=True)
    
    return df

