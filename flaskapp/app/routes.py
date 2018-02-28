from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


"""
First. we imported the Flask class and a function render_template.
Next, we created a new instance of the Flask class.
We then mapped the URL / to the function home(). Now, when someone visits this URL, the function home() will execute.
The function home() uses the Flask function render_template() to render the home.html template we just created from the templates/ folder to the browser.
Finally, we use run() to run our app on a local server. We'll set the debug flag to true, so we can view any applicable error messages if something goes wrong, and so that the local server automatically reloads after we've made changes to the code.
"""