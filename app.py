from flask import Flask, render_template, url_for, request, session, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Reviews')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

reviews = db.reviews
reviews.drop()

# { 'restaurant': '', 'address': '', 'review': '', 'rating': '', 'image': '' },

db.reviews.insert_many([
    { 'restaurant': 'Maizal Restaurant & Tequila Bar', 'address': '990 Bay St, Staten Island, NY 10305', 'review': 'The best tableside guac, hands down', 'rating': '5', 'image': './static/maizal.png'},
    { 'restaurant': 'Jose Tejas', 'address': '700 US-1, Iselin, NJ 08830', 'review': 'Cheap, delicious, and fun!', 'rating': '5', 'image': './static/jose.png' },
    { 'restaurant': 'DeLuca\'s Italian Restaurant', 'address': '7324 Amboy Rd, Staten Island, NY 10307', 'review': 'Come for the drinks, stay for the meatballs', 'rating': '5', 'image': './static/delucas.png' },
    { 'restaurant': 'Patrizia\'s of Staten Island', 'address': '4255 Amboy Rd, Staten Island, NY 10308', 'review': 'One of my favorite Italian restaraunts. The burrata!', 'rating': '5', 'image': './static/pats.png' },
    { 'restaurant': 'Pizzeria Giove', 'address': '278 New Dorp Lane, Staten Island, NY 10306', 'review': 'If you\'re looking for a delicious specialty pie, this is the place', 'rating': '5', 'image': './static/pg.png' },
    { 'restaurant': 'Ocean Sushi', 'address': '20 Jefferson Blvd, Staten Island, NY 10312', 'review': 'Fresh sushi & great service', 'rating': '4', 'image': './static/ocean.png' },
    { 'restaurant': 'Tommy\'s Tavern + Tap', 'address': '2655 Richmond Ave, Staten Island, NY 10314', 'review': 'Their wings are the BOMB.', 'rating': '4', 'image': './static/tommys.png' },
    { 'restaurant': 'Cucina Fresca', 'address': '2110 Richmond Rd, Staten Island, NY 10306', 'review': 'The best service I\'ve ever gotten at a restaurant', 'rating': '4', 'image': './static/cucina.png' },
    { 'restaurant': 'Richmond Republic', 'address': '4459 Amboy Rd, Staten Island, NY 10312', 'review': 'Brunch = A Bloody Mary bar', 'rating': '3', 'image': './static/rr.png' },
    { 'restaurant': 'Mizu Japanese Restaurant', 'address': '240 Page Ave, Staten Island, NY 10307', 'review': 'The hibachi entrees are delicious', 'rating': '4', 'image': './static/mizu.png'},
    { 'restaurant': 'Violette\'s Cellar', 'address': '2271 Hylan Blvd, Staten Island, NY 10306', 'review': 'The decor of this place is one of my favorites. Food is tapas style and pretty good.', 'rating': '3.5', 'image': './static/vc.png'}
])

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', reviews=reviews.find())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit')
def restaurant_new():
    """User adds new restaurant."""
    return render_template('partials/submit.html', review={})

@app.route('/restaurants', methods=['POST'])
def restaurants_submit():
    """Submit new restaurant."""
    review = {
        'restaurant': request.form.get('name'),
        'address': request.form.get('add'),
        'rating': request.form.get('rating'),
        'review': request.form.get('review'),
        # 'image': request.form.get('pic')
    }

    review_id = reviews.insert_one(review).inserted_id
    return redirect(url_for('restaurants_show', review_id=review_id))

# @app.route('/upload', methods=['POST'])
# def upload_image():
#
#     if request.method == "POST":
#
#         if request.files:
#
#             image = request.files["image"]
#
#             print(image)
#
#             return redirect(request.url)


@app.route('/restaurants/<review_id>')
def restaurants_show(review_id):
    review = reviews.find_one({'_id': ObjectId(review_id)})
    return render_template('show.html', review=review)

@app.route('/restaurants/<review_id>/delete', methods=['POST'])
def restaurants_delete(review_id):
    """Delete one restaurant."""
    reviews.delete_one({'_id': ObjectId(review_id)})
    return redirect(url_for('index'))


@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        search = request.form['query']
    pass

@app.route('/account')
def account():
    return render_template('partials/reg_log_form.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))









