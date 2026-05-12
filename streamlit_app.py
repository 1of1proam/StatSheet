import streamlit as st
import pandas as pd
from urllib.parse import quote

st.set_page_config(page_title="1of1 Pro Am", layout="wide")

sheet_id = "1Uui_QzqxqfUVDuL0n84zug2BIyYIHuwAKNbpTNWHgI8"

def load_sheet(tab_name):
  encoded_tab = quote(tab_name)
  url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_tab}"
  return pd.read_csv(url)

st.title("🏀 1of1 Pro Am")

free_agent_df = load_sheet("Free Agent")
combine_game1_df = load_sheet("Combine Game 1 Stats ")
combine_game2_df = load_sheet("Combine Game 2 Stats ")

players_tab, game1_tab, game2_tab = st.tabs([
  "👤 PLAYERS",
  "🏆 Combine Game 1 Stats",
  "🏆 Combine Game 2 Stats"
])

with players_tab:
  st.subheader("Free Agent")
  st.dataframe(free_agent_df, use_container_width=True)

with game1_tab:
  st.subheader("Combine Game 1")
  st.dataframe(combine_game1_df, use_container_width=True)

with game2_tab:
  st.subheader("Combine Game 2")
  st.dataframe(combine_game2_df, use_container_width=True)
