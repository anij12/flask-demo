from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Tut'
db = SQLAlchemy(app)

class Insu(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    msg = db.Column(db.String(120), nullable=False)
@app.route("/")
def home():
    return render_template('index.html',name="aniruddha")
@app.route("/fill", methods=["GET","POST"])
def contact_fill():
    if request.method == "POST":
        fname=request.form.get("name")
        femail=request.form.get("email")
        fmsg=request.form.get("message")
        cur=Insu(name=fname,email=femail,msg=fmsg)
        db.session.add(cur)
        db.session.commit()
        return "<h1>data stored<h1>"
    return render_template("about.html")

app.run(debug=True)