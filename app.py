from flask import Flask, render_template, url_for, request, session, redirect
from pymongo import MongoClient
# from flask_bcrypt import Bycrypt
import os


app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Reviews')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

reviews = db.reviews
reviews.drop()

# { 'restaurant': '', 'address': '', 'review': '', 'rating': '', 'image': '' },

db.reviews.insert_many([
    { 'restaurant': 'Maizal Restaurant & Tequila Bar', 'address': '990 Bay St, Staten Island, NY 10305', 'review': 'The best tableside guac, hands down', 'rating': '5', 'image': './static/maizal.png' },
    { 'restaurant': 'Jose Tejas', 'address': '700 US-1, Iselin, NJ 08830', 'review': 'Cheap, delicious, and fun!', 'rating': '5', 'image': './static/jose.png' },
    { 'restaurant': 'Pizzeria Giove', 'address': '278 New Dorp Lane, Staten Island, NY 10306', 'review': 'If you\'re looking for a delicious specialty pie, this is the place', 'rating': '5', 'image': './static/pg.png' },
    { 'restaurant': 'DeLuca\'s Italian Restaurant', 'address': '7324 Amboy Rd, Staten Island, NY 10307', 'review': 'Come for the drinks, stay for the meatballs', 'rating': '5', 'image': './static/delucas.png' },
    { 'restaurant': 'Richmond Republic', 'address': '4459 Amboy Rd, Staten Island, NY 10312', 'review': 'Brunch = A Bloody Mary bar', 'rating': '3', 'image': './static/rr.png' },
    { 'restaurant': 'Patrizia\'s of Staten Island', 'address': '4255 Amboy Rd, Staten Island, NY 10308', 'review': 'One of my favorite Italian restaraunts. The burrata!', 'rating': '5', 'image': './static/pats.png' },
    { 'restaurant': 'Ocean Sushi', 'address': '20 Jefferson Blvd, Staten Island, NY 10312', 'review': 'Fresh sushi & great service', 'rating': '4', 'image': './static/ocean.png' },
    { 'restaurant': 'Tommy\'s Tavern + Tap', 'address': '2655 Richmond Ave, Staten Island, NY 10314', 'review': 'Their wings are the BOMB.', 'rating': '4', 'image': './static/tommys.png' },
    { 'restaurant': 'Cucina Fresca', 'address': '2110 Richmond Rd, Staten Island, NY 10306', 'review': '4', 'rating': 'The best service I\'ve ever gotten at a restaurant', 'image': './static/cucina.png' }
])

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', reviews=reviews.find())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/account')
def account():
    pass

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))









