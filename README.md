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
