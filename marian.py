#GASE Egg Hotspot Mapping Prototype App
#-------Dependencies-----------
import streamlit as st

#------WEBPAGE SETTINGS----
page_title = "GASEApp"
page_icon = ":seedling:"
layout = "centered"

#---------------------------
# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["Marian"])
st.write("DB password:", st.secrets["Marian12345"])

# And the root-level secrets are also accessible as environment variables:

import os
st.write(
	"Has environment variables been set:",
	os.environ["Marian"] == st.secrets["Marian"])

#--------------------------

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title + " " + page_icon)


#----INPUT & SAVE FORM------
if st.button('UPLOAD'):
    st.write('UPLOADED')
else:
    st.write('UPLOAD IMAGE')
