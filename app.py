import os
import csv
import openai
from flask import Flask, redirect, render_template, request, url_for

MODEL_NAME = "text-davinci-003"

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
DATASET_PATH = "./data/CAvideos_20_entries.csv"

# Read CSV into list of lists
videos = []
with open(DATASET_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)  # extract headers as first row
    # extract only the useful columns
    for row in reader:
        video = {"title": row[headers.index("title")], "thumbnail_link": row[headers.index("thumbnail_link")], "tags": row[headers.index("tags")], "views": row[headers.index("views")], "likes": row[headers.index("likes")]}
        videos.append(video)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        
        #Get criteria from users' input
        criteria = request.form["criteria"]
        
        # Apply rate function to each row's title and store the summary in a new list
        
        rate (videos, criteria)

        #Sort the data by criteria in descending order
        sorted_data = sorted(videos, key=lambda x: float(x["rating"]), reverse=True)
        
        # Keep only the top 5 videos
        sorted_data = sorted_data[:5]

        return render_template("index.html", result=sorted_data)   
    
    return render_template("index.html")
    
#rate function    
def rate(videos, criteria):
    if any(substring in criteria for substring in ["like", "engagement", "view"]):
        prompt = f'Rate the following videos with these title, tags, like counts, and view by the following criteria - {criteria} - from 0 to 1 in 2 decimal points and return only their ratings as a list of 2 decimal point floats. A video with higher like count should receive a higher rating:\n\n'
    else:
        prompt = f'Rate the following videos with these title, tags, like counts, and view by the following criteria - {criteria} - from 0 to 1 in 2 decimal points and return only their ratings as a list of 2 decimal point floats. A video with video title and tags more relevant to the criter should receive a higher rating:\n\n'
    for i, video in enumerate(videos):
        prompt += f"{i+1}: "
        prompt += f"{video['title']}"
        prompt += f" Tags: {video['tags']}"
        prompt += f" Like count: {video['likes']} "
        prompt += f"Views: {video['views']}\n"
    print(prompt)
    response = openai.Completion.create(
        model=MODEL_NAME,
        prompt=prompt,
        temperature=0.1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ratings = response.choices[0].text.strip()
    ratings = ratings.strip("[")
    ratings = ratings.strip("]")
    ratings_list = [float(rating) for rating in ratings.split(", ")]
    print(ratings_list)
    for i, rating in enumerate(ratings_list):
        videos[i]["rating"] = rating
    
    return videos