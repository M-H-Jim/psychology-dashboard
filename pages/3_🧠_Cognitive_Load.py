import streamlit as st

from database import get_participants
from dashboard_utils import add_cognitive_load_scores


st.title("🧠 Cognitive Load")
st.caption("Descriptive overview of cognitive load measures")


df = get_participants()

df = add_cognitive_load_scores(df)


# -------------------------
# Group summary
# -------------------------

st.subheader("Cognitive Load by Group")

group_summary = (
    df.groupby("group_name")[
        ["clt_total", "leppink_total", "paas_mental_effort"]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    group_summary,
    use_container_width=True
)


# -------------------------
# CLT
# -------------------------

st.subheader("Cognitive Load Theory Questionnaire")

st.bar_chart(
    group_summary["clt_total"]
)


# -------------------------
# Leppink
# -------------------------

st.subheader("Leppink Cognitive Load Scale")

st.bar_chart(
    group_summary["leppink_total"]
)


# -------------------------
# Paas
# -------------------------

st.subheader("Paas Mental Effort")

st.bar_chart(
    group_summary["paas_mental_effort"]
)