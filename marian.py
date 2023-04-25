#GASE Egg Hotspot Mapping Prototype App
#-------Dependencies-----------
import calendar
from datetime import datetime
import streamlit as st
import plotly.graph_objects as go


#------WEBPAGE SETTINGS----
page_title = "GASEApp"
page_icon = ":seedling:"
layout = "centered"

maps = ["History","Current"]
#--------------------------

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title + " " + page_icon)

#------DROP DOWN-----------
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

#----INPUT & SAVE FORM------
if st.button('UPLOAD'):
    st.write('UPLOADED')
else:
    st.write('UPLOAD IMAGE')
#--------------------------#
st.header(f"Data Entry")
with st.form("entry_form",clear_on_submit=True):
    column1,column2 = st.columns(2)
    column1.selectbox("Select Month: ",months,key="month")
    column2.selectbox("Select Year: ", years, key="year")
    "---"
    
    with st.expander("Maps"):
        for maps in maps:
            st.number_input(f"{maps}:", min_value=0,format="%i",step=10,key=maps)
    "---"
    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"] + "_" + str(st.session_state["month"]))
        maps = {maps: st.session_state[maps] for maps in maps}
        #TODO
        st.write(f"maps:{maps}")