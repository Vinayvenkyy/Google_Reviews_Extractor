import os
import serpapi
from dotenv import load_dotenv


load_dotenv(dotenv_path='./.env')  # Explicit relative path


print("+++++++++++++++++++++++++++++++++++++++++++++")
api_key = os.getenv('SERPAPI_KEY')
print(api_key)
print("+++++++++++++++++++++++++++++++++++++++++++++")
client = serpapi.Client(api_key = api_key)

results = client.search({
    'engine': 'google_maps',
    'type': 'search',
    'q': 'Arnold\'s Martial Arts'
})

print(results)

