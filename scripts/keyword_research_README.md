# Keyword Research Tool

## Setup Instructions
1. Install dependencies:
```bash
pip install requests python-dotenv
```

2. Create `.env` file with API credentials:
```ini
# Get credentials from respective API providers
DATAFORSEO_USER=your_username
DATAFORSEO_PASS=your_password
SEMRUSH_API_KEY=your_key
AHREFS_API_KEY=your_key
```

## Usage Examples
1. Single keyword analysis:
```bash
python keyword_research_tool.py "supply chain innovators"
```

2. Bulk analysis from file:
```bash
python keyword_research_tool.py -f keywords.txt
```

## API Support
**Currently Integrated Service**:  
- **DataForSEO** (Search Volume API)  
  - Environment Variable: `DATAFORSEO_USER/PASS`  
  - Documentation: [https://developer.dataforseo.com/](https://developer.dataforseo.com/)  

*Other services removed per user request - Jan 2026*

## Testing Without Credentials
```python
# Enable mock mode in the script
os.environ["MOCK_MODE"] = "true"
python keyword_research_tool.py "test keyword"
```

**Mock Response Format**:
```json
[
  {
    "keyword": "test keyword",
    "search_volume": 650,
    "competition": 0.35,
    "cpc": 1.20,
    "difficulty": 42
  }
]
```
