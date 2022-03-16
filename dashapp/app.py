import streamlit as st
from multiapp import MultiApp
import settings
import map_draft, histogramtime, home, factors, hy # import your pages here


settings.init()
app = MultiApp()

st.subheader("Multi page Crash/Fatality Visualization Dashboard")

# Add all your application here
#app.add_app("Home for Selection", datauploadandwidget.app)
app.add_app("Home Page",home.app)
app.add_app("Map", map_draft.app)
app.add_app("Timeline", histogramtime.app)
app.add_app("Factors", factors.app)
app.add_app("hy",hy.app)
# The main app
app.run()