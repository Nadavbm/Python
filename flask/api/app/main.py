from flask import Flask, jsonify, request

# Create flask app
app = Flask(__name__)

# Create address book
people = [{'name' : 'Shimi', 'nachname' : 'Tavori', 'address' : 'Naharia, HaYorkim 32'}, {'name' : 'Margol', 'nachname' : 'Zanani', 'address' : 'Bagdad, Rehov Tesha 1092, Metula'}, {'name' : 'Ohevet', 'nachname' : 'Hazilim', 'address' : 'Tiberias, Kebab HaZoem 19'}]

# Navigate between pages
@app.route('/', methods=['GET'])
def index():
    return 'It works!'

@app.route('/json', methods=['GET'])
def jsonIndex():
    return jsonify({'message' : 'It works!'}) 

@app.route('/people', methods=['GET'])
def allPeople():
    return jsonify({'people' : people})

#@app.route('person/<string:name>', methods=['GET'])
#def firstPerson():
#    address = [person for person in people if person['name'] == name]
#    return jsonify([{'person' : address[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
