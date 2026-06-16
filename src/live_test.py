import joblib
import pandas as pd

def factory_control_panel():
    print("⚙️ Loading the Predictive Maintenance AI Brain...")
    try:
        model = joblib.load('src/predictive_model.pkl')
    except Exception as e:
        print(f"❌ Could not find the saved model file: {e}")
        return

    print("\n🏭 === WELCOME TO THE FACTORY CONTROL PANEL ===")
    print("Enter the current machine telemetry readings to check status:\n")

    try:
        air_temp = float(input("实时 🌡️ Air Temperature (Kelvin) [Normal is ~298]: "))
        proc_temp = float(input("🔥 Process Temperature (Kelvin) [Normal is ~308]: "))
        speed = float(input("🔄 Rotational Speed (RPM) [Normal is ~1500]: "))
        torque = float(input("💪 Torque (Nm) [Normal is ~40]: "))
        wear = float(input("⏳ Tool Wear (Minutes) [Normal is ~0 to 200]: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    custom_data = pd.DataFrame([{
        'air_temp_k': air_temp,
        'process_temp_k': proc_temp,
        'rotational_speed_rpm': speed,
        'torque_nm': torque,
        'tool_wear_min': wear
    }])

    prediction = model.predict(custom_data)[0]
    probabilities = model.predict_proba(custom_data)[0]
    failure_risk = probabilities[1] * 100

    print("\n================= AI ANALYSIS REPORT =================")
    if prediction == 0:
        print(f"🟢 STATUS: SAFE (Machine operating normally)")
        print(f"📉 Breakdown Risk: {failure_risk:.1f}%")
    else:
        print(f"🚨 WARNING: FAILURE IMMINENT! Schedule Emergency Maintenance!")
        print(f"📈 Breakdown Risk: {failure_risk:.1f}%")
    print("======================================================")

if __name__ == "__main__":
    factory_control_panel()