import finnhub
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Environment variable
FINNHUB_API = os.getenv("FINNHUB_API_KEY")

# Setup client
finnhub_client = finnhub.Client(api_key=FINNHUB_API)

print(finnhub_client.company_profile2(symbol='AAPL'))