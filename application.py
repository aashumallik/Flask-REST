from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model): #creating a model with sql alchemy
    id = db.Column(db.Integer, primary_key=True) #creating a coloumn with ID integer where primary key exists
    name = db.Column(db.String(80), unique=True, nullable=False) #creating a coloumn with name as a string with max 80 chars, always unique name and no null values
    description = db.Column(db.String(120))

    def __repr__(self) :
        return f"{self.name} - {self.description}"




@app.route('/')
def index():
    return 'Hello Pussy'
    
@app.route('/users') #writing a get method to return users
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_Data={'name': user.name,'description':user.description}

        output.append(user_Data)
    return {"users": output} #returning a dictionary with some dummy data

@app.route('/users/<id>')
def get_user(id):
    user=User.query.get_or_404(id)
    return {'name': user.name,'description':user.description}

@app.route('/users',methods=['POST'])
def add_user():
    user = User(name=request.json['name'],description=request.json['description'])
    db.session.add(user)
    db.session.commit()
    return {'id': user.id}

@app.route('/users/<id>', methods=['DELETE'])

def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return {"404"}
    db.session.delete(user)
    db.session.commit()
    return {"message": "Hell yeah BITCH"}
    


    