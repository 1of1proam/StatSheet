import streamlit as st
import pandas as pd
from urllib.parse import quote

sheet_id = "1Uui_QzqxqfUVDuL0n84zug2BIyYIHuwAKNbpTNWHgI8"

tab_name = "Combine Game 2"

encoded_tab = quote(tab_name)

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_tab}"

df = pd.read_csv(url)

st.title("Combine Game 2")

st.dataframe(df)
