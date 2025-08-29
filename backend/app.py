from flask import Flask, render_template
import os

template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'templates')
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route("/")
def index():
    page_title = "Stock"
    return render_template('index.html', page_title=page_title)

if __name__ == "__main__":
    app.run(debug=True)
    