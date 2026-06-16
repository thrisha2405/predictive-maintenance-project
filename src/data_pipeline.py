import pandas as pd
from sqlalchemy import create_engine

def fetch_factory_data():
    print("🔌 Establishing pipeline connection to PostgreSQL...")
    
    # 1. Define the database credentials connection string
    # Syntax: postgresql://username:password@localhost:port/database_name
    # Assuming your default Postgres password is 'postgres' - change if you set a custom one!
    conn_string = "postgresql://postgres:admin123@localhost:5432/factory_operations"
    try:
        # 2. Create the database connection engine
        engine = create_engine(conn_string)
        
        # 3. Write our extraction query
        query = "SELECT * FROM asset_telemetry;"
        
        print("📥 Extracting 10,000 telemetry rows from 'asset_telemetry' table...")
        # 4. Stream the SQL table straight into a Pandas DataFrame
        df = pd.read_sql(query, con=engine)
        
        print("✅ Extraction Complete!")
        print(f"📊 Data Frame Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")
        
        # 5. Print a quick preview of the incoming production data
        print("📋 Telemetry Stream Preview:")
        print(df[['ud_id', 'product_id', 'air_temp_k', 'rotational_speed_rpm', 'machine_failure']].head())
        
        return df

    except Exception as e:
        print(f"❌ Pipeline Failure: {str(e)}")
        print("\n💡 Tip: Double check if your pgAdmin password matches 'postgres' in the connection string.")
        return None

if __name__ == "__main__":
    factory_df = fetch_factory_data()