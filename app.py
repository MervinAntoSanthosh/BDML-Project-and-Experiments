from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def get_sentiment_label(compound_score):
    """Convert compound score to sentiment label"""
    if compound_score >= 0.05:
        return 'positive'
    elif compound_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    """Analyze sentiment for input text"""
    data = request.json
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'error': 'Please enter some text to analyze'}), 400
    
    # Analyze sentiment
    sentiment_scores = analyzer.polarity_scores(text)
    sentiment_label = get_sentiment_label(sentiment_scores['compound'])
    
    # Determine confidence level
    confidence = abs(sentiment_scores['compound'])
    if confidence >= 0.7:
        confidence_level = "Very High"
    elif confidence >= 0.5:
        confidence_level = "High"
    elif confidence >= 0.3:
        confidence_level = "Medium"
    elif confidence >= 0.1:
        confidence_level = "Low"
    else:
        confidence_level = "Very Low"
    
    return jsonify({
        'text': text,
        'sentiment': {
            'label': sentiment_label,
            'compound': round(sentiment_scores['compound'], 4),
            'positive': round(sentiment_scores['pos'], 4),
            'negative': round(sentiment_scores['neg'], 4),
            'neutral': round(sentiment_scores['neu'], 4),
            'confidence': confidence_level,
            'confidence_score': round(confidence, 4)
        }
    })

if __name__ == '__main__':
    print("🚀 Comment Sentiment Analyzer")
    print("=" * 40)
    print("💬 Enter any comment to analyze")
    print("🎯 Get: Positive, Negative, or Neutral")
    print("🔗 Open: http://localhost:5000")
    print("=" * 40)
    app.run(debug=True, host='0.0.0.0', port=5000)