from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="요트 다이스",
    page_icon="🎲",
    layout="wide",
)

html_file = Path(__file__).resolve().parent / "yacht_dice.html"

st.iframe(
    html_file,
    width="stretch",
    height="content",
)
