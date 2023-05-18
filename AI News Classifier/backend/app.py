from flask import Flask, session, request, redirect, render_template, url_for, jsonify, send_file
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from pred_model import label

app = Flask(__name__)



CORS(app, supports_credentials=True)


basedir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SECRET_KEY']='1234dfghjk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'everything.db')
db = SQLAlchemy(app)
db.init_app(app)
app.app_context().push()
app.secret_key = '1234dfghjk'
app.app_context().push()

#api
api = Api(app)
app.app_context().push()


class ListModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False, unique = True)
    label = db.Column(db.String, nullable=True)
    key_words = db.Column(db.String, nullable=True)

db.create_all()


list_resource_fields = {
    'id': fields.Integer,
    'url': fields.String,
    'label': fields.String,
    'key_words': fields.String
}

list_put_args = reqparse.RequestParser()
list_put_args.add_argument("URL", type=str, help="url is required", required=True)


class List(Resource):
    

    @marshal_with(list_resource_fields)
    def get(self):
        list = ListModel.query.all()
        return list, 201

    @marshal_with(list_resource_fields)
    def put(self):
        args = list_put_args.parse_args()
        existing = ListModel.query.filter_by(url = args["URL"]).first()
        if(existing):
            return existing, 201
        model = label(args["URL"])
        list = ListModel(url=args['URL'], label = model[0], key_words = model[1] )
        db.session.add(list)
        db.session.commit()
        return list, 201


api.add_resource(List, "/dashboard")



if __name__ == "__main__":
    app.run(debug = True) 
