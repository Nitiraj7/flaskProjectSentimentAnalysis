from flask import Flask,request,jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/app/sentiment',methods=['POST'])
def sentimental_analysis():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error':'no text provided'}),400
    
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        result = 'positive'
    elif sentiment < 0:
        result = 'negative'
    else:
        result = 'neutral'
    
    return jsonify({"sentiment":result,"polarity":sentiment})


if __name__ == '__main__':
    app.run(debug=True)
 