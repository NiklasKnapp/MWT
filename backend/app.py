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

logging.getLogger().setLevel(logging.DEBUG)

class DynamicModel(db.Model):
    __tablename__ = 'my_table'
    id = db.Column(db.Integer, primary_key=True)

def create_model_class(csv_columns):
    # Dynamically create columns based on CSV columns
    for column in csv_columns:
        if column != 'id':
            setattr(DynamicModel, column, db.Column(db.String(255)))

    return DynamicModel

def save_csv_to_database(file, model_class):
    df = pd.read_csv(file)
    model_class.__table__.create(db.engine, checkfirst=True)
    
    df.to_sql('my_table', db.engine, if_exists='replace', index=False)

def read_data_from_database(model_class):
    # Fetch data from the database using SQLAlchemy
    query_result = db.session.query(model_class).all()

    # Convert the query result to a list of dictionaries
    data = [{column.name: getattr(row, column.name) for column in model_class.__table__.columns} for row in query_result]

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    return df

def reset_data(model_class):
    

@app.route('/upload', methods=['GET'])
def upload():
    logging.info("start upload")
    #file = request.files['file']
    file = 'test.csv'
    df = pd.read_csv(file)
    csv_columns = df.columns.tolist()
    logging.debug(csv_columns)

    # Create a dynamic SQLAlchemy model based on CSV columns
    DynamicModel = create_model_class(csv_columns)

    # Save the CSV data to the database using the dynamic model
    save_csv_to_database(file, DynamicModel)

    logging.info("upload successful")

    return jsonify({"headers": csv_columns})

@app.route('/headers', methods=['GET'])
def get_headers():
    logging.debug("return headers")
    df = read_data_from_database(DynamicModel)

    headers = list(df.columns)
    logging.debug(headers)

    return jsonify({'headers': headers})

@app.route('/train/<string:column>', methods=['Get'])
def train(column):
    df = read_data_from_database(DynamicModel)

    X = df.drop(columns=[column])
    y = df[column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r_squared = r2_score(y_test, y_pred)

    return jsonify({'r_squared': r_squared})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)