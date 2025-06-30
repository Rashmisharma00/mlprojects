import logging
import os
from datetime import datetime

# Step 1: Generate log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Step 2: Create logs/ if not exists
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Step 3: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s"
)

# Step 4: Write a test log
logging.info("✅ This is a test log message.")
print("✔️ Logging complete. Check the 'logs/' directory.")


