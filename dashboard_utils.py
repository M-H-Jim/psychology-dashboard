def count_groups(df):
    return {
        "AI": (df["group_name"] == "AI").sum(),
        "Non-AI": (df["group_name"] == "Non-AI").sum(),
        "Control": (df["group_name"] == "Control").sum(),
    }

def get_group_counts(df):
    return (
        df["group_name"]
        .value_counts()
        .rename_axis("Group")
        .reset_index(name="Participants")
    )

def add_cognitive_load_scores(df):
    df = df.copy()

    # CLT total score
    clt_columns = [
        f"clt_{i:02d}"
        for i in range(1, 16)
    ]

    df["clt_total"] = df[clt_columns].sum(axis=1)

    # Leppink total score
    leppink_columns = [
        f"leppink_{i:02d}"
        for i in range(1, 11)
    ]

    df["leppink_total"] = df[leppink_columns].sum(axis=1)

    return df

def add_working_memory_changes(df):
    df = df.copy()

    # Raw score changes
    df["corsi_change"] = (
        df["post_corsi_score"] - df["corsi_score"]
    )

    df["digit_span_change"] = (
        df["post_digit_span_score"] - df["digit_span_score"]
    )

    # Percentile changes
    df["corsi_percentile_change"] = (
        df["post_corsi_percentile"] - df["corsi_percentile"]
    )

    df["digit_span_percentile_change"] = (
        df["post_digit_span_percentile"]
        - df["digit_span_percentile"]
    )

    return df

def add_divided_attention_changes(df):
    df = df.copy()

    # Trail Making Part B time change
    df["trail_b_change"] = (
        df["post_trail_b"] - df["trail_b"]
    )

    # Trail Making Part B percentile change
    df["trail_b_percentile_change"] = (
        df["post_trail_b_percentile"]
        - df["trail_b_percentile"]
    )

    return df