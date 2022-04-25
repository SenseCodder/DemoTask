from numpy import DataSource, empty
from model import db, demograpic_data
from flask import request,jsonify,make_response
from sqlalchemy import inspect
from config import app,engine
import chardet
import pandas as pd
import filterdata
import os


app.route(filterdata)

@app.route('/', methods=['GET'])
def home():
    print(f'headers:{request.headers}')
    return "<h1>See Chart Of Demographic_Data</h1>"    



def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#load data into database    
def setdata():
    

     if not os.path.exists(app.config['IMAGES_FOLDER']):
        os.mkdir(app.config['IMAGES_FOLDER'])
     with open('2015-2016_Demographic_Data_-_Grades_K-8_School.csv','rb') as f:
        result = chardet.detect(f.read())
        
        df = pd.read_csv('2015-2016_Demographic_Data_-_Grades_K-8_School.csv',encoding= result["encoding"]) 
        df = df.fillna(0)
        inspector = inspect(engine)
        
        ret = inspector.has_table('demograpic_data')
        
        if len(demograpic_data.query.all()) == 0:
            array = df.values.tolist()
            for i in range(0, len(array)): 
               
               demo_data  =  demograpic_data(array[i][0],array[i][1],array[i][2],array[i][3],int(array[i][4]) if isfloat(array[i][4]) else 0,int(array[i][5]) if isfloat(array[i][5]) else 0,int(array[i][6]) if isfloat(array[i][6]) else 0,int(array[i][7]) if isfloat(array[i][7]) else 0,int(array[i][8]) if isfloat(array[i][8]) else 0,int(array[i][9]) if isfloat(array[i][9]) else 0,int(array[i][10]) if isfloat(array[i][10]) else 0,int(array[i][11]) if isfloat(array[i][11]) else 0,int(array[i][12]) if isfloat(array[i][12]) else 0,int(array[i][13]) if isfloat(array[i][13]) else 0,int(array[i][14]) if isfloat(array[i][14]) else 0,float(array[i][15]) if isfloat(array[i][15]) else 0,int(array[i][16]) if isfloat(array[i][16]) else 0,float(array[i][17]) if isfloat(array[i][17]) else 0,int(array[i][18]) if isfloat(array[i][18]) else 0,float(array[i][19]) if isfloat(array[i][19]) else 0,int(array[i][20]) if isfloat(array[i][20]) else 0,float(array[i][21]) if isfloat(array[i][21]) else 0,int(array[i][22]) if isfloat(array[i][22]) else 0,float(array[i][23]) if isfloat(array[i][23]) else 0,int(array[i][24]) if isfloat(array[i][24]) else 0,float(array[i][25]) if isfloat(array[i][25]) else 0,int(array[i][26]) if isfloat(array[i][26]) else 0,float(array[i][27]) if isfloat(array[i][27]) else 0,int(array[i][28]) if isfloat(array[i][28]) else 0,float(array[i][29]) if isfloat(array[i][29]) else 0,int(array[i][30]) if isfloat(array[i][30]) else 0,float(array[i][31]) if isfloat(array[i][31]) else 0,int(array[i][32]) if isfloat(array[i][32]) else 0,float(array[i][33]) if isfloat(array[i][33]) else 0,int(array[i][34]) if isfloat(array[i][34]) else 0,float(array[i][35]) if isfloat(array[i][35]) else 0,int(array[i][36]) if isfloat(array[i][36]) else 0,float(array[i][37]) if isfloat(array[i][37]) else 0,int(array[i][38]) if isfloat(array[i][38]) else 0,float(array[i][39]) if isfloat(array[i][39]) else 0,int(array[i][40]) if isfloat(array[i][40]) else 0,float(array[i][41]) if isfloat(array[i][41]) else 0,int(array[i][42]) if isfloat(array[i][42]) else 0,float(array[i][43]) if isfloat(array[i][43]) else 0,int(array[i][44]) if isfloat(array[i][44]) else 0,float(array[i][45]) if isfloat(array[i][45]) else 0,int(array[i][46]) if isfloat(array[i][46]) else 0,float(array[i][47]) if isfloat(array[i][47]) else 0,int(array[i][48]) if isfloat(array[i][48]) else 0,int(array[i][49]) if isfloat(array[i][49]) else 0,float(array[i][50]) if isfloat(array[i][50]) else 0,int(array[i][51]) if isfloat(array[i][51]) else 0,float(array[i][52]) if isfloat(array[i][52]) else 0,int(array[i][53]) if isfloat(array[i][53]) else 0,float(array[i][54]) if isfloat(array[i][54]) else 0,int(array[i][55]) if isfloat(array[i][55]) else 0,float(array[i][56]) if isfloat(array[i][56]) else 0,int(array[i][57]) if isfloat(array[i][57]) else 0,float(array[i][58]) if isfloat(array[i][58]) else 0,int(array[i][59]) if isfloat(array[i][59]) else 0,int(array[i][60]) if isfloat(array[i][60]) else 0,float(array[i][61]) if isfloat(array[i][61]) else 0,int(array[i][62]) if isfloat(array[i][62]) else 0,float(array[i][63]) if isfloat(array[i][63]) else 0,int(array[i][64]) if isfloat(array[i][64]) else 0,float(array[i][65]) if isfloat(array[i][65]) else 0,int(array[i][66]) if isfloat(array[i][66]) else 0,float(array[i][67]) if isfloat(array[i][67]) else 0,int(array[i][68]) if isfloat(array[i][68]) else 0,float(array[i][69]) if isfloat(array[i][69]) else 0)
            
               db.session.add(demo_data)
               db.session.commit()
if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debugger shell
    # if you hit an error while running the
   
    with app.app_context():   
        setdata()
       
    app.run(debug=True)
  
    
    
    