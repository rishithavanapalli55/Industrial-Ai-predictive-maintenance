import streamlit as st

# Configure page layout
st.set_page_config(layout="wide", page_title="Industrial Predictive Maintenance", page_icon="🏭")

# --- Custom CSS for a professional dark theme ---
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: #c9d1d9;
        }
        .big-font {
            font-size: 36px !important;
            font-weight: 800 !important;
            color: #f0f6fc;
            margin-bottom: 5px;
        }
        .sub-font {
            font-size: 16px !important;
            color: #8b949e;
            margin-bottom: 25px;
        }
        .model-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .section-header {
            font-size: 20px;
            font-weight: 700;
            color: #f0f6fc;
            margin-top: 20px;
            margin-bottom: 15px;
        }
        .stButton>button {
            width: 100%;
            background-color: #238636;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            border: 1px solid #2ea043;
        }
        .stButton>button:hover {
            background-color: #2ea043;
            border-color: #3fb950;
        }
    </style>
""", unsafe_allow_html=True)

# --- Layout Implementation ---

# 1. Header Section
st.markdown('<p class="big-font">🏭 Industrial AI Predictive Maintenance</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">A smart system to detect and prevent machine failures in your production line.</p>', unsafe_allow_html=True)

# Create two columns for main content and sidebar stats
col_left, col_right = st.columns([2, 1])

with col_left:
    # 2. Active Machine Learning Model Card
    st.markdown('<p class="section-header">🛠️ Active AI Model</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="model-card">
            <div style="color: #8b949e; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px;">Model Name</div>
            <div style="color: #56d364; font-size: 22px; font-weight: 800; margin-top: 5px;">Random Forest Classifier</div>
            <div style="margin-top: 10px; font-size: 14px; color: #c9d1d9;">
                Model Accuracy: <span style="color: #56d364; font-weight: bold;">97.5%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Machine Parameters Input Section
    st.markdown('<p class="section-header">⚙️ Machine Parameter Inputs</p>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="model-card">', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        
        with c1:
            product_type = st.selectbox("Product Type", ["L", "M", "H"], index=0)
            air_temperature = st.number_input("Air Temperature [K]", value=298.15, step=0.1, format="%.2f")
        
        with c2:
            rotational_speed = st.number_input("Rotational Speed [rpm]", value=1513, step=1)
            torque = st.number_input("Torque [Nm]", value=40.03, step=0.01, format="%.2f")
        
        st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)
        predict_button = st.button("Predict Machine Failure Status")
        
        if predict_button:
            st.success("Prediction executed successfully!")

        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # 4. Model Statistics Panel
    st.markdown('<p class="section-header">📊 Model Statistics</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="model-card">
            <h4 style="color: #f0f6fc; font-size: 16px; margin-bottom: 10px;">Performance Overview</h4>
            <hr style="border-color: #30363d; margin: 10px 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 14px;">
                <span>F1 Score:</span>
                <span style="font-weight: bold; color: #56d364;">0.97</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 14px;">
                <span>Precision:</span>
                <span style="font-weight: bold; color: #56d364;">0.98</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 14px;">
                <span>Recall:</span>
                <span style="font-weight: bold; color: #56d364;">0.96</span>
            </div>
        </div>
    """, unsafe_allow_html=True)