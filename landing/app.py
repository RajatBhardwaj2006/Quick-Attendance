import os
from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", app_url=os.getenv("STREAMLIT_APP_URL","http://localhost:8501"))
if __name__=="__main__":
    app.run(debug=True)
