import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
# Import the connection function we successfully built in our other file!
from data_pipeline import fetch_factory_data

def train_predictive_model():
    # 1. Fetch the data from our PostgreSQL pipeline
    df = fetch_factory_data()
    if df is None:
        print("❌ Model training aborted: Could not fetch data.")
        return

    print("🧠 Starting AI Model Training Workflow...")

    # 2. Select Features (X) and Target (y)
    # We choose numerical sensor data that indicates machine stress
    feature_cols = ['air_temp_k', 'process_temp_k', 'rotational_speed_rpm', 'torque_nm', 'tool_wear_min']
    X = df[feature_cols]
    y = df['machine_failure']

    # 3. Split data into Training set (80%) and Testing set (20%)
    # This lets us test the AI on data it has never seen before to prove it works!
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print(f"📊 Split data into {X_train.shape[0]} training rows and {X_test.shape[0]} evaluation testing rows.")

    # 4. Initialize our AI Model (The Random Forest)
    print("🌲 Breeding a Random Forest of 100 Decision Trees...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # 5. Train the model (This is where the actual "learning" happens!)
    print("🏋️‍♂️ Training the AI to recognize failure patterns... (Fitting model)")
    model.fit(X_train, y_train)
    print("✨ Training complete!")

    # 6. Evaluate the AI's predictions
    print("🔮 Putting the AI to the test against unseen evaluation data...")
    predictions = model.predict(X_test)

    # 7. Print the results
    accuracy = accuracy_score(y_test, predictions)
    print("\n================== AI PERFORMANCE REPORT ==================")
    print(f"🎯 Overall Model Accuracy: {accuracy * 100:.2f}%")
    print("\nDetailed Breakdown:")
    print(classification_report(y_test, predictions, target_names=['Normal Operation', 'Machine Failure']))
    print("===========================================================")

    import joblib
    joblib.dump(model, 'src/predictive_model.pkl')
    print("💾 AI Brain successfully saved to 'src/predictive_model.pkl'!")

if __name__ == "__main__":
    train_predictive_model()

