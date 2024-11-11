from flask import Flask, jsonify, request
from random import uniform
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Existing sample food truck data
food_trucks = [
    {
        "name": "Tasty Tacos",
        "lat": 40.748817,
        "lon": -73.985428,
        "food_items": [{"name": "Tacos", "price": "$3", "image": "taco.jpg"},
                       {"name": "Burritos", "price": "$5", "image": "burrito.jpg"},
                       {"name": "Nachos", "price": "$4", "image": "nachos.jpg"}],
        "reviews": [
            "Best tacos in NYC!",
            "Super tasty and fresh ingredients.",
            "Love the spicy salsa!"
        ],
        "operating_hours": "11 AM - 10 PM",
        "rating": 4.5,
        "location": "Midtown"
    },
    {
        "name": "Burger Bus",
        "lat": 40.73061,
        "lon": -73.935242,
        "food_items": [{"name": "Burgers", "price": "$7", "image": "burger.jpg"},
                       {"name": "Fries", "price": "$3", "image": "fries.jpg"},
                       {"name": "Shakes", "price": "$5", "image": "shake.jpg"}],
        "reviews": [
            "The cheeseburger is a must-try!",
            "Great service and delicious food.",
            "Their milkshakes are amazing!"
        ],
        "operating_hours": "10 AM - 11 PM",
        "rating": 4.8,
        "location": "Williamsburg"
    },
    {
        "name": "Pizza Palace",
        "lat": 40.712776,
        "lon": -74.005974,
        "food_items": [{"name": "Pizza", "price": "$2", "image": "pizza.jpg"},
                       {"name": "Calzones", "price": "$6", "image": "calzone.jpg"},
                       {"name": "Garlic Knots", "price": "$1", "image": "garlic_knots.jpg"}],
        "reviews": [
            "Authentic New York pizza!",
            "Crust is perfect!",
            "Best calzones around!"
        ],
        "operating_hours": "12 PM - 12 AM",
        "rating": 4.7,
        "location": "East Village"
    },
    {
        "name": "Vegan Delight",
        "lat": 40.758896,
        "lon": -73.985130,
        "food_items": [{"name": "Salads", "price": "$8", "image": "salad.jpg"},
                       {"name": "Smoothies", "price": "$5", "image": "smoothie.jpg"},
                       {"name": "Veggie Burgers", "price": "$7", "image": "veggie_burger.jpg"}],
        "reviews": [
            "Amazing vegan options!",
            "Fresh and healthy meals.",
            "Love the smoothies!"
        ],
        "operating_hours": "9 AM - 9 PM",
        "rating": 4.9,
        "location": "Central Park"
    },
]

@app.route("/api/foodtrucks", methods=["GET"])
def get_food_trucks():
    # Randomize locations slightly to simulate movement
    trucks = [
        {
            "name": truck["name"],
            "lat": truck["lat"] + uniform(-0.005, 0.005),
            "lon": truck["lon"] + uniform(-0.005, 0.005),
            "food_items": truck["food_items"],
            "reviews": truck["reviews"],
            "operating_hours": truck["operating_hours"],
            "rating": truck["rating"],
            "location": truck["location"]
        }
        for truck in food_trucks
    ]
    return jsonify(trucks)

@app.route("/api/foodtrucks", methods=["POST"])
def add_food_truck():
    # Get the JSON data from the request
    data = request.json
    # Add the new food truck to the food_trucks list
    food_trucks.append(data)
    return jsonify({"message": "Food truck added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
