from bottle import Bottle, request, response

# Create the Bottle app instance
app = Bottle()

# Expose Bottle framework components
Request = request
Response = response
App = app


# add CORS headers to all responses
@app.hook("after_request")
def enable_cors():
    """
    Add CORS headers to all responses.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = (
        "Origin, Content-Type, Accept, Authorization"
    )
    response.headers["Access-Control-Allow-Credentials"] = "true"


# handle preflight OPTIONS requests
@app.route("/<:re:.*>", method="OPTIONS")
def handle_options():
    """
    Respond to preflight OPTIONS requests for CORS.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = (
        "Origin, Content-Type, Accept, Authorization"
    )
    return {}
