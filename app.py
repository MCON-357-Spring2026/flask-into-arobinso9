from flask import Flask, request, current_app,jsonify
app = Flask(__name__)

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
    # Here we are passing the data in after the ? in the URL, which is defined inside the body
    # Before in route 3, we passed the data as part of the URL path which is defined in the function.
    # we use path params (route 3 style) for resource identification
    # we use query params (route 4) for action/filtering
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operation = request.args.get('operation')

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
# Route 5: Echo Endpoint (POST)
@app.route("/echo", methods=['POST'])
def echo_endpoint():
    # we are first getting the JSON data sent into the request body
    data = request.get_json()

    # we need to check if data exists
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    data["echoed"] = True
    return jsonify(data)

# Route 6: Status Code Practice
# using path params again!
@app.route("/status/<int:code>", methods=['GET'])
def status_code_practice(code):
    message = f"This is a {code} status message"
    return message, code

if __name__ == "__main__":
    app.run(debug=True)





