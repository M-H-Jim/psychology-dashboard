import streamlit as st

from database import get_participants


st.title("⚡ Multitasking")
st.caption("Performance during the secondary number-monitoring task")


df = get_participants()


# =====================================================
# ONLY AI AND NON-AI PARTICIPANTS
# =====================================================

multitasking_df = df[
    df["group_name"].isin(["AI", "Non-AI"])
].copy()


# =====================================================
# GROUP SUMMARY
# =====================================================

st.subheader("Multitasking Performance")


group_summary = (
    multitasking_df.groupby("group_name")[
        [
            "correct_presses",
            "false_presses",
            "missed_sevens",
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
# CORRECT PRESSES
# =====================================================

st.subheader("Correct Presses")

correct = (
    multitasking_df.groupby("group_name")[
        "correct_presses"
    ]
    .mean()
    .round(2)
)

st.bar_chart(correct)


# =====================================================
# FALSE PRESSES
# =====================================================

st.subheader("False Presses")

false = (
    multitasking_df.groupby("group_name")[
        "false_presses"
    ]
    .mean()
    .round(2)
)

st.bar_chart(false)


# =====================================================
# MISSED SEVENS
# =====================================================

st.subheader("Missed 7s")

missed = (
    multitasking_df.groupby("group_name")[
        "missed_sevens"
    ]
    .mean()
    .round(2)
)

st.bar_chart(missed)