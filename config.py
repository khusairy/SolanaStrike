import os
from dotenv import load_dotenv

# Load environment variables from .env file (if you're using .env)
load_dotenv()

# Configuration Settings
CONFIG = {
    # Solana Network and Wallet Information
    "RPC_URL": os.getenv("RPC", "https://api.mainnet-beta.solana.com"),  # RPC endpoint
    "PUBLIC_KEY": os.getenv("PUB_KEY", "your_public_key_here"),           # Your public key
    "PRIVATE_KEY": os.getenv("PRIV_KEY", "your_private_key_here"),        # Your private key

    # Buy Amount and Strategy
    "BUY_AMOUNT": float(os.getenv("BUY_AMOUNT", 0.01)),                    # Amount of SOL to use for buying tokens

    # Optional Settings
    "CHECK_TWITTER": os.getenv("CHECK_TWITTER", "false").lower() == "true",  # Check if new pools have Twitter accounts
    "CHECK_WEBSITE": os.getenv("CHECK_WEBSITE", "false").lower() == "true",  # Check if new pools have a website
    "CHECK_TELEGRAM": os.getenv("CHECK_TELEGRAM", "false").lower() == "true" # Check if new pools have a Telegram group
}

# Print the configuration to verify
def print_config():
    print("Configuration Loaded:")
    for key, value in CONFIG.items():
        print(f"{key}: {value}")

# Example usage
if __name__ == "__main__":
    print_config()
