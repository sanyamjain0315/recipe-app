from flask import Flask, render_template, url_for

app = Flask(__name__)

from pymongo import MongoClient

# Replace these with your MongoDB connection details
mongo_uri = "mongodb://localhost:27017/"
database_name = "recipes_collection"
collection_name = "recipes"

# Create a connection to the MongoDB server
client = MongoClient(mongo_uri)

# Access the database
db = client[database_name]

# Access the collection
collection = db[collection_name]


@app.route('/')
def home():
    all_recipes = collection.find({})
    print(all_recipes)
    return render_template('templates\home.html', recipes=all_recipes)

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
