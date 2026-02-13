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
    # we make the request, and request.get() returns the Response object which contains
    # the status code, headers, and the body.
    # response.json() takes the raw text from the server and converts it to a python dict
    response = requests.get(url)

    # check to see if name is in the returned python string
    if name in response.text:
        print(f"Success: Response contains '{name}'")
    else:
        print(f"Failure: '{name}' not found in response")

def test_calculator_route():
    base_url = 'http://127.0.0.1:5000/calculate'

    resp_add = requests.get(f"{base_url}?num1=10&num2=5&operation=add")
    if resp_add.status_code == 200:
        # since response.json returns takes the raw text from the server and converts it to a
        # python dict, and then we look up the value associated with the key results
        print(f"Success Add: {resp_add.json()['result']}")

    resp_mult = requests.get(f"{base_url}?num1=10&num2=5&operation=multiply")
    if resp_mult.status_code == 200:
        print(f"Success Multiply: {resp_mult.json()['result']}")

    resp_div_zero = requests.get(f"{base_url}?num1=10&num2=0&operation=divide")
    if resp_div_zero.status_code == 400:
        print(f"Error: {resp_div_zero.json()['error']}")

def test_echo_route():
    url = 'http://127.0.0.1:5000/echo'

    # we create a dict that will be converted to JSON and sent in the request body
    sample_data = {
        "user": "Aviva",
        "message": "Testing the echo!"
    }

    # requests.post sends the data. We need to say the address= the url, and the contents= json
    # we use 'json=' which converts our dict to JSON.
    # we cant send dicts over the internet - only strings of text
    response = requests.post(url, json=sample_data)

    if response.status_code == 200:
        # we convert the server's response back into a python dict
        returned_data = response.json()

        if returned_data.get("echoed") == True:
            print(f"Success: Server echoed data and added key! Full response: {returned_data}")
        else:
            print(" Oops, failure: 'echoed' key is missing or is False.")

    elif response.status_code == 400:
        print(f"Error!!!! :( Received status code {response.status_code}")

def diff_status_codes():
