import streamlit as st

from database import get_participants
from dashboard_utils import add_divided_attention_changes


st.title("🎯 Divided Attention")
st.caption("Trail Making Test Part B performance")


df = get_participants()

df = add_divided_attention_changes(df)


# =====================================================
# GROUP SUMMARY
# =====================================================

st.subheader("Trail Making Part B by Group")


group_summary = (
    df.groupby("group_name")[
        [
            "trail_b",
            "post_trail_b",
            "trail_b_percentile",
            "post_trail_b_percentile",
            "trail_b_change",
            "trail_b_percentile_change",
        ]
    ]
    .mean()
    .round(2)
)


st.dataframe(
    group_summary,
    use_container_width=True
)


# =====================================================
# TRAIL B TIME
# =====================================================

st.subheader("Trail B Completion Time")

trail_time = (
    df.groupby("group_name")[
        ["trail_b", "post_trail_b"]
    ]
    .mean()
    .round(2)
)

st.bar_chart(trail_time)


# =====================================================
# TRAIL B PERCENTILE
# =====================================================

st.subheader("Trail B Percentile")

trail_percentile = (
    df.groupby("group_name")[
        ["trail_b_percentile", "post_trail_b_percentile"]
    ]
    .mean()
    .round(2)
)

st.bar_chart(trail_percentile)


# =====================================================
# CHANGE
# =====================================================

st.subheader("Observed Change")

change_summary = (
    df.groupby("group_name")[
        [
            "trail_b_change",
            "trail_b_percentile_change",
        ]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    change_summary,
    use_container_width=True
)