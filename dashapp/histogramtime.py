import pandas as pd
import streamlit as st
import numpy as np
import datetime
import matplotlib.pyplot as plt
import altair as alt
import settings

def app():
    
    data = filters.filterdata(settings.get_data(),settings.see_ph,
                                settings.ph,settings.see_yea,settings.yea,
                                settings.see_m,settings.m,settings.see_weekday,
                                settings.w,settings.see_hour,settings.h,settings.see_w,
                                settings.wea,settings.see_l,settings.li,settings.see_rdsurf,
                                settings.rdsurf,settings.see_pav,settings.pav,
                                settings.see_acctyp,settings.acctyp)
    # data['Hour'] = data['TIME'].astype(str).str[-4:-2]
    # data['Minute'] = data['TIME'].astype(str).str[-2:]
    # data.rename(columns={"DAYMTH": "Day", "MONTH": "Month", "ACCYR": "Year"}, inplace=True)
    # data['Datetime'] = pd.to_datetime(data[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    # data['Weekday'] = data['Datetime'].dt.weekday
    # data['Hourly'] = data['Datetime'].dt.hour
    # data['Monthly'] = data['Datetime'].dt.month
    # data['Yearly'] = data['Datetime'].dt.year
    #st.set_page_config(layout="centered")
    #st.set_page_config(layout="wide")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader('Number of crashes by Year')
        year_df = data.groupby('Yearly').count()
        year_df.rename(columns={'FORM_REPT_NO': "Crashes"}, inplace=True)
        c = alt.Chart(year_df.reset_index()).mark_bar().encode(
            x=alt.X('Yearly:N'),
            y='Crashes:Q',
            tooltip=['Yearly', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= year_df['Crashes'].max(),
                alt.value('#000057'),     # which sets the bar orange.
                alt.value('#5252ff')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Crashes)

    with col2:
        #st.subheader('Number of crashes by year')
        #hour_to_filter = st.slider('time', 0, 23, 17)
        #hist_values = np.histogram(data['Datetime'].dt.year, bins=5, range=(2013, 2017))["Number of Crash in each year"]
        #st.bar_chart(hist_values)

        #st.subheader('Number of crashes by month')
        #hour_to_filter = st.slider('time', 0, 23, 17)
        #hist_values = np.histogram(data['Datetime'].dt.month, bins=12, range=(1, 12))[0]
        #st.bar_chart(hist_values)

        st.subheader('Number of crashes by Month')
        month_df = data.groupby('Monthly').count()
        monthlist = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        month_df.rename(index={i: monthlist[i] for i in range(1,13)},columns = {'FORM_REPT_NO':"Crashes"},inplace= True)
        c = alt.Chart(month_df.reset_index()).mark_bar().encode(
            x=alt.X('Monthly:N',sort=monthlist),
            y='Crashes:Q',
            tooltip=['Monthly', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= month_df['Crashes'].max(),
                alt.value('#000057'),     # which sets the bar orange.
                alt.value('#5252ff')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Crashes)


    with col3:
        #st.subheader('Number of crashes by day')
        #hour_to_filter = st.slider('time', 0, 23, 17)
        #hist_values = np.histogram(data['Datetime'].dt.weekday, bins=7, range=(1, 7))[0]
        #st.bar_chart(hist_values)

        st.subheader('Number of crashes by day')
        week_df = data.groupby('Weekday').count()
        weekdaylist = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        week_df.rename(index={i: weekdaylist[i] for i in range(7)},columns = {'FORM_REPT_NO':"Crashes"},inplace= True)
        c = alt.Chart(week_df.reset_index()).mark_bar().encode(
            x=alt.X('Weekday:N',sort=weekdaylist),
            y='Crashes:Q',
            tooltip=['Weekday', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= week_df['Crashes'].max(),
                alt.value('#000057'),     # which sets the bar orange.
                alt.value('#5252ff')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Crashes)

    with col4:
        #st.subheader('Number of crashes by hour')
        #hour_to_filter = st.slider('time', 0, 23, 17)
        #hist_values = np.histogram(data['Datetime'].dt.hour, bins=24, range=(0, 24))[0]
        #st.bar_chart(hist_values)
        ####plotting histogram
        st.subheader('Number of crashes by Hour')
        hour_df = data.groupby('Hourly').count()
        hourlist = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM',
                    '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12AM']
        hour_df.rename(index={i: hourlist[i] for i in range(24)}, columns={'FORM_REPT_NO': "Crashes"}, inplace=True)
        c = alt.Chart(hour_df.reset_index()).mark_bar().encode(
            x=alt.X('Hourly:N',sort=hourlist),
            y='Crashes:Q',
            tooltip=['Hourly', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= hour_df['Crashes'].max(),
                alt.value('#000057'),     # which sets the bar orange.
                alt.value('#5252ff')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Crashes)



    with col1:
        st.subheader('Number of Fatalities by Year')
        year_df = data.groupby('Yearly').sum()
        year_df.rename(columns={'TOT_KILL': "Fatalities"}, inplace=True)
        c = alt.Chart(year_df.reset_index()).mark_bar().encode(
            x=alt.X('Yearly:N'),
            y='Fatalities:Q',
            tooltip=['Yearly', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= year_df['Fatalities'].max(),
                alt.value('#2e0000'),     # which sets the bar orange.
                alt.value('#ff5252')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Fatalities)

    with col2:
        st.subheader('Number of Fatalities by Month')
        month_df = data.groupby('Monthly').sum()
        monthlist = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        month_df.rename(index={i: monthlist[i] for i in range(1,13)},columns = {'TOT_KILL':"Fatalities"},inplace= True)
        c = alt.Chart(month_df.reset_index()).mark_bar().encode(
            x=alt.X('Monthly:N',sort=monthlist),
            y='Fatalities:Q',
            tooltip=['Monthly', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= month_df['Fatalities'].max(),
                alt.value('#2e0000'),     # which sets the bar orange.
                alt.value('#ff5252')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Fatalities)

    with col3:
        #st.subheader('Number of crashes by day')
        #hour_to_filter = st.slider('time', 0, 23, 17)
        #hist_values = np.histogram(data['Datetime'].dt.weekday, bins=7, range=(1, 7))[0]
        #st.bar_chart(hist_values)

        st.subheader('Number of Fatalities by day')
        week_df = data.groupby('Weekday').sum()
        weekdaylist = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        week_df.rename(index={i: weekdaylist[i] for i in range(7)},columns = {'TOT_KILL':"Fatalities"},inplace= True)
        c = alt.Chart(week_df.reset_index()).mark_bar().encode(
            x=alt.X('Weekday:N',sort=weekdaylist),
            y='Fatalities:Q',
            tooltip=['Weekday', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= week_df['Fatalities'].max(),
                alt.value('#2e0000'),     # which sets the bar orange.
                alt.value('#ff5252')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Fatalities)

    with col4:
        #st.subheader('Number of crashes by hour')
        #hour_to_filter = st.slider('time', 0, 23, 17)
        #hist_values = np.histogram(data['Datetime'].dt.hour, bins=24, range=(0, 24))[0]
        #st.bar_chart(hist_values)
        ####plotting histogram
        st.subheader('Number of Fatalities by Hour')
        hour_df = data.groupby('Hourly').sum()
        hourlist = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM',
                    '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12AM']
        hour_df.rename(index={i: hourlist[i] for i in range(24)}, columns={'TOT_KILL': "Fatalities"}, inplace=True)
        c = alt.Chart(hour_df.reset_index()).mark_bar().encode(
            x=alt.X('Hourly:N',sort=hourlist),
            y='Fatalities:Q',
            tooltip=['Hourly', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= hour_df['Fatalities'].max(),
                alt.value('#2e0000'),     # which sets the bar orange.
                alt.value('#ff5252')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        st.write(alt.datum.Fatalities)



