
import streamlit as st
import pandas as pd

from database import get_participants


st.set_page_config(
    page_title="Participant Profiles",
    page_icon="👤",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

st.title("👤 Participant Profiles")
st.caption("Browse participants and view their individual research records.")

df = get_participants()

if df.empty:
    st.info("No participants have been registered yet.")
    st.stop()


# --------------------------------------------------
# PARTICIPANT SELECTOR
# --------------------------------------------------

st.subheader("Participant Directory")

# Search by participant name or ID
search = st.text_input(
    "🔎 Search participants",
    placeholder="Enter participant name or ID..."
)

filtered_df = df.copy()

if search:
    search = search.strip()

    filtered_df = filtered_df[
        filtered_df["name"].astype(str).str.contains(
            search, case=False, na=False
        )
        |
        filtered_df["id"].astype(str).str.contains(
            search, case=False, na=False
        )
    ]

if filtered_df.empty:
    st.warning("No matching participants found.")
    st.stop()


# Create readable options while keeping the actual database ID
participant_options = {
    f"Participant {i + 1} — {row['name']} ({row['group_name']})": row["id"]
    for i, (_, row) in enumerate(filtered_df.iterrows())
}

selected_label = st.selectbox(
    "Select a participant",
    options=list(participant_options.keys())
)

selected_id = participant_options[selected_label]

participant = df.loc[df["id"] == selected_id].iloc[0]


# --------------------------------------------------
# PROFILE HEADER
# --------------------------------------------------

st.divider()

col1, col2 = st.columns([1, 5])

with col1:
    st.markdown(
        """
        <div style="
            background-color: #262730;
            border-radius: 50%;
            width: 100px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
        ">👤</div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.title(str(participant.get("name", "Unknown")))
    participant_number = df.index[df["id"] == selected_id][0] + 1
    st.caption(f"Participant #{participant_number}")

    group = participant.get("group_name", "Unknown")

    if group == "AI":
        st.success("AI Group")
    elif group == "Non-AI":
        st.info("Non-AI Group")
    elif group == "Control":
        st.warning("Control Group")
    else:
        st.write(f"Group: {group}")


# --------------------------------------------------
# PROFILE TABS
# --------------------------------------------------

profile_tab, tests_tab, questionnaires_tab = st.tabs([
    "👤 Profile",
    "🧠 Tests",
    "📋 Questionnaires"
])


# --------------------------------------------------
# PROFILE TAB
# --------------------------------------------------

with profile_tab:

    st.subheader("Personal Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Age**")
        st.write(participant.get("age", "N/A"))

        st.markdown("**Gender**")
        st.write(participant.get("gender", "N/A"))

        st.markdown("**University**")
        st.write(participant.get("university", "N/A"))

    with col2:
        st.markdown("**Department**")
        st.write(participant.get("department", "N/A"))

        st.markdown("**Academic Year**")
        st.write(participant.get("academic_year", "N/A"))

        st.markdown("**Socioeconomic Status**")
        st.write(participant.get("socioeconomic_status", "N/A"))

    with col3:
        st.markdown("**Daily Internet Usage**")
        st.write(participant.get("daily_internet_hours", "N/A"))

        st.markdown("**Internet Purpose**")
        purpose = participant.get("internet_purposes", "N/A")
        other = participant.get("internet_purpose_other")

        if purpose == "Other" and pd.notna(other):
            st.write(f"Other: {other}")
        else:
            st.write(purpose)

        st.markdown("**Physical Activity**")
        st.write(participant.get("daily_physical_activity", "N/A"))

    st.divider()

    st.subheader("Additional Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Internet Usage Affects Life**")
        st.write(participant.get("internet_usage_affects_life", "N/A"))

    with col2:
        st.markdown("**Has Close Friend**")
        st.write(participant.get("has_close_friend", "N/A"))

    st.divider()

    st.subheader("Research Consent")

    consent = participant.get("consent_given")

    if consent is True:
        st.success("Consent provided")
    elif consent is False:
        st.error("Consent not provided")
    else:
        st.write("Consent information unavailable")

    st.write(
        "Consent Date:",
        participant.get("consent_date", "N/A")
    )


# --------------------------------------------------
# TESTS TAB
# --------------------------------------------------

with tests_tab:

    st.subheader("Trail Making Test")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Pre-test**")

        st.metric("Trail A", participant.get("trail_a", "N/A"))
        st.metric("Trail B", participant.get("trail_b", "N/A"))
        st.metric(
            "Difference",
            participant.get("trail_difference", "N/A")
        )
        st.metric(
            "Trail B Percentile",
            participant.get("trail_b_percentile", "N/A")
        )

    with col2:
        st.markdown("**Post-test**")

        st.metric("Trail A", participant.get("post_trail_a", "N/A"))
        st.metric("Trail B", participant.get("post_trail_b", "N/A"))
        st.metric(
            "Difference",
            participant.get("post_trail_difference", "N/A")
        )
        st.metric(
            "Trail B Percentile",
            participant.get("post_trail_b_percentile", "N/A")
        )

    st.divider()

    st.subheader("Number Monitoring Task")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Correct Presses",
            participant.get("correct_presses", "N/A")
        )

    with col2:
        st.metric(
            "False Presses",
            participant.get("false_presses", "N/A")
        )

    with col3:
        st.metric(
            "Missed Sevens",
            participant.get("missed_sevens", "N/A")
        )

    st.divider()

    st.subheader("Multiple Choice Questions")

    mcq_cols = st.columns(4)

    for i in range(1, 5):
        with mcq_cols[i - 1]:
            st.metric(
                f"MCQ {i}",
                participant.get(f"mcq{i}", "N/A")
            )


# --------------------------------------------------
# QUESTIONNAIRES TAB
# --------------------------------------------------

with questionnaires_tab:

    st.subheader("ADEXI Questionnaire")

    pre_adexi = [
        participant.get(f"pre_adexi_{i:02d}")
        for i in range(1, 15)
    ]

    post_adexi = [
        participant.get(f"adexi_{i:02d}")
        for i in range(1, 15)
    ]

    adexi_df = pd.DataFrame({
        "Question": [f"Question {i}" for i in range(1, 15)],
        "Pre-ADEXI": pre_adexi,
        "Post-ADEXI": post_adexi
    })

    st.dataframe(
        adexi_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Cognitive Load Test")

    clt_values = [
        participant.get(f"clt_{i:02d}")
        for i in range(1, 16)
    ]

    clt_df = pd.DataFrame({
        "Question": [f"Question {i}" for i in range(1, 16)],
        "Response": clt_values
    })

    st.dataframe(
        clt_df,
        use_container_width=True,
        hide_index=True
    )
