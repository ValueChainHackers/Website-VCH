import glob
import os
import re
from datetime import datetime

def compile_reports():
    report_dir = "business-documentation/keyword_reports"
    output_file = "business-documentation/MASTER_KEYWORD_ANALYSIS.md"
    reports = glob.glob(f"{report_dir}/*_report.md")
    
    if not reports:
        print("No individual reports found")
        return
    
    master_content = f"""# Master Keyword Analysis Report
*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*  
**Total Names Analyzed**: {len(reports)}  

## Table of Contents
"""

    metrics_table = """## Comparative Metrics
| Name | Volume | Difficulty | CPC | Competition | Sentiment |
|------|--------|------------|-----|-------------|-----------|
"""
    
    # Process each report
    reports_content = "\n## Individual Reports\n"
    for report_path in reports:
        with open(report_path, 'r') as f:
            content = f.read()
            name = extract_name(content)
            metrics = extract_metrics(content)
            
            # Register in table of contents
            clean_name = name.replace(' ', '-').lower()
            master_content += f"- [{name}](#{clean_name}-metrics)\n"
            
            # Add to metrics table
            metrics_table += f"| [{name}](./keyword_reports/{os.path.basename(report_path)}) " \
                             f"| {metrics['volume']} | {metrics['difficulty']} " \
                             f"| ${metrics['cpc']} | {metrics['competition']} " \
                             f"| {metrics['sentiment']}/10 |\n"
            
            # Add report excerpts
            reports_content += f"### {name} Metrics\n{content}\n\n---\n"
    
    # Compile final output
    final_content = (
        master_content + "\n" + 
        metrics_table + "\n" +
        reports_content
    )

    with open(output_file, 'w') as f:
        f.write(final_content)
    print(f"Master report generated at: {output_file}")

def extract_name(content):
    match = re.search(r'# (.+) Analysis Report', content)
    return match.group(1) if match else "Unknown"

def extract_metrics(content):
    """Extract key metrics from report content with error handling"""
    metrics = {
        'volume': 0,
        'difficulty': 0.0,
        'cpc': 0.0,
        'competition': 0.0,
        'sentiment': 5  # Default neutral score
    }
    
    # Extract values with fallbacks
    try:
        vol_match = re.search(r'DataForSEO.*?\| (\d+)', content)
        if vol_match:
            metrics['volume'] = int(vol_match.group(1))
    except Exception:
        pass
    
    try:
        diff_match = re.search(r'DataForSEO.*?\|\s*(\d+\.?\d*)', content)
        if diff_match:
            metrics['difficulty'] = float(diff_match.group(1))
    except Exception:
        pass
    
    try:
        cpc_match = re.search(r'\$(\d+\.\d+)', content)
        if cpc_match:
            metrics['cpc'] = float(cpc_match.group(1))
    except Exception:
        pass
    
    try:
        comp_match = re.search(r'Competition.*?\|\s*(\d+\.\d+)', content)
        if comp_match:
            metrics['competition'] = float(comp_match.group(1))
    except Exception:
        pass
    
    try:
        sent_match = re.search(r'Overall Score": (\d+)', content)
        if sent_match:
            metrics['sentiment'] = int(sent_match.group(1))
    except Exception:
        pass
        
    return metrics

if __name__ == "__main__":
    compile_reports()
