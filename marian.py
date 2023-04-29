#GASE Egg Hotspot Mapping Prototype App
#-------Dependencies-----------
import streamlit as st

#------WEBPAGE SETTINGS----
page_title = "GASEApp"
page_icon = ":seedling:"
layout = "centered"

#---------------------------
# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:
import os
st.write(
	"Has environment variables been set:",
	os.environ["db_username"] == st.secrets["db_username"])

#--------------------------

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title + " " + page_icon)


#----INPUT & SAVE FORM------
if st.button('UPLOAD'):
    st.write('UPLOADED')
else:
    st.write('UPLOAD IMAGE')

#-+++++++++++++++++++++++++++++++++++++++
#----------------------------------------
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gtag_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
