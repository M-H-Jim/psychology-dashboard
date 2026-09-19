import streamlit as st

from database import get_participants


st.title("🗃️ Raw Data")
st.caption("Complete participant dataset")

df = get_participants()


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
    "সামগ্রিকভাবে, এই কাজটি আমার জন্য মানসিকভাবে কঠিন ছিল।"
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
    column for column in desired_order
    if column in df.columns
]

df = df[desired_order]


st.dataframe(
    df,
    use_container_width=True,
    height=650
)