#!/usr/bin/python3
"""Index page for site"""
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects:
    """Retrieves the number of each object"""
    cls = [Amenity, City, Place, Review, State, User]
    names = ['amenities', 'cities', 'places', 'reviews', 'states', 'users']
    objs = {}
    for i in range(len(cls)):
        objs[names[i]] = storage.count(classes[i])
    return jsonify(objs)
