import streamlit as st
import pandas as pd
from urllib.parse import quote
import base64

def get_base64(file_path):
  with open(file_path, "rb") as f:
    data = f.read()
  return base64.b64encode(data).decode()

logo_base64 = get_base64("logo.png")

st.markdown(
  f"""
  <style>
  .stApp {{
  background-image: url("data:image/png;base64,{logo_base64}");
  background-size: 500px;
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
}}
</style>
""",
unsafe_allow_html=True
)

st.set_page_config(page_title="1of1 Pro Am", layout="wide")

sheet_id = "1Uui_QzqxqfUVDuL0n84zug2BIyYIHuwAKNbpTNWHgI8"

def load_sheet(tab_name):
  encoded_tab = quote(tab_name)
  url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_tab}"
  return pd.read_csv(url)

st.title(" 1of1 Pro Am")

free_agent_df = load_sheet("Free Agent")
combine_game1_df = load_sheet("Combine Game 1 Stats")
combine_game2_df = load_sheet("Combine Game 2 Stats")
draft_df = load_sheet("Draft")
teams_df = load_sheet("Teams")

players_tab, game1_tab, game2_tab, draft_tab, teams_tab = st.tabs([
  " Free Agent Players",
  " Combine Game 1 Stats",
  " Combine Game 2 Stats",
  " Draft ",
  " Teams "
])

with players_tab:
  st.subheader("Free Agent")
  st.dataframe(free_agent_df, use_container_width=True)

with game1_tab:
  st.subheader("Combine Game 1 Stats")
  st.dataframe(combine_game1_df, use_container_width=True)

with game2_tab:
  st.subheader("Combine Game 2 Stats")
  st.dataframe(combine_game2_df, use_container_width=True)

with draft_tab:
  st.subheader("Draft")
  st.dataframe(draft_df, use_container_width=True)

with teams_tab:
  st.subheader("Teams")
  st.dataframe(teams_df, use_container_width=True)
