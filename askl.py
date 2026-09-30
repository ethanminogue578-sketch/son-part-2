import requests

url = "https://openlibrary.org/search.json?q=dracula/&scrlybrkr=79698899"
response = requests.get(url, verify=False)
data = response.json()

books = data["docs"]

for book in books:
    print(book["title"])