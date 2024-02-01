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
num_stories (optional): Number of latest stories to retrieve. Default is set to 6 if not provided. <br>
Example usage: <br>
GET /getTimeStories?num_stories=10 <br>
This will return the 10 latest stories from Time.com.

## Endpoint Details
Endpoint: /getTimeStories <br>
Method: GET <br>
Query Parameters: <br>
num_stories (optional): Number of latest stories to retrieve. Defaults to 6 if not provided. <br>
Response: JSON array containing the latest stories with each story having the following attributes:<br>
title: Title of the story.<br>
link: URL link to the full story.
## Response
json

[ <br>
  { <br>
    "link": "/6590760/indian-opposition-leader-hemant-soren-arrested-elections/", <br>
    "title": "Indian Opposition Leader Arrested Months Before Elections" <br>
  }, <br>
  { <br>
    "link": "/6590750/taylor-swift-super-bowl-sports-betting-rules/", <br>
    "title": "Las Vegas: No Betting Allowed on Taylor Swift Attending the Super Bowl" <br>
  }, <br>
  { <br>
    "link": "/6590720/new-on-netflix-february-2024/", <br>
    "title": "What's New on Netflix in February 2024" <br>
  }, <br>
  { <br>
    "link": "/6590643/iran-executions/", <br>
    "title": "Iran Execution Campaign" <br>
  }, <br>
  { <br>
    "link": "/6590711/deepfake-protection-federal-bill/", <br>
    "title": "How a New Bill Could Protect Against Deepfakes" <br>
  }, <br>
  { <br>
    "link": "/6590470/csam-ai-tech-ceos/", <br>
    "title": "AI Complicates Crackdown on Child Abuse Images" <br>
  } <br>
]
