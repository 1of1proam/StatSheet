import streamlit as st
import pandas as pd

sheet_id = "1Uui_QzqxqfUVDuL0n84zug2BIyYTHuwAKNbpTNWHgI8"

free_agent_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=Free%20Agent"

draft_combine_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=Draft%20Combine"

draft_combine1_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=Draft%20Combine1"

free_agent_df = pd.read_csv(free_agent_url)

draft_combine_df = pd.read_csv(draft_combine_url)

draft_combine1_df = pd.read_csv(draft_combine1_url)

st.title("2K League Stats")

st.header("Free Agent")
st.dataframe(free_agent_df)

st.header("Draft Combine")
st.dataframe(draft_combine_df)

st.header("Draft Combine1")
st.dataframe(draft_combine1_df)
