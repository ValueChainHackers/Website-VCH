#!/usr/bin/env python3
"""
Download partner logos from various sources.
This script attempts to download official logos for VCH partners.
"""

import requests
import os
from pathlib import Path

# Create partners directory if it doesn't exist
PARTNERS_DIR = Path('assets/images/partners')
PARTNERS_DIR.mkdir(parents=True, exist_ok=True)

# Logo URLs - These are example URLs, you may need to update them with actual direct download links
LOGOS = {
    'scania-logo.svg': 'https://worldvectorlogo.com/download/scania-3.svg',
    'puma-logo.svg': 'https://worldvectorlogo.com/download/puma-logo.svg',
    'danone-logo.svg': 'https://worldvectorlogo.com/download/danone.svg',
}

def download_logo(url: str, filename: str):
    """Download a logo from URL and save to partners directory."""
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()

        filepath = PARTNERS_DIR / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully downloaded {filename} ({len(response.content)} bytes)")
        return True
    except Exception as e:
        print(f"✗ Error downloading {filename}: {e}")
        return False

def main():
    """Main function to download all partner logos."""
    print("=== Partner Logo Downloader ===\n")

    success_count = 0
    total_count = len(LOGOS)

    for filename, url in LOGOS.items():
        if download_logo(url, filename):
            success_count += 1
        print()

    print(f"\n=== Summary ===")
    print(f"Successfully downloaded: {success_count}/{total_count} logos")

    if success_count < total_count:
        print("\n⚠ Note: Some logos failed to download.")
        print("You may need to:")
        print("1. Visit the logo websites manually")
        print("2. Update the URLs in this script with direct download links")
        print("3. Contact partners directly for their logos")
        print("\nSee docs/partner-logos-download-guide.md for more information.")

if __name__ == '__main__':
    main()
