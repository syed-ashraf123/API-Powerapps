from flask import Flask
from flask_restful import reqparse,Api,Resource
app=Flask(__name__)
api=Api(app)
req=reqparse.RequestParser()
req.add_argument("name1",type=str,help="You didnt send name")
req.add_argument("age",type=int,help="You didnt send name")
class Hello(Resource):
	def get(self,name):
		return {"data":name}
api.add_resource(Hello,'/Hello/<string:name>')
if __name__=="__main__":
	app.run(debug=True)