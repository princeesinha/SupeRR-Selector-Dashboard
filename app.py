
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="SupeRR Selector Analytics",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 SupeRR Selector Season 2")
st.subheader("Pressure vs Normal Cricket Performance")

folder = os.path.dirname(__file__)

bat_file = os.path.join(folder, "Final_Batter_Ranking.csv")
bowl_file = os.path.join(folder, "Final_Bowler_Ranking.csv")

if os.path.exists(bat_file) and os.path.exists(bowl_file):

    bat = pd.read_csv(bat_file)
    bowl = pd.read_csv(bowl_file)

    st.header("🏏 Batter Performance")

    st.dataframe(bat, use_container_width=True)

    if "striker_name" in bat.columns:
        player = st.selectbox(
            "Select a batter",
            bat["striker_name"].tolist()
        )
        selected = bat[bat["striker_name"] == player].iloc[0]

        c1, c2, c3 = st.columns(3)
        c1.metric("Pressure Strike Rate", selected["pressure_SR"])
        c2.metric("Normal Strike Rate", selected["normal_SR"])
        c3.metric("SR Difference", selected["SR_difference"])

    st.header("🎯 Bowler Performance")
    st.dataframe(bowl, use_container_width=True)

    if "bowler_name" in bowl.columns:
        st.bar_chart(
            bowl.set_index("bowler_name")["wickets"]
        )

    st.caption(
        "Note: Rankings are exploratory and depend on the "
        "simplified pressure definition and sample size."
    )

else:
    st.error(
        "CSV files not found. Upload Final_Batter_Ranking.csv "
        "and Final_Bowler_Ranking.csv into this repository."
    )
