import pandas as pd
import streamlit as st
import numpy as np
import datetime
import matplotlib.pyplot as plt
import altair as alt
import settings
import filters

def app():
    data = filters.filterdata(settings.get_data(),settings.see_ph,
                                settings.ph,settings.see_yea,settings.yea,
                                settings.see_m,settings.m,settings.see_weekday,
                                settings.w,settings.see_hour,settings.h,settings.see_w,
                                settings.wea,settings.see_l,settings.li,settings.see_rdsurf,
                                settings.rdsurf,settings.see_pav,settings.pav,
                                settings.see_acctyp,settings.acctyp)
    col1, col2, col3, col4 = st.columns(4)
    ###weather bar chart
    x = data.copy()
    #x['TOT_KILL'] = x['TOT_KILL'] .astype(int)
    #x['TOT_PED'] = x['TOT_PED'].astype(int)
    #x = x[['weather', 'TOT_KILL', 'TOT_PED']].groupby(['weather']).agg(['sum', 'sum'])

    with col1:
        #st.title("Weather Conditions")
        st.subheader('Number of Crashes by Weather Type')
        crash_count = data.groupby(['weather']).count()
        crash_count.rename(columns={'FORM_REPT_NO': "Crashes"}, inplace=True)
        c = alt.Chart(crash_count.reset_index()).mark_bar().encode(
            x='Crashes:Q',
            y=alt.X('weather:N'),
            tooltip=['weather', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= crash_count['Crashes'].max(),
                alt.value('#000057'),  # which sets the bar orange.
                alt.value('#5252ff')  # And if it's not true it sets the bar steelblue.
            )).interactive()
        st.altair_chart(c)
       #st.write(alt.datum.Crashes)

        st.subheader('Number of Fatalities by Weather Type')
        fatal_count = data.groupby(['weather']).sum()
        fatal_count.rename(columns={'TOT_KILL': "Fatalities"}, inplace=True)
        c = alt.Chart(fatal_count.reset_index()).mark_bar().encode(
            x='Fatalities:Q',
            y=alt.X('weather:N'),
            tooltip=['weather', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= fatal_count['Fatalities'].max(),
                alt.value('#651a1a'),     # which sets the bar orange.
                alt.value('#0000a8')   # And if it's not true it sets the bar steelblue.
                )).interactive()
        st.altair_chart(c)
        #st.write(alt.datum.Fatalities)

    with col2:
        #st.title ("Light Conditions")
        st.subheader('Number of Crashes by Light Conditions')
        crash_count = data.groupby(['LIGHT']).count()
        crash_count.rename(columns={'FORM_REPT_NO': "Crashes"}, inplace=True)
        c = alt.Chart(crash_count.reset_index()).mark_bar().encode(
            x='Crashes:Q',
            y=alt.X('LIGHT:N'),
            tooltip=['LIGHT', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= crash_count['Crashes'].max(),
                alt.value('#000057'),  # which sets the bar orange.
                alt.value('#5252ff')  # And if it's not true it sets the bar steelblue.
            )).interactive()
        st.altair_chart(c)
        #st.write(alt.datum.Crashes)

        st.subheader('Number of Fatalities by Light Conditions')
        fatal_count = data.groupby(['LIGHT']).sum()
        fatal_count.rename(columns={'TOT_KILL': "Fatalities"}, inplace=True)
        c = alt.Chart(fatal_count.reset_index()).mark_bar().encode(
            x='Fatalities:Q',
            y=alt.X('LIGHT:N'),
            tooltip=['LIGHT', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= fatal_count['Fatalities'].max(),
                alt.value('#651a1a'),  # which sets the bar orange.
                alt.value('#0000a8')  # And if it's not true it sets the bar steelblue.
            )).interactive()
        st.altair_chart(c)
        #st.write(alt.datum.Fatalities)
    with col3:
        st.subheader('Number of Crashes by Road Surface Conditions')
        crash_count = data.groupby(['RDSURF']).count()
        crash_count.rename(columns={'FORM_REPT_NO': "Crashes"}, inplace=True)
        c = alt.Chart(crash_count.reset_index()).mark_bar().encode(
            x='Crashes:Q',
            y=alt.X('RDSURF:N'),
            tooltip=['RDSURF', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= crash_count['Crashes'].max(),
                alt.value('#000057'),  # which sets the bar orange.
                alt.value('#5252ff')  # And if it's not true it sets the bar steelblue.
            )).interactive()
        st.altair_chart(c)
        #st.write(alt.datum.Crashes)

        st.subheader('Number of Fatalities by Road Surface Conditions')
        fatal_count = data.groupby(['RDSURF']).sum()
        fatal_count.rename(columns={'TOT_KILL': "Fatalities"}, inplace=True)
        c = alt.Chart(fatal_count.reset_index()).mark_bar().encode(
            x='Fatalities:Q',
            y=alt.X('RDSURF:N'),
            tooltip=['RDSURF', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= fatal_count['Fatalities'].max(),
                alt.value('#651a1a'),  # which sets the bar orange.
                alt.value('#0000a8')  # And if it's not true it sets the bar steelblue.
            )).interactive()
        st.altair_chart(c)
        #st.write(alt.datum.Fatalities)
    with col4:
        st.subheader('Number of Crashes by Pavement Type')
        crash_count = data.groupby(['SURF_TYP']).count()
        crash_count.rename(columns={'FORM_REPT_NO': "Crashes"}, inplace=True)
        c = alt.Chart(crash_count.reset_index()).mark_bar().encode(
            x='Crashes:Q',
            y=alt.X('SURF_TYP:N'),
            tooltip=['SURF_TYP', 'Crashes'],
            color=alt.condition(
                alt.datum.Crashes >= crash_count['Crashes'].max(),
                alt.value('#000057'),  # which sets the bar orange.
                alt.value('#5252ff')  # And if it's not true it sets the bar steelblue.
            )).interactive()
        st.altair_chart(c)
        #st.write(alt.datum.Crashes)

        st.subheader('Number of Fatalities by Pavement Type')
        fatal_count = data.groupby(['SURF_TYP']).sum()
        fatal_count.rename(columns={'TOT_KILL': "Fatalities"}, inplace=True)
        c = alt.Chart(fatal_count.reset_index()).mark_bar().encode(
            x='Fatalities:Q',
            y=alt.X('SURF_TYP:N'),
            tooltip=['SURF_TYP', 'Fatalities'],
            color=alt.condition(
                alt.datum.Fatalities >= fatal_count['Fatalities'].max(),
                alt.value('#651a1a'),  # which sets the bar orange.
                alt.value('#0000a8')  # And if it's not true it sets the bar steelblue.
            )).interactive()
        st.altair_chart(c)
        #st.write(alt.datum.Fatalities)




