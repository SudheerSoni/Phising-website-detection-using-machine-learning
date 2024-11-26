import numpy as np
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]




from flask import Flask, request, jsonify, render_template
import joblib


from  url_features  import extract_features



# Load the model from the file 
model = joblib.load('xg_boost_recomondation.pkl')  
  
# Use the loaded model to make predictions 



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index2.html')


# @app.route('/register',methods=['POST'])
# def register():
    

#     int_features2 = [str(x) for x in request.form.values()]
#     #print(int_features2)
#     #print(int_features2[0])
#     #print(int_features2[1])
#     r1=int_features2[0]
#     print(r1)
    
#     r2=int_features2[1]
#     print(r2)
#     logu1=int_features2[0]
#     passw1=int_features2[1]
        
    

    


#     import MySQLdb


# # Open database connection
#     db = MySQLdb.connect("localhost","root",'',"ddbb" )

# # prepare a cursor object using cursor() method
#     cursor = db.cursor()
#     cursor.execute("SELECT user FROM user_register")
#     result1=cursor.fetchall()
#               #print(result1)
#               #print(gmail1)
#     for row1 in result1:
#                       print(row1)
#                       print(row1[0])
#                       gmail_list1.append(str(row1[0]))
                      

                      
#     print(gmail_list1)
#     if logu1 in gmail_list1:
                      
#                       return render_template('register.html',text="This Username is Already in Use ")
#     else:

                 
              

# # Prepare SQL query to INSERT a record into the database.
#                   sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
#                   val = (r1, r2)
   
#                   try:
#    # Execute the SQL command
#                                        cursor.execute(sql,val)
#    # Commit your changes in the database
#                                        db.commit()
#                   except:
#    # Rollback in case there is any error
#                                        db.rollback()

# # disconnect from server
#                   db.close()
                  
#                   return render_template('register.html',text="Succesfully Registered")
                
#                   return render_template('login.html')

                      
# @app.route('/login')
# def login(): 
#     return render_template('login.html')         
                      

# @app.route('/logedin',methods=['POST'])
# def logedin():
    
#     int_features3 = [str(x) for x in request.form.values()]
#     print(int_features3)
#     logu=int_features3[0]
#     passw=int_features3[1]

#     import MySQLdb
#     db = MySQLdb.connect("localhost","root","","ddbb" )

# # prepare a cursor object using cursor() method
#     cursor = db.cursor()
#     cursor.execute("SELECT user FROM user_register")
#     result1=cursor.fetchall()
            
#     for row1 in result1:
#                       print(row1)
#                       print(row1[0])
#                       gmail_list.append(str(row1[0]))
                      
              
                      
#     print(gmail_list)
    

#     cursor1= db.cursor()
#     cursor1.execute("SELECT password FROM user_register")
#     result2=cursor1.fetchall()
             
#     for row2 in result2:
#                       print(row2)
#                       print(row2[0])
#                       password_list.append(str(row2[0]))
                      
                 
                      
#     print(password_list)
#     print(gmail_list.index(logu))
#     print(password_list.index(passw))
    
#     if gmail_list.index(logu)==password_list.index(passw):
#         return render_template('index2.html')
#     else:
#         return render_template('login.html',text='Use Proper Username and Password')
                  
                                               



                          
              


@app.route('/production')
def production(): 
    return render_template('main_pagge.html')


@app.route('/production/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [str(x) for x in request.form.values()]


    print(int_features)
    #a=int_features

    #url_processed = url_features.main(a[0])
    list_inputs=extract_features(int_features[0])
    d={'URL_length':0,'Hostname_length':0,'IP_address':0,'Number_of_dots':0,'hyphens':0,'at_symbols':0,'question_marks':0,'ampersands':0,'Vertical_bar':0,'equal_signs':0,'underscores':0,'tildes':0,'percent_signs':0,'slashes':0,'Aistrisk':0,' colons':0,' commas':0,  'semicolons':0,' dollar_signs':0, 'spaces':0,  'www':0,'com':0,'double_slashes' :0, 'Domain_age':0, 'Web_traffic':0,'DNS_record ':0,'Google_index':0}
    d['URL_length']=list_inputs[0]
    d['Hostname_length']=list_inputs[1]
    d['IP_address']=list_inputs[2]
    d['Number_of_dots']=list_inputs[3]
    d['hyphens']=list_inputs[4]
    d['at_symbols']=list_inputs[5]
    d['question_marks']=list_inputs[6]
    d['ampersands']=list_inputs[7]
    d['Vertical_bar']=list_inputs[8]
    d['equal_signs']=list_inputs[9]
    d['underscores']=list_inputs[10]
    d['tildes']=list_inputs[11]
    d['percent_signs']=list_inputs[12]
    d['slashes']=list_inputs[13]
    d['Aistrisk']=list_inputs[14]
    d['colons']=list_inputs[15]
    d['commas']=list_inputs[16]
    d['semicolons']=list_inputs[17]
    d['dollar_signs']=list_inputs[18]
    d['spaces']=list_inputs[19]
    d['www']=list_inputs[20]
    d['com']=list_inputs[21]
    d['double_slashes']=list_inputs[22]
    d['Domain_age']=list_inputs[23]
    d['Web_traffic']=list_inputs[24]
    d['DNS_record']=list_inputs[25]
    d['Google_index']=list_inputs[26]

    
    url_processed =np.array([list_inputs])
    prediction=model.predict(url_processed)
    print(prediction)                                                                                                                                                                                              
    
    if prediction==1:
        return render_template('main_pagge.html',features= 'URL_length',features1='Hostname_length',features2='IP_address',features3='Number_of_dots',features4='hyphens',features5='at_symbols',features6='question_marks',features7='ampersands',features8='Vertical_bar',features9='equal_signs',features10='underscores',features11='tildes',features12='percent_signs',features13='slashes',features14='Aistrisk',features15='colons',features16='commas',features17='semicolons',features18=' dollar_signs',features19='spaces',features20='www',features21='com',features22='double_slashes',features23='Domain_age',features24='Web_traffic',features25='DNS_record',features26='Google_index',
                                            featuresa=d['URL_length'],featuresb=d['Hostname_length'],featuresc=d['IP_address'],featuresd=d['Number_of_dots'],featurese=d['hyphens'],featuresf=d['at_symbols'],featuresg=d['question_marks'],featuresh=d['ampersands'],featuresi=d['Vertical_bar'],featuresj=d['equal_signs'],featuresk=d['underscores'],featuresl=d['tildes'],featuresm=d['percent_signs'],featuresn=d['slashes'],featureso=d['Aistrisk'],featuresp=d['colons'],featuresq=d['commas'],featuresr=d['semicolons'],featuress=d['dollar_signs'],featurest=d['spaces'],featuresu=d['www'],featuresv=d['com'],featuresw=d['double_slashes'],featuresx=d['Domain_age'],featuresy=d['Web_traffic'],featuresz=d['DNS_record'],featuresaa=d['Google_index'],prediction_text='This is a Phishing Website')
    else:
        return render_template('main_pagge.html',features= 'URL_length',features1='Hostname_length',features2='IP_address',features3='Number_of_dots',features4='hyphens',features5='at_symbols',features6='question_marks',features7='ampersands',features8='Vertical_bar',features9='equal_signs',features10='underscores',features11='tildes',features12='percent_signs',features13='slashes',features14='Aistrisk',features15='colons',features16='commas',features17='semicolons',features18=' dollar_signs',features19='spaces',features20='www',features21='com',features22='double_slashes',features23='Domain_age',features24='Web_traffic',features25='DNS_record',features26='Google_index',
                                            featuresa=d['URL_length'],featuresb=d['Hostname_length'],featuresc=d['IP_address'],featuresd=d['Number_of_dots'],featurese=d['hyphens'],featuresf=d['at_symbols'],featuresg=d['question_marks'],featuresh=d['ampersands'],featuresi=d['Vertical_bar'],featuresj=d['equal_signs'],featuresk=d['underscores'],featuresl=d['tildes'],featuresm=d['percent_signs'],featuresn=d['slashes'],featureso=d['Aistrisk'],featuresp=d['colons'],featuresq=d['commas'],featuresr=d['semicolons'],featuress=d['dollar_signs'],featurest=d['spaces'],featuresu=d['www'],featuresv=d['com'],featuresw=d['double_slashes'],featuresx=d['Domain_age'],featuresy=d['Web_traffic'],featuresz=d['DNS_record'],featuresaa=d['Google_index'],prediction_text2='This is a legitimate Website')



if __name__ == "__main__":
    app.run(debug=True)
