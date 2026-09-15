import streamlit as st

from database import get_participants
from dashboard_utils import add_working_memory_changes


st.title("💾 Working Memory")
st.caption("Pre-test, post-test, percentiles, and observed changes")


df = get_participants()

df = add_working_memory_changes(df)


# =====================================================
# CORSI
# =====================================================

st.subheader("Corsi Block-Tapping Test")

corsi_summary = (
    df.groupby("group_name")[
        [
            "corsi_score",
            "post_corsi_score",
            "corsi_percentile",
            "post_corsi_percentile",
            "corsi_change",
            "corsi_percentile_change",
        ]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    corsi_summary,
    use_container_width=True
)


st.write("### Corsi Score")

corsi_scores = (
    df.groupby("group_name")[
        ["corsi_score", "post_corsi_score"]
    ]
    .mean()
    .round(2)
)

st.bar_chart(corsi_scores)


st.write("### Corsi Percentile")

corsi_percentiles = (
    df.groupby("group_name")[
        ["corsi_percentile", "post_corsi_percentile"]
    ]
    .mean()
    .round(2)
)

st.bar_chart(corsi_percentiles)


# =====================================================
# DIGIT SPAN
# =====================================================

st.subheader("Digit Span Test")

digit_summary = (
    df.groupby("group_name")[
        [
            "digit_span_score",
            "post_digit_span_score",
            "digit_span_percentile",
            "post_digit_span_percentile",
            "digit_span_change",
            "digit_span_percentile_change",
        ]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    digit_summary,
    use_container_width=True
)


st.write("### Digit Span Score")

digit_scores = (
    df.groupby("group_name")[
        ["digit_span_score", "post_digit_span_score"]
    ]
    .mean()
    .round(2)
)

st.bar_chart(digit_scores)


st.write("### Digit Span Percentile")

digit_percentiles = (
    df.groupby("group_name")[
        ["digit_span_percentile", "post_digit_span_percentile"]
    ]
    .mean()
    .round(2)
)

st.bar_chart(digit_percentiles)


# =====================================================
# CHANGE
# =====================================================

st.subheader("Observed Change")

change_summary = (
    df.groupby("group_name")[
        [
            "corsi_change",
            "corsi_percentile_change",
            "digit_span_change",
            "digit_span_percentile_change",
        ]
    ]
    .mean()
    .round(2)
)

st.dataframe(
    change_summary,
    use_container_width=True
)