import settings
import filters
import json  # library to handle JSON files
import requests  # library to handle requests
import folium  # map rendering library
import streamlit as st  # creating an app
import pandas as pd
from streamlit_folium import folium_static
import pandas as pd
import numpy as np
import datetime
import branca.colormap as cmp



def app():
    json_dir = 'data/wa.json'
    polygon_coor = json.load(open(json_dir))
    
    data_all = filters.filterdata(settings.get_data(),settings.see_ph,
                                settings.ph,settings.see_yea,settings.yea,
                                settings.see_m,settings.m,settings.see_weekday,
                                settings.w,settings.see_hour,settings.h,settings.see_w,
                                settings.wea,settings.see_l,settings.li,settings.see_rdsurf,
                                settings.rdsurf,settings.see_pav,settings.pav,
                                settings.see_acctyp,settings.acctyp)
    
    Countylist = []
    with open(json_dir) as json_file:
        data = json.load(json_file)
        for c in data['features']:
            Countylist.append(c['properties']['NAME'])

    m = folium.Map(location=[47, -122], tiles='wa counties', name="Light Map",attr="My Data attribution", zoom_start=30)
    #m = folium.map(location = [46.48, -122.5], tiles='CartoDB positron', name="Light Map", zoom_start=5, attr="My Data attribution")

    # col1, col2= st.columns(2)
    # with col1:
    #     cof = st.radio("Crashes or Fatalities",('Crashes', 'Fatalities'))

    data_all['County Name'] = data_all['County Name'].str.strip()


    #crash
    data_count = data_all.groupby(['County Name']).count().reset_index()
    data_count['Crash Count'] = data_count.loc[:,'FORM_REPT_NO']
    data_count = data_count[['County Name','Crash Count']]
    #data_count['sqrt_count'] = data_count['Crash Count']**(1/2)

    if not data_count['Crash Count'].empty:
        county_with_highest_crash = data_count.loc[ data_count['Crash Count'] == data_count['Crash Count'].max(),'County Name'].values[0]
    else:
        county_with_highest_crash = None

    missingc = list(set(Countylist) - set(data_all['County Name'].to_list()))
    for i in missingc:
        missingd = pd.DataFrame([[i,0]], columns=['County Name','Crash Count'])
        data_count = data_count.append(missingd,ignore_index = True)

    crashes_dict = data_count.set_index('County Name')['Crash Count']

    #fatalities
    kill_count = data_all.groupby(['County Name']).sum()['TOT_KILL'].reset_index()

    missingc = list(set(Countylist) - set(kill_count['County Name'].to_list()))

    for i in missingc:
        missingd = pd.DataFrame([[i,0]], columns=['County Name','TOT_KILL'])
        kill_count = kill_count.append(missingd,ignore_index = True)

    kill_dict = kill_count.set_index('County Name')['TOT_KILL']
    kill_count = kill_count.append(missingd,ignore_index = True)
    
    if not kill_count['TOT_KILL'].empty:
        county_with_highest_fatalities = kill_count.loc[kill_count['TOT_KILL'] == kill_count['TOT_KILL'].max(),'County Name'].values[0]
    else:
        county_with_highest_fatalities = None
    
    linear_c = cmp.LinearColormap(
        colors=['yellow','red','purple'], index=data_count['Crash Count'].quantile([0, .75,1]).round().to_list(),vmin=0,vmax=data_count['Crash Count'].max() ,
        #colors=['yellow','red','purple'], index= [0,data_count['Crash Count'].max()/2,data_count['Crash Count'].max()],vmin=0,vmax=data_count['Crash Count'].max() ,
        caption='Color Scale for Map' #Caption for Color scale or Legend
    )

    linear_k =cmp.LinearColormap(
        colors=['pink','red','black'], index= kill_count['TOT_KILL'].quantile([0, .75,1]).round().to_list(),vmin=0,vmax=kill_count['TOT_KILL'].max(),
        caption='Color Scale for Map' #Caption for Color scale or Legend
    )

    m = folium.Map(location=[47, -122], tiles='cartodb positron', zoom_start=5.5)
    folium.GeoJson(json_dir,
                name="NAME", popup=folium.features.GeoJsonPopup(fields=["NAME","COUNTY"])).add_to(m)

    #if cof == 'Crashes':
    st.subheader("Number of crashes in each county")
    cp = folium.GeoJson(json_dir,
                style_function=lambda feature: {
                        'fillColor': linear_c(crashes_dict[feature['properties']['NAME']]),
                        'fillOpacity':0.8,
                        'color': 'black',     #border color for the color fills
                        'weight': 1,          #how thick the border has to be
                        'dashArray': '5, 3'  #dashed lines length,space between them
                    }).add_to(m)
    linear_c.add_to(m)
    for s in cp.data['features']:
        ct = data_count.loc[data_count['County Name'] == s['properties']['NAME'], 'Crash Count'].astype(float).values[0]
        s['properties']['Crashes'] = ct
    folium.GeoJsonTooltip(['NAME','Crashes']).add_to(cp)  
    folium.LayerControl().add_to(m)
    d1 = "<p style='font-size:14px;font-weight:bold;'><span style='font-family:Impact, fantasy;font-size:18px;color: Purple'>{} County </span>has the most<span style='font-size:18px;font-weight:bold;color:Red'> {}</span></p>".format(str(county_with_highest_crash),'crashes')
    folium_static(m, width=800, height=400)
    st.write(d1,unsafe_allow_html=True )

    m1 = folium.Map(location=[47, -122], tiles='cartodb positron', zoom_start=5.5)
    folium.GeoJson(json_dir,
            name="NAME", popup=folium.features.GeoJsonPopup(fields=["NAME","COUNTY"])).add_to(m1)

    st.subheader("Number of fatalities in each county")
    cp2 = folium.GeoJson(json_dir,
            style_function=lambda feature: {
                    'fillColor': linear_k(kill_dict[feature['properties']['NAME']]),
                    'fillOpacity':0.8,
                    'color': 'black',     #border color for the color fills
                    'weight': 1,          #how thick the border has to be
                    'dashArray': '5, 3'  #dashed lines length,space between them
                }).add_to(m1)
    linear_k.add_to(m1)
    for s in cp2.data['features']:
        ft = kill_count.loc[kill_count['County Name'] == s['properties']['NAME'], 'TOT_KILL'].astype(float).values[0]
        s['properties']['Fatalities'] = ft
    folium.GeoJsonTooltip(['NAME','Fatalities']).add_to(cp2)  
    folium.LayerControl().add_to(m1)
    
    d2 = "<p style='font-size:14px;font-weight:bold;'><span style='font-family:Impact, fantasy;font-size:18px;color: Purple'>{} County </span>has the most<span style='font-size:18px;font-weight:bold;color:Red'> {}</span></p>".format(str(county_with_highest_fatalities),'fatalities')
    folium_static(m1, width=800, height=400)
    #new_title = '<p style="font-family:Impact, fantasy; color:Red; font-size: 30px;">{} County</p>'
    st.write(d2,unsafe_allow_html=True )

        
