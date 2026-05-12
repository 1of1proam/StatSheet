import streamlit as st
import pandas as pd

sheet_id = "PASTE_YOUR_SHEET_ID_HERE"

url = f"https://docs.google.com/spreadsheets/d/1Uui_QzqxqfUVDuL0n84zug2BIyYIHuwAKNbpTNWHgI8/edit?gid=0#gid=0"

df = pd.read_csv(url)

st.title("2K League Stats")

st.dataframe(df)
