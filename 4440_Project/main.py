from flask import Flask,render_template,request
# create flask object
app = Flask(__name__, static_folder='templates', static_url_path='')
app.debug = True
# create home page #
@app.route("/")
def index():
    return render_template("Home.html")

@app.route('/chosen', methods=['POST'])
def form_submit():
    selected_option = request.form.get('query')
    if selected_option == 'meals':
        return render_template('mealPlan.html')
    elif selected_option == 'overview':
        return render_template('overview.html')
    elif selected_option == 'Adult':
        return render_template('Adult.html')
    elif selected_option == '':
        return render_template('Adult.html')
    else:
        return render_template('fake.html')
#----------------main funtion-----------------#
if __name__ == "__main__":
    app.run()
    app.debug = True
