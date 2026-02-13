1- What does the @app.route() decorator actually do?
It creates a mapping between a specific URL path and the Python function that should handle it

2- How does Flask know which function to call when a request arrives?
When a request comes to the server, Flask checks the Path and the HTTP Method (GET, POST, ...)
against that map to find the correct function

3- What's the difference between route parameters (<name>) and query parameters (?key=value)?
Route Params (/greet/Aviva): Used for identifying a specific resource. They are mandatory parts of the URL.
Query Params (?num1=5): Used for filtering or actions. They are optional and added to the end of the URL after a ?

4- Why do we need to use request.get_json() for POST requests but request.args.get() for GET query parameters?
GET data is sent in the URL itself (the "Header" area), so we use request.args, which parses the URL string
POST data is sent in the Request Body, so we use request.get_json() which parses the body of the message.

5- What happens if you try to access request.args outside of a request context?
a RuntimeError. Flasks request object only exists while a request is actually happening.
If you try to use it when the server isn't currently processing a call, 
then python will complain that you are working "outside of request context."