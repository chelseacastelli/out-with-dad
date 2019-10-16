from flask import Flask, render_template

app = Flask(__name__)


reviews = [
    { 'restaurant': 'DeLuca\'s Italian Restaurant', 'address': '7324 Amboy Rd, Staten Island, NY 10307', 'review': 'The best meatballs I ever had. Drinks are also really good', 'rating': '5' },
    { 'restaurant': 'Maizal Restaurant & Tequila Bar', 'address': '990 Bay St, Staten Island, NY 10305', 'review': 'One of my favorite places.. best tableside guac on SI, hands down!', 'rating': '5' }
]


@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', reviews=reviews)


