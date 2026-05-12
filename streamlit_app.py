import pandas as pd
import streamlit as st

st.title("2K League Stats")

data = {
"Player": ["Player 1", "Player 2", "Player 3"],
"PPG": [30.2, 25.1, 18.4],
"APG": [8.1, 6.3, 4.2],
"RPG": [7.5, 10.1, 5.3]
}

df = pd.DataFrame(data)

st.subheader("Player Stats")
st.dataframe(df)

st.subheader("League Leader")

top_scorer = df.loc[df["PPG"].idxmax(), "Player"]

st.write("Top Scorer:", top_scorer)
