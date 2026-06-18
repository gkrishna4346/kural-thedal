import streamlit as st
import pandas as pd


# -----------------
# PAGE CONFIG
# -----------------

st.set_page_config(
    page_title="குறளும் பொருளும்",
    layout="centered"
)


# -----------------
# LOAD DATA
# -----------------

@st.cache_data
def load_data():

    df = pd.read_csv("raw_kt.csv")

    df["Kural Number"] = (
        df["Kural Number"].astype(int)
    )

    return df


try:
    df = load_data()

except:
    st.error("raw_kt.csv not found")
    st.stop()


# -----------------
# HEADER
# -----------------

left_header, right_header = st.columns([4, 1])

with left_header:

    st.title("குறளும் பொருளும்")

    st.caption(
        "குறளின் மாண்பு - சான்றோர் பார்வையில்"
    )

with right_header:

    st.image(
        "images/logo.png",
        width=140
    )

st.divider()


# -----------------
# SEARCH
# -----------------

left, right = st.columns([3, 1])

with left:

    kural_num = st.number_input(
        "Kural Number",
        min_value=1,
        max_value=1330,
        value=1
    )

with right:

    st.write("")


search = st.button(
    "🔍 Search",
    use_container_width=True
)


# -----------------
# RESULTS
# -----------------

if search:

    row = df[
        df["Kural Number"] == kural_num
    ]

    if row.empty:

        st.warning(
            "Kural not found"
        )

    else:

        r = row.iloc[0]

        c1, c2 = st.columns(2)

        with c1:

            st.text_input(
                "Section Name",
                str(r.get("Section Name", "")),
                disabled=True
            )

        with c2:

            st.text_input(
                "Chapter Number",
                str(r.get("Chapter Number", "")),
                disabled=True
            )

        st.text_input(
            "Chapter Name",
            str(r.get("Chapter Name", "")),
            disabled=True
        )

        st.subheader("📜 Kural")

        st.text_area(
            "",
            str(r.get("Kural", "")),
            height=120
        )

        # -----------------
        # மு.வ உரை
        # -----------------

        st.subheader(
            "மு.வ உரை:"
        )

        st.text_area(
            "",
            str(r.iloc[5]) if len(r) > 5 else "",
            height=120
        )

        # -----------------
        # கலைஞர் உரை
        # -----------------

        st.subheader(
            "கலைஞர் உரை:"
        )

        st.text_area(
            "",
            str(r.iloc[6]) if len(r) > 6 else "",
            height=120
        )

        # -----------------
        # சாலமன் பாப்பையா உரை
        # -----------------

        st.subheader(
            "சாலமன் பாப்பையா உரை:"
        )

        st.text_area(
            "",
            str(r.iloc[7]) if len(r) > 7 else "",
            height=120
        )
