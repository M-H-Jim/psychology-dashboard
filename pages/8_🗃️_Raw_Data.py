import streamlit as st

from database import (
    get_participants,
    delete_participant,
    delete_all_participants
)


st.set_page_config(layout="wide")



st.title("🗃️ Raw Data")
st.caption("Complete participant dataset")

df = get_participants()


# Make displayed index start from 1
df.index = range(1, len(df) + 1)


# ─────────────────────────────────────────────
# CLT question labels
# ─────────────────────────────────────────────

clt_questions = [
        "শেখার বিষয়বস্তু বুঝতে কঠিন ছিল।",
        "শেখার বিষয়বস্তুর ব্যাখ্যাগুলো বুঝতে কঠিন ছিল।",
        "শেখার বিষয়বস্তু জটিল ছিল।",
        "শেখার বিষয়বস্তুর মধ্যে অনেক জটিল তথ্য ছিল।",
        "পূর্ব জ্ঞান ছাড়া তথ্যগুলো বোধগম্য ছিল না।",
        "শেখার উপকরণের কাঠামো সম্পর্কে সামগ্রিক ধারণা পাওয়া কঠিন ছিল।",
        "শেখার উপকরণের নকশার কারণে পৃথক তথ্য-এককগুলোর মধ্যে সম্পর্ক শনাক্ত করা কঠিন ছিল।",
        "শেখার উপকরণের নকশা ব্যবহার-অনুপযোগী ছিল।",
        "শেখার উপকরণের নকশার কারণে প্রাসঙ্গিক তথ্য দ্রুত খুঁজে পাওয়া কঠিন ছিল।",
        "শেখার উপকরণের নকশার কারণে আমার মনে হয়েছিল যে শেখার বিষয়বস্তুতে মনোযোগ দিতে পারছি না।",
        "আমি শেখার বিষয়বস্তু নিয়ে সক্রিয়ভাবে চিন্তা করেছি।",
        "শেখার বিষয়বস্তু বোঝার জন্য আমি চেষ্টা করেছি।",
        "আমি শেখার বিষয়বস্তু সম্পর্কে সামগ্রিক/গভীর ধারণা অর্জন করেছি।",
        "শেখার বিষয়বস্তুর মাধ্যমে আমি আমার পূর্বজ্ঞানকে আরও বিস্তৃত করতে পেরেছি।",
        "শেখার উপকরণের মাধ্যমে অর্জিত জ্ঞান আমি দ্রুত ও নিখুঁতভাবে প্রয়োগ করতে পারি।"
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
# ADEXI question labels
# ─────────────────────────────────────────────

adexi_questions = [
    "আমার দীর্ঘ নির্দেশনা মনে রাখতে অসুবিধা হয়।",
    "কোনো কাজের মাঝখানে আমি কী করছিলাম তা মনে রাখতে আমার অসুবিধা হয়।",
    "কী ঘটতে পারে তা আগে না ভেবেই কাজ করে ফেলার প্রবণতা আমার আছে।",
    "কেউ নিষেধ করলেও আমার পছন্দের কোনো কাজ থেকে নিজেকে বিরত রাখতে আমার অসুবিধা হয়।",
    "কেউ আমাকে একসঙ্গে কয়েকটি কাজ করতে বললে, আমি শুধু প্রথমটি অথবা শেষটি মনে রাখি।",
    "অনুপযুক্ত পরিস্থিতিতে হাসি বা অট্টহাসি থেকে বিরত থাকতে আমার অসুবিধা হয়।",
    "কোনো সমস্যায় আটকে গেলে সেটি সমাধানের ভিন্ন উপায় বের করতে আমার অসুবিধা হয়।",
    "কেউ আমাকে কিছু আনতে বললে, কী আনতে হবে তা আমি ভুলে যাই।",
    "কোনো কাজের পরিকল্পনা করতে আমার অসুবিধা হয় (যেমন, ভ্রমণে, কাজে বা স্কুলে যাওয়ার সময় প্রয়োজনীয় সবকিছু সঙ্গে নেওয়ার কথা মনে রাখা)।",
    "আমার পছন্দের কোনো কাজ থামাতে আমার অসুবিধা হয় (যেমন, ঘুমানোর সময় হয়ে গেলেও সন্ধ্যায় টিভি দেখা বা কম্পিউটারের সামনে বসে থাকা)।",
    "কীভাবে করতে হবে তা দেখিয়ে না দিলে শুধু মৌখিক নির্দেশনা বুঝতে আমার অসুবিধা হয়।",
    "একাধিক ধাপ রয়েছে এমন কাজ বা কার্যক্রম করতে আমার অসুবিধা হয়।",
    "আগাম চিন্তা করতে বা অভিজ্ঞতা থেকে শিখতে আমার অসুবিধা হয়।",
    "আমার সঙ্গে যাদের দেখা হয়, তারা আমাকে আমার সমবয়সীদের তুলনায় বেশি প্রাণবন্ত বা চঞ্চল মনে করেন বলে মনে হয়।"
]

adexi_column_names = {
    f"adexi_{i:02d}": question
    for i, question in enumerate(adexi_questions, start=1)
}

df = df.rename(columns=adexi_column_names)



# ─────────────────────────────────────────────
# Reorder columns
# ─────────────────────────────────────────────

desired_order = [
    "id",
    "name",
    "group_name",

    # Pre-tests
    "trail_a",
    "trail_b",
    "trail_difference",
    "trail_b_percentile",

    # Treatment
    "correct_presses",
    "false_presses",
    "missed_sevens",
    "mcq1",
    "mcq2",
    "mcq3",
    "mcq4",

    # Post-tests
    "post_trail_a",
    "post_trail_b",
    "post_trail_difference",
    "post_trail_b_percentile",

    # Cognitive Load
    *clt_column_names.values(),
    # ADEXI
    *adexi_column_names.values(),
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

            selected_id = int(df.loc[selected_index, "id"])
            selected_name = df.loc[selected_index, "name"]

            st.warning(
                f"You're about to permanently delete participant "
                f"'{selected_name}'."
            )

            st.caption("This action cannot be undone.")

            col1, col2 = st.columns(2)

            with col1:

                if st.button("Yes, Delete"):

                    db_id = df.loc[selected_index, "id"]

                    delete_participant(db_id)

                    st.session_state.confirm_delete = False

                    st.success(
                        f"Participant {selected_name} deleted successfully."
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
                "Type 'DELETE ALL' to confirm",
                type="password"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button("Confirm Delete All"):

                    if delete_code == "DELETE ALL":

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