import time
import requests
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Your Render URL
URL = "https://your-app.onrender.com/"  # Replace with your actual URL

def ping():
    try:
        response = requests.get(URL)
        logger.info(f"Ping status: {response.status_code}, Time: {datetime.now()}")
    except Exception as e:
        logger.error(f"Ping failed: {str(e)}")

def main():
    logger.info("Starting ping service...")
    while True:
        ping()
        time.sleep(840)  # 14 minutes

if __name__ == "__main__":
    main() 