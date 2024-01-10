from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')


#Creating
@api.route('/plants', methods = ['POST'])
#@token_required
def create_plant():

    print(request.json)
    name = request.json['name']
    family = request.json['family']
    genus = request.json['genus']
    species = request.json['species']
    common_name =request.json['common_name']
    origin = request.json['origin']
    uid = request.json['uid']

    #print(f'BIG TESTER: {current_user_token.token}')




    contact = Contact(name, family, genus, species, common_name, origin, uid)
    print(contact)
    db.session.add(contact)
    db.session.commit()

    response = contact_schema.dump(contact)
    return jsonify(response)
#Retrieving all 
@api.route('/plants/user/<uid>', methods=['GET'])
# @token_required
def get_all_plants(uid):
    contacts=Contact.query.filter_by(uid=uid).all()
    response=contacts_schema.dump(contacts)
    return jsonify(response)


#Retrieving single
@api.route('/plants/<id>',methods=['GET'])
#@token_required
def get_single_plant(id):
    contact=Contact.query.get(id)
    response=contact_schema.dump(contact)
    return jsonify(response)

#Updating
@api.route('/plants/<id>', methods=['POST','PUT'])
#@token_required
def update_car( id):
    contact=Contact.query.get(id)
    uid= request.json['uid']
    if contact.uid != uid:
        return {'status':"invalid user"}, 400
    contact.name = request.json['name']
    contact.family = request.json['family']
    contact.genus = request.json['genus']
    contact.species = request.json['species']
    contact.common_name =request.json['common_name']
    contact.origin = request.json['origin']

    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)

#Deleting car
@api.route('/plants/<id>', methods=['DELETE'])
#@token_required
def delete_car(id):
    contact= Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    response= contact_schema.dump(contact)
    return jsonify(response)