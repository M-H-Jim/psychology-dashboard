import streamlit as st

from database import (
    get_participants,
    delete_participant,
    delete_all_participants
)


st.title("🗃️ Raw Data")
st.caption("Complete participant dataset")

df = get_participants()


# Make displayed index start from 1
df.index = range(1, len(df) + 1)


# ─────────────────────────────────────────────
# CLT question labels
# ─────────────────────────────────────────────

clt_questions = [
    "এই কাজটি করতে আমার অনেক মানসিক প্রচেষ্টা প্রয়োজন হয়েছে।",
    "এই কাজটি সম্পন্ন করা আমার জন্য কঠিন ছিল।",
    "এই কাজটি করতে আমার মনোযোগ ধরে রাখা কঠিন ছিল।",
    "এই কাজটি করার সময় আমাকে অনেক চিন্তা করতে হয়েছে।",
    "এই কাজটি করতে আমার অনেক মানসিক শক্তি ব্যবহার করতে হয়েছে।",
    "এই কাজটি করার সময় তথ্যগুলো মনে রাখা কঠিন ছিল।",
    "এই কাজটি করার সময় আমার চিন্তাভাবনার উপর অনেক চাপ অনুভূত হয়েছে।",
    "এই কাজটি করার সময় একসঙ্গে অনেক বিষয় নিয়ে ভাবতে হয়েছে।",
    "এই কাজটি সম্পন্ন করতে আমার অনেক মনোযোগ দিতে হয়েছে।",
    "এই কাজটি করার সময় আমার মানসিক চাপ বেশি অনুভূত হয়েছে।",
    "এই কাজটি করার সময় তথ্য প্রক্রিয়া করা কঠিন মনে হয়েছে।",
    "এই কাজটি করার সময় আমার চিন্তার গতি ধীর হয়ে গেছে বলে মনে হয়েছে।",
    "এই কাজটি করার সময় বিভিন্ন তথ্য একসঙ্গে সামলানো কঠিন ছিল।",
    "এই কাজটি করার সময় আমার মানসিক ক্ষমতার উপর বেশি চাপ পড়েছে।",
    "সামগ্রিকভাবে, এই কাজটি আমার জন্য মানসিকভাবে কঠিন ছিল."
]


# ─────────────────────────────────────────────
# Rename CLT columns
# ─────────────────────────────────────────────

clt_column_names = {
    f"clt_{i:02d}": question
    for i, question in enumerate(clt_questions, start=1)
}

df = df.rename(columns=clt_column_names)


# ─────────────────────────────────────────────
# Reorder columns
# ─────────────────────────────────────────────

desired_order = [
    "id",
    "name",
    "group_name",

    # Pre-tests
    "corsi_score",
    "corsi_percentile",
    "digit_span_score",
    "digit_span_percentile",
    "trail_a",
    "trail_b",
    "trail_difference",
    "trail_b_percentile",

    # Treatment
    "correct_presses",
    "false_presses",
    "missed_sevens",
    "summary",

    # Post-tests
    "post_corsi_score",
    "post_corsi_percentile",
    "post_digit_span_score",
    "post_digit_span_percentile",
    "post_trail_a",
    "post_trail_b",
    "post_trail_difference",
    "post_trail_b_percentile",

    # Cognitive Load
    *clt_column_names.values(),
]


# Only use columns that actually exist
desired_order = [
    column
    for column in desired_order
    if column in df.columns
]

df = df[desired_order]


# Hide database ID from displayed table
display_df = df.drop(columns=["id"])


# ─────────────────────────────────────────────
# Layout
# ─────────────────────────────────────────────

left, right = st.columns([4, 2])


# ═════════════════════════════════════════════
# DATA TABLE
# ═════════════════════════════════════════════

with left:

    st.dataframe(
        display_df,
        use_container_width=True,
        height=650
    )


# ═════════════════════════════════════════════
# CONTROLS
# ═════════════════════════════════════════════

with right:

    # ─────────────────────────────────────────
    # Delete ONE participant
    # ─────────────────────────────────────────

    st.subheader("Delete Participant")

    if len(df) > 0:

        selected_index = st.selectbox(
            "Select participant",
            options=df.index
        )

        if "confirm_delete" not in st.session_state:
            st.session_state.confirm_delete = False

        if not st.session_state.confirm_delete:

            if st.button("Delete Selected Participant"):

                st.session_state.confirm_delete = True
                st.rerun()

        else:

            st.warning(
                f"Are you sure you want to delete Participant {selected_index}?"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button("Yes, Delete"):

                    db_id = df.loc[selected_index, "id"]

                    delete_participant(db_id)

                    st.session_state.confirm_delete = False

                    st.success(
                        f"Participant {selected_index} deleted successfully."
                    )

                    st.rerun()

            with col2:

                if st.button("Cancel"):

                    st.session_state.confirm_delete = False
                    st.rerun()

    else:

        st.info("No participant data available.")


    # ─────────────────────────────────────────
    # Delete ALL participants
    # ─────────────────────────────────────────

    # Only show this section when data exists
    if len(df) > 0:

        st.divider()

        st.subheader("⚠️ Delete All Data")

        if "confirm_delete_all" not in st.session_state:
            st.session_state.confirm_delete_all = False

        if not st.session_state.confirm_delete_all:

            if st.button(
                "Delete All Participants",
                type="primary"
            ):

                st.session_state.confirm_delete_all = True
                st.rerun()

        else:

            st.warning(
                "⚠️ This will permanently delete EVERY participant record."
            )

            delete_code = st.text_input(
                "Enter confirmation code",
                type="password"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button("Confirm Delete All"):

                    if delete_code == "1234":

                        delete_all_participants()

                        st.session_state.confirm_delete_all = False

                        st.success(
                            "All participant data has been deleted successfully."
                        )

                        st.rerun()

                    else:

                        st.error("Incorrect confirmation code.")

            with col2:

                if st.button("Cancel Delete All"):

                    st.session_state.confirm_delete_all = False
                    st.rerun()