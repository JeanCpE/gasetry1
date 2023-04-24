import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title('Heatmaps')

    filepath = "https://github.com/gaseapp/gasetry1/blob/main/records/gtag.csv"
    m = leafmap.Map(tiles="stamentoner")

    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude="longitude",
        value="pop_max",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=500)