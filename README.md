# 💬 Comment Sentiment Analyzer

A simple and powerful web application that analyzes the sentiment of any text using Natural Language Processing (NLP). Instantly determine if a comment is **Positive** 😊, **Negative** 😠, or **Neutral** 😐.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- ✅ **Real-time Sentiment Analysis** - Instant results
- ✅ **NLP Powered** - Uses VADER sentiment analysis
- ✅ **Emoji Support** - Understands emojis in text
- ✅ **Confidence Scores** - Shows analysis confidence level
- ✅ **Beautiful UI** - Modern, responsive design
- ✅ **Example Comments** - Pre-loaded examples to test
- ✅ **No API Keys Required** - Works completely offline

## 🚀 Demo

Simply enter any comment or text, and the app will analyze its sentiment:

**Examples:**
- "This is absolutely amazing! Love it! 😍" → **POSITIVE**
- "This is terrible, worst thing ever 😡" → **NEGATIVE**
- "The content is okay, nothing special" → **NEUTRAL**

## 🛠️ Technology Stack

### Backend
- **Python 3.7+**
- **Flask** - Web framework
- **VADER Sentiment** - NLP sentiment analysis library
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradients and animations
- **JavaScript (Vanilla)** - Interactive functionality
- **Font Awesome** - Icons

### NLP Engine
- **VADER (Valence Aware Dictionary and sEntiment Reasoner)**
  - Lexicon-based sentiment analysis
  - Optimized for social media text
  - Handles emojis, slang, and informal language
  - Pre-trained on social media data

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/comment-sentiment-analyzer.git
cd comment-sentiment-analyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser**
```
http://localhost:5000
```

## 📁 Project Structure

```
comment-sentiment-analyzer/
├── app.py                 # Flask application (Backend)
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend interface
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## 🎯 How It Works

### Sentiment Analysis Pipeline

```
User Input → VADER Analyzer → Sentiment Scores → Classification → Visual Results
```

1. **Input**: User enters text/comment
2. **Processing**: VADER analyzes the text
3. **Scoring**: Generates sentiment scores
   - Positive score (0-1)
   - Negative score (0-1)
   - Neutral score (0-1)
   - Compound score (-1 to +1)
4. **Classification**: 
   - Compound ≥ 0.05 → Positive
   - Compound ≤ -0.05 → Negative
   - Otherwise → Neutral
5. **Display**: Shows result with emoji and confidence

### VADER Sentiment Features

- **Emoji Recognition**: 😊 😡 👍 💀
- **Intensifiers**: "very good" > "good"
- **Negation Handling**: "not bad" ≠ "bad"
- **Punctuation Impact**: "Great!!!" > "Great"
- **Slang Support**: Modern internet language

## 🔧 API Endpoint

### POST `/api/analyze-sentiment`

**Request:**
```json
{
  "text": "This is amazing!"
}
```

**Response:**
```json
{
  "text": "This is amazing!",
  "sentiment": {
    "label": "positive",
    "compound": 0.6249,
    "positive": 0.692,
    "negative": 0.0,
    "neutral": 0.308,
    "confidence": "High",
    "confidence_score": 0.6249
  }
}
```

## 💡 Use Cases

- **Social Media Monitoring** - Analyze user comments
- **Customer Feedback** - Understand customer sentiment
- **Product Reviews** - Categorize review sentiment
- **Content Moderation** - Flag negative comments
- **Market Research** - Analyze public opinion
- **Educational Tool** - Learn about NLP and sentiment analysis

## 🎨 Screenshots

### Main Interface
Clean and intuitive interface for entering comments

### Analysis Results
Clear visual feedback with emoji indicators and detailed scores

### Example Comments
Pre-loaded examples for quick testing

## ⌨️ Keyboard Shortcuts

- **Ctrl + Enter** - Analyze sentiment
- **Click Examples** - Auto-fill and analyze

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **VADER Sentiment** - C.J. Hutto & Eric Gilbert for the VADER sentiment analysis tool
- **Flask** - Pallets Projects for the Flask framework
- **Font Awesome** - For the beautiful icons

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/comment-sentiment-analyzer](https://github.com/yourusername/comment-sentiment-analyzer)

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Batch analysis (multiple comments at once)
- [ ] Export results to CSV/JSON
- [ ] Sentiment trend visualization
- [ ] Custom sentiment thresholds
- [ ] API rate limiting
- [ ] User authentication
- [ ] Comment history tracking

---

⭐ **Star this repo if you find it helpful!** ⭐