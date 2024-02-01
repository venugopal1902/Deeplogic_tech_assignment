## Time Stories API
This repository contains a Flask application that serves as an API for retrieving the latest stories from Time.com without using any internal or external libraries/packages

## Setup
Clone the repository to your local machine:
```bash
 git clone <repository-url>
1. Navigate to the project directory:
cd <repository-directory>

2. Install the required dependencies using pip:

pip install -r requirements.txt```


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
Method: GET
Query Parameters:
num_stories (optional): Number of latest stories to retrieve. Defaults to 6 if not provided.
Response: JSON array containing the latest stories with each story having the following attributes:
title: Title of the story.
link: URL link to the full story.
## Example Response
json
Copy code
[
    {
        "title": "Story Title 1",
        "link": "https://example.com/story1"
    },
    {
        "title": "Story Title 2",
        "link": "https://example.com/story2"
    },
    ...
]

