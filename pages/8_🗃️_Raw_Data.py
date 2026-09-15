import streamlit as st

from database import get_participants


st.title("🗃️ Raw Data")
st.caption("Complete participant dataset")


df = get_participants()


st.dataframe(
    df,
    use_container_width=True,
    height=650
)