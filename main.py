import pprint

import pandas as pd

from broker.zerodha_client import get_kite_client
from config.config_loader import load_config


def main():
    print("========================================")
    print("  QUANTS SIMULATOR ENGINE STARTING... ")
    print("========================================")

    # ------------------------------------------------
    # Load Configurations
    # ------------------------------------------------
    config = load_config()
    print(config)

    # ------------------------------------------------
    # Zerodha login
    # ------------------------------------------------
    print("Connecting to Zerodha...")
    kite = get_kite_client()
    enctoken = kite.enctoken
    user_id = config["zerodha"]["user_id"]
    print("Login successful")

    profile = kite.profile()
    user_name = profile.get('user_shortname')
    print(f"Logged in: {user_name}")

    print("My Zerodha Profile")
    pprint.pprint(kite.profile())

    print("My Holdings")
    pprint.pprint(kite.holdings())

    print("My Positions")
    pprint.pprint(kite.positions())

    # ------------------------------------------------
    # Instruments Master File
    # ------------------------------------------------
    # Download
    try:
        print("[INFO] Downloading instruments, please wait...")
        all_instruments = kite.instruments()
        df = pd.DataFrame(all_instruments)

        filtered_df = df[df['exchange'].isin(['NSE', 'NFO', 'BSE'])]
        filtered_df.to_csv("data/Instruments.csv", index=False)
        print(f"[SUCCESS] Saved {len(filtered_df)} instruments CSV file'.")
    except Exception as e:
        print(f"[ERROR] Failed to fetch instruments: {e}")

    # Read

if __name__ == "__main__":
    main()