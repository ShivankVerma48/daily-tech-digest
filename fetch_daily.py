import json
import urllib.request
from datetime import datetime, timezone
import os

def fetch_top_stories(limit=5):
    try:
        req = urllib.request.Request(
            "https://hacker-news.firebaseio.com/v0/topstories.json",
            headers={"User-Agent": "DailyDigestBot/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            story_ids = json.loads(response.read().decode())[:limit]
        
        stories = []
        for sid in story_ids:
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
            item_req = urllib.request.Request(item_url, headers={"User-Agent": "DailyDigestBot/1.0"})
            with urllib.request.urlopen(item_req, timeout=10) as res:
                stories.append(json.loads(res.read().decode()))
        return stories
    except Exception as e:
        print(f"Error fetching stories: {e}")
        return []

def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    os.makedirs("digests", exist_ok=True)
    file_path = os.path.join("digests", f"{today}.md")
    
    stories = fetch_top_stories(limit=5)
    
    content = [
        f"# 📰 Daily Tech & Engineering Digest — {today}",
        f"\n*Auto-generated on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}*\n",
        "## Top Hacker News Stories Today\n"
    ]
    
    if stories:
        for idx, story in enumerate(stories, 1):
            title = story.get("title", "No Title")
            url = story.get("url", f"https://news.ycombinator.com/item?id={story.get('id')}")
            score = story.get("score", 0)
            by = story.get("by", "unknown")
            content.append(f"{idx}. **[{title}]({url})** — *Score: {score} | By: {by}*")
    else:
        content.append("No stories retrieved today. Daily heartbeat logged.\n")
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n")
        
    print(f"Successfully generated digest for {today} at {file_path}")

if __name__ == "__main__":
    main()
