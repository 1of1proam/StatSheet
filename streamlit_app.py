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
combine_game1_df = load_sheet("Combine Game 1")
combine_game2_df = load_sheet("Combine Game 2")
draft_df = load_sheet("Draft")
teams_df = load_sheet("teams")


st.header("Free Agent")
st.dataframe(free_agent_df)

st.header("Combine Game 1")
st.dataframe(combine_game1_df)

st.header("Combine Game 2")
st.dataframe(combine_game2_df)

st.header("Draft")
st.dataframe(draft_df)

st.header("Teams")
st.dataframe(teams_df)
