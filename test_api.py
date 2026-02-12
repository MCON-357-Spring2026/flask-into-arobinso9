import requests
# client code
# client will send in URL and will receive a response from the Server and will then format it
# Client (Requests) ->	Sends requests and processes the data. ->	requests.get(...)


def test_welcome_route():
    response = requests.get('http://127.0.0.1:5000/')
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text}\n")
def test_about_route():
    response = requests.get('http://127.0.0.1:5000/about')
    # we will parse the JSON response into a Python Dict
    data = response.json()
    # we are printing the values using the keys of the dict
    print(f"Name: {data['name']}")
    print(f"Course: {data['course']}")
    print(f"Semester: {data['semester']}\n")

# When we call response.text, we are asking the requests library to give us the raw body
# of the server's response as a Python string.
def test_greeting_route():
    name = "Aviva"
    url = f'http://127.0.0.1:5000/greet/{name}'
    # we make the request
    response = requests.get(url)

    # check to see if name is in the returned python string
    if name in response.text:
        print(f"Success: Response contains '{name}'")
    else:
        print(f"Failure: '{name}' not found in response")
