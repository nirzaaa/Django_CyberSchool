import requests
import re

url_login = 'http://localhost:8000/login/'
url_profile = 'http://localhost:8000/profile/'

session = requests.Session()

response = session.get(url_login)
csrf_token = session.cookies.get_dict()['csrftoken']

login_data = {
    'csrfmiddlewaretoken': csrf_token,
    'username': '<your username>',
    'password': '<your password>'
}

response = session.post(url_login, data=login_data)

# Check if the login was successful (you should inspect the website's response for this).
if response.status_code == 200:
    print("Login successful!")
    response = session.get(url_profile)

    x = re.search('name="email" value=', response.text)
    y = re.search('maxlength="320" class', response.text)
    your_email = response.text[x.end()+1:y.start()-2]
    print(f"By scraping the login session I found that your email is: {your_email}")

else:
    print("Login failed.")


