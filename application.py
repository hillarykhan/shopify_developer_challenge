from flask import Flask, request, render_template, Response
from db import init_db, db
from werkzeug.utils import secure_filename
from models import Img


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/')
def hello():
    return "Let's see some cats!"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
        pic = request.files['pic']

        if not pic:
            return 'No pic uploaded', 400

        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        img = Img(img=pic.read(), mimetype=mimetype, name=filename)
        db.session.add(img)
        db.session.commit()
        
        return 'Image successfully uploaded!', 200
    return render_template('index.html')


@app.route('/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'There is no image with that id', 404
    return Response(img.img, mimetype=img.mimetype)