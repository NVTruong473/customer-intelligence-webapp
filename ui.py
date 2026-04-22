import streamlit as st
import pandas as pd
from predict import predict_customer
from utils import reset_users


def dashboard():

    # --------------------------------
    # TOP BAR
    # --------------------------------
    col1, col2, col3 = st.columns([6, 2, 2])

    with col1:
        st.markdown(
            f"""
            <div class='title-box'>
                <h2>Welcome {st.session_state.user}</h2>
                <p>Customer Intelligence Dashboard</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        if st.session_state.user == "admin":
            if st.button("Reset Data"):
                reset_users()
                st.success("Reset completed.")
                st.rerun()

    with col3:
        if st.button("Logout"):
            st.session_state.login = False
            st.session_state.user = ""
            st.rerun()

    # --------------------------------
    # SIDEBAR INPUT
    # --------------------------------
    st.sidebar.header("Customer Input")

    tenure = st.sidebar.slider(
        "Service Months",
        0, 72, 12
    )

    monthly = st.sidebar.slider(
        "Monthly Charges",
        0.0, 150.0, 70.0
    )

    total = st.sidebar.slider(
        "Total Charges",
        0.0, 10000.0, 1000.0
    )

    senior = st.sidebar.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    gender = st.sidebar.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    partner = st.sidebar.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.sidebar.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    phone = st.sidebar.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    internet = st.sidebar.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    contract = st.sidebar.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"]
    )

    payment = st.sidebar.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    # --------------------------------
    # SUMMARY CARDS
    # --------------------------------
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class='card'>
                <div class='big'>{tenure}</div>
                <div class='small'>Service Months</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class='card'>
                <div class='big'>${monthly:.0f}</div>
                <div class='small'>Monthly Bill</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class='card'>
                <div class='big'>{contract}</div>
                <div class='small'>Contract Type</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # BUILD INPUT DATA
    # --------------------------------
    data = {
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "SeniorCitizen": senior,
        "gender": gender,
        "Partner": partner,
        "Dependents": dependents,
        "PhoneService": phone,
        "InternetService": internet,
        "Contract": contract,
        "PaymentMethod": payment
    }

    # --------------------------------
    # PREDICT BUTTON
    # --------------------------------
    st.markdown("### Prediction Center")

    if st.button("Predict Customer Risk"):

        pred, prob = predict_customer(data)

        st.subheader("Prediction Result")

        if pred == 1:
            st.error("High Churn Risk")
        else:
            st.success("Low Churn Risk")

        st.progress(int(prob * 100))
        st.write(f"Churn Probability: {prob:.2%}")

        if prob >= 0.70:
            st.warning(
                "Recommendation: Offer discount now."
            )

        elif prob >= 0.40:
            st.info(
                "Recommendation: Contact customer soon."
            )

        else:
            st.success(
                "Recommendation: Upsell premium package."
            )

        st.markdown("### Input Summary")

        st.dataframe(
            pd.DataFrame([data]),
            use_container_width=True
        )
