from flask import Flask,request,jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/app/sentimentfor',methods=['POST'])
def sentimental_analysisfor():
    data = request.get_json()
    texts = data.get('texts',[])
    if not texts:
        return jsonify({'error':'no data from here'}),400
    results = []

    for i in texts:
        if not i.strip():
            continue
        blob = TextBlob(i)                      # WE CREATE A VAR blob AND PUT i(values) from texts INTO IT  
        polarity = blob.sentiment.polarity      # THEN WE CREATE polarity VAR 

        if polarity > 0:
            sentiment = 'positive'
        elif polarity < 0:  
            sentiment = 'negative'          #HERE WE USE CONDITIONAL STATEMENTS TO IDENTIFY THE POLARITY OF THE LINE BY textblob librabry
        else:
            sentiment = 'neutral'

        results.append({
            "text":i,
            "sentiment":sentiment,          #TO APPEND THE RESULT WITH POLARITY AND SENTIMENT WITH JSON DATA HERE 'texts' : i WILL TAKE ONE BY ONE ELEMENTS FORM THE LISTS
            "polarity":polarity
        })
    return jsonify({"results":results})

if __name__ == '__main__':              #TO RUN THE APP
    app.run(debug = True)

