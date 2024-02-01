## Time Stories API
This repository contains a Flask application that serves as an API for retrieving the latest stories from Time.com without using any internal or external libraries/packages

## Setup
Clone the repository to your local machine:

 git clone <repository-url>
1. Navigate to the project directory:
cd <repository-directory>

2. Install the required dependencies using pip:

pip install -r requirements.txt


## Usage

Run the Flask application by executing the following command:

python app.py
Once the application is running, you can access the API endpoint to retrieve the latest Time stories.

GET /getTimeStories
## Parameters
num_stories (optional): Number of latest stories to retrieve. Default is set to 6 if not provided.
Example usage:
GET /getTimeStories?num_stories=10
This will return the 10 latest stories from Time.com.

## Endpoint Details
Endpoint: /getTimeStories
Method: GET <br>
Query Parameters:
num_stories (optional): Number of latest stories to retrieve. Defaults to 6 if not provided.
Response: JSON array containing the latest stories with each story having the following attributes:
title: Title of the story.
link: URL link to the full story.
## Response
json

[
  {
    "link": "/6590760/indian-opposition-leader-hemant-soren-arrested-elections/",
    "title": "Indian Opposition Leader Arrested Months Before Elections"
  },
  {
    "link": "/6590750/taylor-swift-super-bowl-sports-betting-rules/",
    "title": "Las Vegas: No Betting Allowed on Taylor Swift Attending the Super Bowl"
  },
  {
    "link": "/6590720/new-on-netflix-february-2024/",
    "title": "What's New on Netflix in February 2024"
  },
  {
    "link": "/6590643/iran-executions/",
    "title": "Iran Execution Campaign"
  },
  {
    "link": "/6590711/deepfake-protection-federal-bill/",
    "title": "How a New Bill Could Protect Against Deepfakes"
  },
  {
    "link": "/6590470/csam-ai-tech-ceos/",
    "title": "AI Complicates Crackdown on Child Abuse Images"
  }
]
