import argparse
from pytrends.request import TrendReq
import pandas as pd
import time
import json
from pathlib import Path

def fetch_trends_data(keywords, geo='NL', sleep_seconds=5, retries=3):
    """Fetches Google Trends data without API key using pytrends."""
    pytrends = TrendReq(hl='en-US', tz=360)
    data = {}
    
    for kw in keywords:
        for attempt in range(retries):
            try:
                pytrends.build_payload([kw], geo=geo)
                interest_over_time = pytrends.interest_over_time()
                if not interest_over_time.empty:
                    data[kw] = {
                        'average_interest': float(interest_over_time[kw].mean()),
                        'recent_trend': float(interest_over_time[kw].tail(3).mean()),
                        'is_partial': bool(interest_over_time['isPartial'].any())
                    }
                break
            except Exception as e:
                print(f"Attempt {attempt+1} failed for '{kw}': {str(e)}")
                time.sleep(sleep_seconds)
        else:
            print(f"Skipping '{kw}' - permanent failure after {retries} attempts")
            continue  # Don't return empty data point
    
    return data

def main():
    parser = argparse.ArgumentParser(description='Fetch Google Trends data')
    parser.add_argument('keywords', nargs='+', help='Keywords to search')
    parser.add_argument('--geo', default='NL', help='Geographic location (default: NL)')
    parser.add_argument('--output', required=True, help='Output JSON path')
    args = parser.parse_args()

    result = fetch_trends_data(args.keywords, args.geo)
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump({
            'geo': args.geo,
            'keywords': args.keywords,
            'data': result
        }, f, indent=2)
    
    print(f"Trends data saved to {output_path}")

if __name__ == "__main__":
    main()
