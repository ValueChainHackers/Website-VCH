import requests
import json
import sys
import os

# Configuration (Only DataForSEO implemented)
API_CREDENTIALS = {
    "dataforseo": (os.getenv("DATAFORSEO_USER"), os.getenv("DATAFORSEO_PASS"))
}

def dataforseo_keyword_analysis(keywords):
    """Fetch keyword data using DataForSEO API"""
    # Check if credentials exist
    if not all(API_CREDENTIALS['dataforseo']):
        print("No DataForSEO credentials found - using mock data")
        return generate_mock_data(keywords)
        
    url = "https://api.dataforseo.com/v3/keywords_data/google/search_volume/live"
    headers = {
        "Authorization": f"Basic {API_CREDENTIALS['dataforseo'][0]}:{API_CREDENTIALS['dataforseo'][1]}",
        "Content-Type": "application/json"
    }
    data = [{"keyword": kw, "location_code": 2840} for kw in keywords]  # 2840 = Netherlands
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"DataForSEO API Error: {str(e)} \nFalling back to mock data")
        return generate_mock_data(keywords)

def generate_mock_data(keywords):
    """Generate enhanced mock data with SEO insights"""
    return {
        "tasks": [
            {
                "result": [
                    {
                        "keyword": kw,
                        "search_volume": len(kw)*10 + 50,
                        "competition": 0.3 + (i*0.1),
                        "high_top_of_page_bid": 1.2 + (i*0.5),
                        "keyword_difficulty": 40 + (i*5),
                        "competitors": [
                            {"domain": f"competitor{i+1}.com", "position": j+1}
                            for j in range(3)
                        ],
                        "monthly_trends": [max(10, len(kw)*2 + (m*5)) for m in range(12)],
                        "related_terms": [f"{kw.split()[0]} {word}" for word in ["analytics", "solutions", "platform"]],
                        "serp_features": ["featured_snippet"] if i % 2 == 0 else []
                    }
                    for i, kw in enumerate(keywords)
                ]
            }
        ]
    }

def parse_keyword_data(api_response, service="dataforseo"):
    """Parse response from different API services"""
    results = []
    
    if service == "dataforseo" and api_response.get("tasks"):
        for task in api_response["tasks"]:
            for result in task.get("result", []):
                results.append({
                    "keyword": result.get("keyword"),
                    "search_volume": result.get("search_volume"),
                    "competition": result.get("competition"),
                    "cpc": result.get("high_top_of_page_bid"),
                    "difficulty": result.get("keyword_difficulty"),
                    "competitors": result.get("competitors", []),
                    "monthly_trends": result.get("monthly_trends", []),
                    "related_terms": result.get("related_terms", []),
                    "serp_features": result.get("serp_features", [])
                })
    # Add parsers for other services here
    
    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: python keyword_research_tool.py <keyword> [additional_keywords...]")
        print("   or: python keyword_research_tool.py -f <keywords_file.txt>")
        sys.exit(1)
    
    keywords = []
    if sys.argv[1] == "-f":
        with open(sys.argv[2], "r") as f:
            keywords = [line.strip() for line in f if line.strip()]
    else:
        keywords = sys.argv[1:]
    
    # Get data from selected service
    results = dataforseo_keyword_analysis(keywords)
    
    if results:
        formatted_report = []
        for item in parse_keyword_data(results):
            report = f"""
### {item['keyword']} Analysis
**Search Volume**: {item['search_volume']}/month  
**Competition**: {item['competition']:.1f} (0=Low, 1=High)  
**SEO Difficulty**: {item['difficulty']}/100  
**Avg. CPC**: ${item['cpc']:.2f}

#### Top Competitors
{'\n'.join([f"- {c['domain']} (Position #{c['position']})" for c in item['competitors']])}

#### Monthly Trends
{' █' * int(item['search_volume']/50)} {item['search_volume']} searches

#### Related Terms
{', '.join(item['related_terms'][:3])}

#### SERP Features
{', '.join(item['serp_features']) or 'None detected'}"""
            formatted_report.append(report)
            
        print("\n\n".join(formatted_report))
    else:
        print("No results obtained from API")

if __name__ == "__main__":
    main()
