import pandas as pd
from datetime import datetime 
import os

def audit_user_data(csv_path): 
    try: 
        # Check if file exists 
        if not os.path.exists(csv_path): 
            print (f"[!] File '{csv_path}' not found.") 
            return 
        
        # Read the CSV file 
        df = pd.read_csv(csv_path) 

        # Handle empty files 
        if df.empty: 
            print("[!} CSV file is empty. No data to audit.") 
            return 
        
        # Check required columns exist 
        required_columns = {'last_login', 'days_inactive', 'active'} 
        if not required_columns.issubset(df.columns):
            print(f"[!] CSV is missing one or more required columns: {required_columns}")
            return 
        
        # Convert the last login to datetime 
        df['last_login'] = pd.to_datetime(df['last_login'], errors='coerce')

        # Get today's date
        now = datetime.now()

        # Calculate the days since last login
        df['days_since_last_login'] = (now - df['last_login']).dt.days

        # Flag users with problems
        flagged = df[(df['days_inactive'] > 90) | (df['active'].str.lower() == 'no')]

        # Save results to the report
        os.makedirs("reports", exist_ok=True)
        flagged.to_csv("reports/sample_audit_report.csv", index=False)
        print(f"[+] Audit complete. Found {len(flagged)} users that need review.")

        # Logging the run
        os.makedirs("logs", exist_ok=True)
        with open("logs/run_log.txt", "a") as log:
            log.write(f"Audit run at {now} - Flagged: {len(flagged)} users\n")

    except pd.errors.EmptyDataError:
        print("[!] CSV file is empty or malformed.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

# Run it
if __name__ == "__main__":
    audit_user_data("internal_users.csv")







