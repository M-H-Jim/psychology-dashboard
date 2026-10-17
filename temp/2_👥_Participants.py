import streamlit as st

from database import get_participants


st.title("👥 Participants")
st.caption("Participant overview and group information")


df = get_participants()


# -------------------------
# Filters
# -------------------------

col1, col2 = st.columns(2)

with col1:
    search = st.text_input(
        "Search participant",
        placeholder="Enter participant name..."
    )

with col2:
    group_filter = st.selectbox(
        "Group",
        ["All", "AI", "Non-AI", "Control"]
    )


# -------------------------
# Apply filters
# -------------------------

filtered_df = df.copy()


if search:
    filtered_df = filtered_df[
        filtered_df["name"]
        .astype(str)
        .str.contains(search, case=False, na=False)
    ]


if group_filter != "All":
    filtered_df = filtered_df[
        filtered_df["group_name"] == group_filter
    ]


# -------------------------
# Results
# -------------------------

st.subheader("Participants")

st.write(
    f"Showing **{len(filtered_df)}** of **{len(df)}** participants"
)


st.dataframe(
    filtered_df[
        [
            "id",
            "name",
            "group_name",
            "corsi_score",
            "digit_span_score",
            "trail_a",
            "trail_b",
        ]
    ],
    use_container_width=True,
    height=550
)