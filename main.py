#### importing libraries
import serpapi
import os
import pandas as pd
from dotenv import load_dotenv
# Load the environment variables
print("Code running...")
# Set your API key  from the environment variable
load_dotenv(dotenv_path='./.env')  # Explicit relative path

print("+++++++++++++++++++++++++++++++++++++++++++++")
api_key = os.getenv('SERPAPI_KEY')
print(api_key)
print("+++++++++++++++++++++++++++++++++++++++++++++")
client = serpapi.Client(api_key=api_key)

# Place ID for the location
place_id = "ChIJJZzWWcWJTIYRmthvDCIgXFU" # Check code below to get place_id

# Initialize an empty list to store reviews
all_reviews = []

# Initialize next_page_token to continue to the next pages
# next_page_token = "CAESBkVnSUlDQQ==" # Check how to get next_page_token_initially
my_counter = 0
# Loop to fetch reviews as long as there is a next_page_token
while True:
    my_counter +=1
    print(my_counter)
    if my_counter == 30:
      print("Something wrong with the code.")
      break;

    params = {
        'engine': 'google_maps_reviews',
        'type': 'search',
        'place_id': place_id,
        'sort_by': 'date',
    }

    if my_counter > 1 and next_page_token:
        params["next_page_token"] = results['serpapi_pagination']['next_page_token']

    print("Search == ")
    print(params)
    # print(results['serpapi_pagination']['next_page_token'])
    # Fetch the results from the API
    results = client.search(params)


    reviews = results.get("reviews", [])
    for review in reviews:
        user_name = review["user"]["name"]
        rating = review["rating"]
        review_text = review.get("snippet", "-- NA --")
        review_date = review["date"]
        # Add it to dataframe
        all_reviews.append({
            'Name': user_name,
            'Rating': rating,
            'Review': review_text,
            'Date': review_date
        })

    # Check if there is a next page
    # next_page_token = results['serpapi_pagination']['next_page_token']
    if 'serpapi_pagination' in results and 'next_page_token' in results['serpapi_pagination']:
      next_page_token = results['serpapi_pagination']['next_page_token']
    else:
      next_page_token = None

    # If no next page token is found, break the loop
    if not next_page_token:
        break

# Create a DataFrame from the collected reviews
df = pd.DataFrame(all_reviews)

# Display the DataFrame
print("----------------------")
print("Number of reviews recorded: ", len(df))
print("----------------------")

print(df)