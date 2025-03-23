# Internal User Audit Automation Tool
This Python script simulates a real-world automation project for a cybersecurity analyst. It reads employee login data and identifies users who may be security risks due to inactivitiy or being marked inactive 

#Simple terms what the code accomplishes
- Reads user login data from a CSV file
- Flags users who:
  - Haven't logged in for 90+ days
  - Are marked as inactive
  - Generates a report and logs each run

🚀 How to Run It

  Run - python audit_tool.py 
