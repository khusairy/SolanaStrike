from solana.keypair import Keypair
from solana.rpc.api import Client
from config import CONFIG, print_config
import base58
import os

# Function to create a new wallet
def create_wallet():
    # Generate a new keypair (public/private keys)
    new_keypair = Keypair()

    # Get the public key (Base58 encoding)
    public_key = new_keypair.public_key
    private_key = new_keypair.secret_key

    # Display the new wallet information
    print(f"New wallet created!")
    print(f"Public Key: {public_key}")
    print(f"Private Key (Base58 Encoded): {base58.b58encode(private_key).decode('utf-8')}")

    # Optionally, save the private key to a file (if needed for future use)
    with open("new_wallet_keypair.json", "w") as wallet_file:
        wallet_data = {
            "public_key": str(public_key),
            "private_key": base58.b58encode(private_key).decode("utf-8")
        }
        wallet_file.write(str(wallet_data))

    print("Wallet keypair saved to new_wallet_keypair.json")

# Function to snipe tokens (existing function for token sniping)
def snipe_token():
    # Initialize Solana client
    client = Client(CONFIG["RPC_URL"])

    # Print configuration for confirmation
    print_config()

    print(f"Attempting to buy tokens with {CONFIG['BUY_AMOUNT']} SOL from wallet {CONFIG['PUBLIC_KEY']}.")

    # Add logic for token sniping

if __name__ == "__main__":
    # Ask user if they want to create a new wallet or use existing config
    print("Do you want to create a new wallet? (yes/no)")
    choice = input().lower()

    if choice == "yes":
        create_wallet()
    else:
        snipe_token()
