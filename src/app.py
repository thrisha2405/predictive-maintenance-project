import streamlit as st
import joblib
import pandas as pd

# 1. Design a beautiful Header for our Web App
st.set_page_config(page_title="Predictive Maintenance Hub", page_icon="⚙️", layout="centered")
st.title("⚙️ AI Factory Control Panel")
st.markdown("---")
st.subheader("Live Telemetry Diagnostics")
st.write("Adjust the sliders below to simulate live machine sensors. Our AI model will calculate the structural breakdown risk in real-time.")

# 2. Load the AI Model Brain we saved earlier
@st.cache_resource  # This line keeps the app fast by loading the brain only once!
def load_ai_brain():
    return joblib.load('src/predictive_model.pkl')

model = load_ai_brain()

# 3. Build Interactive Visual Sliders for the User
st.sidebar.header("🕹️ Sensor Controls")
air_temp = st.sidebar.slider("🌡️ Air Temperature (Kelvin)", min_value=290.0, max_value=315.0, value=298.0, step=0.1)
proc_temp = st.sidebar.slider("🔥 Process Temperature (Kelvin)", min_value=300.0, max_value=325.0, value=308.0, step=0.1)
speed = st.sidebar.slider("🔄 Rotational Speed (RPM)", min_value=1000, max_value=3500, value=1500, step=10)
torque = st.sidebar.slider("💪 Mechanical Torque (Nm)", min_value=5.0, max_value=90.0, value=40.0, step=0.5)
wear = st.sidebar.slider("⏳ Tool Wear Runtime (Minutes)", min_value=0, max_value=300, value=10, step=1)

# 4. Pack the slider variables into a miniature dataset structure for the AI
input_data = pd.DataFrame([{
    'air_temp_k': air_temp,
    'process_temp_k': proc_temp,
    'rotational_speed_rpm': speed,
    'torque_nm': torque,
    'tool_wear_min': wear
}])

# 5. Execute Live Risk Calculations
prediction = model.predict(input_data)[0]
probabilities = model.predict_proba(input_data)[0]
failure_risk = probabilities[1] * 100

# 6. Display the Visual Outputs to the Webpage
st.markdown("### 📊 Real-Time AI Diagnosis Report")

# Create a clean layout with columns
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Calculated Failure Probability", value=f"{failure_risk:.1f}%")

with col2:
    if prediction == 0:
        st.success("🟢 STATUS: COMPONENT STABLE")
    else:
        st.error("🚨 WARNING: DEFECT IMMINENT")

# Add a user-friendly alert message
if failure_risk > 50.0:
    st.warning("⚠️ **System Alert:** Machine metrics are exceeding safety limits. Schedule preventative maintenance immediately to avoid factory downtime.")
else:
    st.info("ℹ️ **System Log:** Machinery is operating within nominal safety parameters.")