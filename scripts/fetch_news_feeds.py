#!/usr/bin/env python3
"""
Fetch RSS feeds and save to Jekyll data files.
This script runs via GitHub Actions to update news content.
"""

import feedparser
import yaml
import re
from datetime import datetime
from typing import List, Dict

# Sustainability & Supply Chain Finance News Sources
SUSTAINABILITY_FEEDS = [
    {
        'url': 'https://www.supplychainbrain.com/rss',
        'name': 'SupplyChainBrain',
        'category': 'supply-chain',
        'icon': 'fa-truck'
    },
    {
        'url': 'https://www.supplychain247.com/rss',
        'name': 'Supply Chain 24/7',
        'category': 'supply-chain',
        'icon': 'fa-box'
    },
    {
        'url': 'https://www.logisticsmgmt.com/rss',
        'name': 'Logistics Management',
        'category': 'supply-chain',
        'icon': 'fa-warehouse'
    },
    {
        'url': 'https://www.circularonline.co.uk/feed/',
        'name': 'Circular Online',
        'category': 'circular',
        'icon': 'fa-recycle'
    },
    {
        'url': 'https://www.bsr.org/en/blog/rss',
        'name': 'BSR Insights',
        'category': 'sustainability',
        'icon': 'fa-leaf'
    },
]

# AI in Supply Chain News Sources
AI_FEEDS = [
    {
        'url': 'https://blog.google/technology/ai/rss',
        'name': 'Google AI Blog',
        'category': 'ai-research',
        'icon': 'fa-google'
    },
    {
        'url': 'https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml',
        'name': 'MIT AI News',
        'category': 'ai-research',
        'icon': 'fa-graduation-cap'
    },
    {
        'url': 'https://www.supplychainbrain.com/topics/technology/artificial-intelligence-ai-machine-learning/rss',
        'name': 'SupplyChainBrain AI',
        'category': 'supply-chain',
        'icon': 'fa-truck'
    },
    {
        'url': 'https://www.kdnuggets.com/feed',
        'name': 'KDnuggets',
        'category': 'machine-learning',
        'icon': 'fa-chart-bar'
    },
]


def strip_html_tags(text: str) -> str:
    """
    Remove HTML tags from text.

    Args:
        text: Text potentially containing HTML tags

    Returns:
        Clean text without HTML tags
    """
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    # Remove extra whitespace
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean


def fetch_feed_articles(feed_info: Dict, max_articles: int = 10) -> List[Dict]:
    """
    Fetch articles from an RSS feed.

    Args:
        feed_info: Dictionary containing feed URL, name, category, and icon
        max_articles: Maximum number of articles to fetch

    Returns:
        List of article dictionaries
    """
    articles = []

    try:
        feed = feedparser.parse(feed_info['url'])

        for entry in feed.entries[:max_articles]:
            # Parse publication date
            pub_date = entry.get('published_parsed') or entry.get('updated_parsed')
            date_str = datetime(*pub_date[:6]).isoformat() if pub_date else datetime.now().isoformat()

            # Get and clean description
            raw_description = entry.get('summary', '')
            clean_description = strip_html_tags(raw_description)
            truncated_description = clean_description[:200] + '...' if len(clean_description) > 200 else clean_description

            article = {
                'title': entry.get('title', 'Untitled'),
                'link': entry.get('link', '#'),
                'description': truncated_description,
                'pub_date': date_str,
                'source': feed_info['name'],
                'category': feed_info['category'],
                'icon': feed_info['icon']
            }
            articles.append(article)

        print(f"[OK] Fetched {len(articles)} articles from {feed_info['name']}")

    except Exception as e:
        print(f"[ERROR] Error fetching {feed_info['name']}: {e}")

    return articles


def main():
    """Main function to fetch all feeds and save to YAML files."""

    # Fetch sustainability news
    print("\n=== Fetching Sustainability News ===")
    sustainability_articles = []
    for feed in SUSTAINABILITY_FEEDS:
        sustainability_articles.extend(fetch_feed_articles(feed))

    # Sort by publication date (newest first)
    sustainability_articles.sort(key=lambda x: x['pub_date'], reverse=True)

    # Save to YAML
    sustainability_data = {
        'last_updated': datetime.now().isoformat(),
        'articles': sustainability_articles[:50]  # Keep top 50
    }

    with open('_data/sustainability_news.yml', 'w') as f:
        yaml.dump(sustainability_data, f, default_flow_style=False, allow_unicode=True)

    print(f"\n[OK] Saved {len(sustainability_articles[:50])} sustainability articles to _data/sustainability_news.yml")

    # Fetch AI news
    print("\n=== Fetching AI News ===")
    ai_articles = []
    for feed in AI_FEEDS:
        ai_articles.extend(fetch_feed_articles(feed))

    # Sort by publication date (newest first)
    ai_articles.sort(key=lambda x: x['pub_date'], reverse=True)

    # Save to YAML
    ai_data = {
        'last_updated': datetime.now().isoformat(),
        'articles': ai_articles[:50]  # Keep top 50
    }

    with open('_data/ai_news.yml', 'w') as f:
        yaml.dump(ai_data, f, default_flow_style=False, allow_unicode=True)

    print(f"[OK] Saved {len(ai_articles[:50])} AI articles to _data/ai_news.yml\n")


if __name__ == '__main__':
    main()
