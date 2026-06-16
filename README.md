# 🛠️ Predictive Maintenance Data Pipeline & Dashboard

An end-to-end data science immersion project that extracts factory telemetry data from a PostgreSQL database, trains a Machine Learning model to predict equipment failure, and serves an interactive web dashboard.

---

## 🎯 Project Overview
This project simulates a modern manufacturing plant monitoring system. It showcases a complete pipeline where real-time sensor metrics (temperature, rotational speed, torque, and tool wear) are evaluated by a machine learning model to predict equipment failures before they happen, allowing for proactive factory maintenance.

---

## 🏗️ Architecture & Core Concepts Learnt

* **Database Management:** Configured a local **PostgreSQL** instance to host over 10,000 rows of historical factory sensor logs (`predictive_maintenance`).
* **Data Pipeline (`src/data_pipeline.py`):** Utilized **SQLAlchemy** to establish a secure programmatic bridge between Python and SQL, pulling live database entries into **Pandas DataFrames** for processing.
* **Machine Learning (`src/train_model.py`):** Implemented a **RandomForest Classifier** via `scikit-learn`. The training process includes an 80/20 train-test split, model optimization, evaluation via classification reports, and binary model serialization using `joblib`.
* **Frontend Dashboard (`src/app.py`):** Built a web interface using **Streamlit** to load the frozen model (`predictive_model.pkl`) and provide real-time interactive parameter optimization via sliders.

* # 📊 Predictive Maintenance Dataset Documentation

This directory contains the telemetry dataset used to train the machine learning model. The data tracks the operational boundary limits of industrial manufacturing machinery to predict sudden mechanical breakdowns.

---

## 🌎 Data Source & Attribution
* **Source:** Kaggle Marketplace
* **Dataset Name:** Predictive Maintenance Dataset
* **Observations:** 10,000 operational data points (rows)
* **Target Variable:** `Target` (Binary classification for machine failure)

---

## 📋 Data Schema & Feature Dictionary

The dataset tracks structural and thermal stresses across the following features:

| Column Name | Data Type | Description | Technical Context |
| :--- | :--- | :--- | :--- |
| **UDI** | Integer | Unique Data Identifier | A sequential row index from 1 to 10,000. |
| **Product ID** | String / Object | Specific Equipment Serial Code | Begins with a letter variant indicating quality scale: **L** (Low, 50%), **M** (Medium, 30%), or **H** (High, 20%). |
| **Type** | String / Object | Material Quality Variant | Explicitly maps out the quality tier of the tool set (`L`, `M`, or `H`). |
| **Air Temperature [K]** | Float | Ambient Room Temperature | Standardized room temperature simulation tracked in Kelvin. |
| **Process Temperature [K]** | Float | Structural Machine Temperature | Internal warmth generated during active tool operation. Dynamically coupled to the Air Temperature ($\approx \text{Air Temp} + 10\text{K}$). |
| **Rotational Speed [rpm]** | Integer | Spindle Rotational Velocity | Revolutions per minute derived from power inputs. Displays characteristic drops under high torque loads. |
| **Torque [Nm]** | Float | Torsional Force Output | Torque forces distributed around a central machine baseline of 40 Nm. |
| **Tool Wear [min]** | Integer | Cumulative Stress Duration | The total active minutes the cutting tool element has been continuously used during production. |
| **Target** | Integer (Binary) | Failure Status Flag | The prediction label: **`0`** (Normal Operation), **`1`** (Equipment Failure occurred). |

---

## 🛠️ Failure Mode Distribution (Context)
A machine failure (`Target = 1`) indicates that the equipment broke down due to one of five specific physical thresholds being breached:
1. **Tool Wear Failure (TWF):** The tool element exceeded safe wear duration.
2. **Heat Dissipation Failure (HDF):** Thermal difference between ambient air and active processing was too tight.
3. **Power Failure (PWF):** The product of torque and speed fell outside the operational power limits.
4. **Overstrain Failure (OSF):** Cumulative tool wear combined with extreme torque exceeded structural load limitations.
5. **Random Failures (RNF):** Sudden unmapped mechanical breakdowns.
