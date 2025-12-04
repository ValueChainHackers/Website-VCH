import argparse
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import json
import time
from pathlib import Path

def fetch_keyword_volumes(keywords, location_id="2076", customer_id="123-456-7890"):
    """Fetches keyword metrics using Google Ads API with test account defaults."""
    try:
        # Initialize client - User must set up credentials in google-ads.yaml
        googleads_client = GoogleAdsClient.load_from_storage(version="v16")
        
        keyword_plan_idea_service = googleads_client.get_service("KeywordPlanIdeaService")
        
        request = googleads_client.get_type("GenerateKeywordIdeasRequest")
        request.customer_id = customer_id
        request.language = googleads_client.get_service("GoogleAdsService").language_constant_path("1000")  # English
        request.geo_target_constants = [googleads_client.get_service("GoogleAdsService").geoTargetConstantPath(location_id)]
        request.include_adult_keywords = False
        
        # Build keyword seeds
        request.keyword_seed.keywords.extend(keywords)
        
        # Execute request
        response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
        
        results = []
        for idea in response:
            results.append({
                "keyword": idea.text,
                "avg_monthly_searches": idea.keyword_idea_metrics.avg_monthly_searches,
                "competition": idea.keyword_idea_metrics.competition.name,
                "cpc_micros": idea.keyword_idea_metrics.cpc_bid_micros
            })
            
        return results
        
    except GoogleAdsException as e:
        print(f"Google Ads API error: {e}")
        return None
    except Exception as e:
        print(f"General error: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Fetch Google Keyword Planner volumes')
    parser.add_argument('keywords', nargs='+', help='Keywords to check')
    parser.add_argument('--location', default="2076", help='Location ID (NL=2076)')
    parser.add_argument('--output', required=True, help='Output JSON path')
    args = parser.parse_args()
    
    try:
        # API call with retry
        for attempt in range(3):
            data = fetch_keyword_volumes(args.keywords, args.location)
            if data is not None:
                break
            print(f"Retry #{attempt+1} after 5s...")
            time.sleep(5)
        else:
            raise Exception("Failed after 3 attempts")
        
        # Save output
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump({
                "keywords": args.keywords,
                "location_id": args.location,
                "data": data
            }, f, indent=2)
            
        print(f"Successfully saved to {output_path}")
        
    except Exception as e:
        print(f"Critical error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
