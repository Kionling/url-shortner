# URL Shortner 
This URL shortner is designed to be a simple and straightforward application that allows the user to input their URL of choice from any website and condense it to the localhost url link that is smaller than the original URL. I created this application to help me track URL links from various websites I want bookmarked. I also built this to develop a future application that allows me to track URL click data from users.

# Technologies
* Flask
* Python
* sqlite3 
* HTML
* python random


# Code Snippet 

```
def get_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

```
This function generates a series of random strings that gets attacted to the original URL that the user wants shortened. The unique character gets added to the end of the '/' route


# Authors
* (Daniel Jauregui)[https://www.linkedin.com/in/kionling/]



