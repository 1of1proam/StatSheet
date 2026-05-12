import streamlit as st
import pandas as pd
from urllib.parse import quote

sheet_id = "1Uui_QzqxqfUVDuL0n84zug2BIyYIHuwAKNbpTNWHgI8"

def load_sheet(tab_name):
  encoded_tab = quote(tab_name)
  url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_tab}"
  return pd.read_csv(url)

st.title("2K League Stats")

free_agent_df = load_sheet("Free Agent")
draft_combine_df = load_sheet("Draft Combine")
draft_combine1_df = load_sheet("Draft Combine1")

st.header("Free Agent")
st.dataframe(free_agent_df)

st.header("Draft Combine")
st.dataframe(draft_combine_df)

st.header("Draft Combine1")
st.dataframe(draft_combine1_df)
