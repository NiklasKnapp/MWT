from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_user:your_password@postgres/your_database'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(255))

@app.route('/upload', methods=['POST'])
def upload():
    logging.debug("start upload")
    #file = request.files['file']
    #df = pd.read_csv(file)
    #headers = df.columns.tolist()
    headers = ['header1', 'header2']
    logging.debug(headers)

    #TODO persist file

    return 200

@app.route('/headers/<int:id>', methods=['GET'])
def get_headers(id):
    logging.debug("return headers")
    #TODO get data from DB

    headers = ['header1', 'header2', id]
    logging.debug(headers)

    return jsonify({'headers': headers})

@app.route('/train/<int:id>/<string:column>', methods=['Get'])
def train(id, column):
    #df = {
    #    1: {"name": "John", "age": 25},
    #    2: {"name": "Jane", "age": 30},
    #    3: {"name": "Bob", "age": 22},
    #}
    
    #TODO: get data from db

    #X = df.drop(columns=[column])
    #y = df[column]

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #model = LinearRegression()
    #model.fit(X_train, y_train)
    #y_pred = model.predict(X_test)

    #r_squared = r2_score(y_test, y_pred)

    #return jsonify({'r_squared': r_squared})
    return 1

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)