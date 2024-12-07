from bottle import Bottle, request, response

# create the Bottle app instance
app = Bottle()

# expose Bottle framework components
Request = request
Response = response
App = app
