from sanic import Sanic
from sanic import Blueprint
from sanic.response import text


app = Sanic(__name__)
from sanic import response


@app.route('/Booking')
def handle_request(request):
    return response.html('<p>Give your information</p><br>user name:<input name="user name"><br> Password: <input type="text" name="pwd"><br>mobile number:<input name="mobile number" maxlength="10"><br>vehicle number:<input name="vehicle no" maxlength="5"><br>Book:<input name="booking"><br><button type="submit">submit</button>')

@app.route('/searching')
def handle_request(request):
    return response.html('<p>Enter your vehicle information</p><br>vehicle number:<input name="vehicle number:"><br> model: <input type="model:"><br>check status:<input name="status" maxlength="10"><br><br><button type="submit">submit</button>')

app.run( port=8011, debug=True)