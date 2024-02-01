from flask import Flask, jsonify, request
import requests
import re

app = Flask(__name__)

def get_latest_stories(num_stories):
    url = "https://time.com"
    response = requests.get(url)
    html_content = response.text
    
    # Extract content within the specified div tag
    pattern = r'<div class="partial latest-stories" data-module_name="Latest Stories">(.*?)</div>'
    match = re.search(pattern, html_content, re.DOTALL)
    
    if match:
        div_content = match.group(1)
        
        # Regular expression to find the latest stories within the extracted div content
        story_pattern = r'<li class="latest-stories__item">\s*<a href="([^"]+)">\s*<h3 class="latest-stories__item-headline">(.*?)</h3>\s*</a>'
        stories = re.findall(story_pattern, div_content)[:num_stories]
        
        # Construct JSON object array
        stories_json = [{"title": title.strip(), "link": link} for link, title in stories]
        
        return stories_json
    else:
        return []

@app.route('/getTimeStories')
def get_time_stories():
    num_stories = request.args.get('num_stories', default=6, type=int)
    stories = get_latest_stories(num_stories)
    return jsonify(stories)

if __name__ == '__main__':
    app.run(debug=True)
