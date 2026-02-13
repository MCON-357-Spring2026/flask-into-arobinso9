from flask import Flask, request, current_app,jsonify
app = Flask(__name__)

# server code
# Server (Flask)->	Waits for requests and returns data. ->	@app.route("/")
# In the server we are dealing with REQUEST objects, (without the s. Request not requests!)
# which have the fields: .method, .path, .content_type, get_json()...

# Route 1: Welcome Endpoint
@app.route("/", methods=['GET'])
def welcome_endpoint():
    return "<h1>Welcome to My Flask API!</h1>"

# Route 2: About Endpoint
@app.route("/about", methods=['GET'])
def about_endpoint():
    return jsonify({
        "name": "Aviva Robinson",
        "course": "MCON-504 - Backend Development",
        "semester": "Spring 2025"
    })

# Route 3: Greeting with Name Parameter
@app.route("/greet/<name>", methods=['GET'])
def greeting_with_params(name): # we need to pass name param in
    return f"<p>Hello, {name}! Welcome to Flask.</p>"

# Route 4: Calculator Endpoint
@app.route("/calculate", methods=['GET'])
def calculate_endpoint():
    # When the user types ?num1=10&num2=5 into their browser,
    # Flask automatically catches those values and stores them inside the request.args object.
    # Here we are passing the data in after the ? in the URL, which is defined inside the body= Query params
    # Before in route 3, we passed the data as part of the URL path which is defined in the function.
    # we use path/route params (route 3 style) for resource identification - mandatory.
    # we use query params (route 4) for action/filtering - query params are optional
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operation = request.args.get('operation')

    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
         result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({
            "result": result,
            "operation": operation
        })

    except Exception as e:
        # Log the exception and return an error response
        print(f"Error occurred: {e}")
        raise e

# Route 5: Echo Endpoint (POST)
@app.route("/echo", methods=['POST'])
def echo_endpoint():
    # we are first getting the JSON data sent into the request body
    data = request.get_json()

    # we need to check if data exists in the dict returned
    if not data:
        # jsonify() creates a dict. We are creating a key:"error" and a value:"No JSON data provided"
        return jsonify({"error": "No JSON data provided"}), 400

    # we added 'echoed'=True key,value pair to our data dict
    data["echoed"] = True
    return jsonify(data)

# Route 6: Status Code Practice
# using path params again!
@app.route("/status/<int:code>", methods=['GET'])
def status_code_practice(code):
    message = f"This is a {code} status message"
    return message, code

# HOOKS
# hooks intercept all requests so we dont specify the route. Flask knows to run the hook b4 every
# route function
@app.before_request
def hook_log_request_to_console():
    # we use the request object to see what the client is doing
    method = request.method
    path = request.path
    print(f"--- [LOG] Incoming Request: {method} {path} ---")

# since the hook is after_request which is after the route function completed its job,
# we already have the response object, so we are now editing it b4 we send it to client
@app.after_request
def hook_adds_custom_header_to_every_response(response):
    response.headers['X-Custom-Header'] = 'FlaskRocks'
    return response

# teardown_request is used for cleanup and does NOT have access to teh response obj
# Instead, it receives an exception argument. If the code ran perfectly, that argument is None.
# If the code crashed, that argument contains the error.
@app.teardown_request
def hook_logs_exceptions_to_console(exception):
    if exception:
        print(f"--- [TEARDOWN] A FATAL error occurred: {exception} ---")

#debug route
@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)


# If we don't have app.run(), the server never starts, and there is nothing for the client to test.
# so app.run() starts the server
if __name__ == "__main__":
    app.run(debug=True)





