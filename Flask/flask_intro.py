
from flask import Flask,request,render_template  #load flask and realtive libraries
from flask_sqlalchemy import SQLAlchemy #load library to connect the database
import pickle   #load the package to import the trained model
import numpy as np   #used to transfer the variable into the input data type of the model
import config   #import the credential

app = Flask(__name__,static_url_path='/static')   #create the flask application

app.config.from_object(config) #connect db
db= SQLAlchemy(app)

#creat a table in db
#class Article(db.Model):
#    __tablename__='article'
#    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#    title=db.Column(db.String(100),nullable=False)

#db.create_all()#check if connected with db


class Player(db.Model): #create the database model to save the user input from the front end
    __tablename__='player' #creare a table "player"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)  #id
    Age=db.Column(db.Integer) #age
    Wage=db.Column(db.Integer) #wage
    Overall_Rating=db.Column(db.Integer) #overall_rating
    Potential=db.Column(db.Integer) #potential
    Composure=db.Column(db.Integer) #composure
    Marking=db.Column(db.Integer) #marking
    Reactions=db.Column(db.Integer) #reaction
    Vision=db.Column(db.Integer) #vision
    Volleys=db.Column(db.Integer) #volleys
    Num_Positions=db.Column(db.Integer) #num_positions
    
db.create_all()

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html') #render the index page; no input needed
    
    
    #article1=Article(title='aaa') #input data to db
    #db.session.add(article1)
    #db.session.commit()
    '''
    context={
            'username':u'Vincent',
            'gender':u'Male',
            'age':u'Age'
            }
    '''

#render_template('index.html',age=u'100')
#**context


@app.route('/', methods = ['POST']) #create post method to get the user input from the front end
def model(): #create model function to run the model and generate the output to the result page
    
    #get the input from front end
    Age = request.form['Age'] 
    Wage = request.form['Wage']
    Overall_Rating = request.form['Overall_Rating']
    Potential = request.form['Potential']
    Composure = request.form['Composure']
    Marking = request.form['Marking']
    Reactions = request.form['Reactions']
    Vision = request.form['Vision']
    Volleys = request.form['Volleys']
    Num_Positions = request.form['Num_Positions']
    
    player1=Player(Age=Age,Wage=Wage,Overall_Rating=Overall_Rating,Potential=Potential,Composure=Composure,
                   Marking=Marking,Reactions=Reactions,Vision=Vision,Volleys=Volleys,Num_Positions=Num_Positions) #load the input into the database
    db.session.add(player1)
    db.session.commit() #update the info
    #return render_template('index.html',Age=Age)
    
    
    #set model input in to numpy array format
    input_array=np.ndarray(shape=(1,10), dtype=float, order='F')
    input_array[0][0]=Age #age
    input_array[0][1]=Wage #Wage
    input_array[0][2]=Overall_Rating #Overall_Rating
    input_array[0][3]=Potential #Potential
    input_array[0][4]=Composure #Composure
    input_array[0][5]=Marking #Marking
    input_array[0][6]=Reactions #Reactions
    input_array[0][7]=Vision #Vision
    input_array[0][8]=Volleys #Volleys
    input_array[0][9]=Num_Positions #Num_Positions
    
    
    pkl_file = open('static/model/rfr.pkl', 'rb') #open the pickle model
    random_forest_model = pickle.load(pkl_file)
    raw_output= random_forest_model.predict(input_array) #predict using the model
    real_output=raw_output[0] #generate the output
    
    return render_template('result.html',prediction=real_output) #render the new page with output
    
#    if (Age == 'Age'or Wage == 'Wage' ):
#        return '<h3> test succeed</h3>'
#    else:
#        return '<h3> invalid_Age </h3>'
    
if __name__ == '__main__':
	app.run(host='0.0.0.0')
