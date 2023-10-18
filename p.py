import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

#classifier = joblib.load(r"decision_tree_model.pkl")
#vectorizer = joblib.load(r"tfidf_vectorizer.pkl")

@app.route("/", methods=['POST'])
def hello():
    body = request.get_json()
    input_data = body.get('data', '')

    test_input = pd.Series(input_data)
    #predictions = classifier.predict(vectorizer.transform(test_input))[0]

    # print("Predictions:", predictions)
    # response = {
    #     "result": predictions
    # }
    # return jsonify(response)

if __name__ == "main":
    app.run()