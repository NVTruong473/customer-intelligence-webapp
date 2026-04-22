import streamlit as st


def load_css():
    st.markdown("""
    <style>

    /* ----------------------------- */
    /* GLOBAL */
    /* ----------------------------- */

    .main {
        background:
        linear-gradient(
            135deg,
            #e0f2fe 0%,
            #f5f3ff 50%,
            #fdf2f8 100%
        );
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1250px;
    }

    h1, h2, h3 {
        color: #111827;
    }

    /* ----------------------------- */
    /* HEADER */
    /* ----------------------------- */

    .title-box {
        background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed,
            #ec4899
        );

        color: white;
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 18px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }

    .title-box h2 {
        margin: 0;
        padding: 0;
        color: white;
    }

    .title-box p {
        margin-top: 6px;
        margin-bottom: 0;
        opacity: 0.95;
        font-size: 15px;
    }

    /* ----------------------------- */
    /* CARD */
    /* ----------------------------- */

    .card {
        background: white;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.06);
        margin-bottom: 14px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.6);
    }

    .big {
        font-size: 28px;
        font-weight: 800;
        color: #111827;
    }

    .small {
        color: #6b7280;
        font-size: 14px;
        margin-top: 4px;
    }

    /* ----------------------------- */
    /* BUTTON */
    /* ----------------------------- */

    .stButton > button {
        width: 100%;
        min-height: 52px;
        border: none;
        border-radius: 14px;
        font-size: 18px;
        font-weight: 700;
        color: white;

        background:
        linear-gradient(
            90deg,
            #2563eb,
            #06b6d4,
            #10b981
        );

        box-shadow: 0 8px 20px rgba(37,99,235,0.22);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        filter: brightness(1.03);
    }

    .stButton > button:active {
        transform: scale(0.99);
    }

    /* ----------------------------- */
    /* INPUT */
    /* ----------------------------- */

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px !important;
    }

    label {
        font-weight: 600 !important;
    }

    /* ----------------------------- */
    /* SIDEBAR */
    /* ----------------------------- */

    section[data-testid="stSidebar"] {
        background: rgba(255,255,255,0.82);
        backdrop-filter: blur(8px);
    }

    /* ----------------------------- */
    /* TABLE */
    /* ----------------------------- */

    .stDataFrame {
        border-radius: 14px;
        overflow: hidden;
    }

    /* ----------------------------- */
    /* MOBILE */
    /* ----------------------------- */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .title-box {
            padding: 16px;
        }

        .title-box h2 {
            font-size: 24px;
        }

        .title-box p {
            font-size: 13px;
        }

        .big {
            font-size: 22px;
        }

        .small {
            font-size: 12px;
        }

        .stButton > button {
            min-height: 56px;
            font-size: 16px;
        }
    }

    </style>
    """, unsafe_allow_html=True)
