from flask import Flask
# create flask object
app = Flask(__name__)
app.debug = True
# create home page #
@app.route("/")
def index():
    return app.send_static_file("Home.html")

#----------------main funtion-----------------#
if __name__ == "__main__":
    app.run()
    app.debug = True
