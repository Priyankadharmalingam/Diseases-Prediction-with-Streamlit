
# Importing libraries
from PIL import Image

import streamlit as st
import numpy as np
import pandas as pd
import pickle


# Loading the trained models 

model1 = pickle.load(open(r'c:\Users\rajal\My practice codes\Web frameworks\diabetes_pred.pkl','rb'))
model2 = pickle.load(open(r'c:\Users\rajal\GISMA\log_ckd_pred.pkl','rb'))
model3 = pickle.load(open(r'c:\Users\rajal\My practice codes\Web frameworks\heart_dis_pred.pkl','rb'))

# Title of the webpage
st.title('Disease Prediction')

# List of predictions to be made
dis =['Diabetes','Chronic Kidney Disease','Heart Disease']

# List of predictions are given under dropdown or select box in sidebar
selected_pred = st.sidebar.selectbox('Predict',dis)

# with condition is True,  getting the input values of particular prediction with st.text_input
if selected_pred=='Diabetes':
    
    st.markdown("**Diabetes** is a chronic (long-lasting) health condition that affects how your body turns food into energy. Most of the food you eat is broken down into sugar (also called glucose) and released into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin.")
    image = Image.open("C:/Users/rajal/Desktop/Streamlit/diabetes.png")
    st.image(image, use_column_width= True)
    st.subheader('Enter the values to check if you have Diabetes or Not')
    
    Pregnancies = st.number_input('Pregnancies')
    Glucose = st.number_input('Glucose')
    BloodPressure= st.number_input('BloodPressure')
    SkinThickness = st.number_input('SkinThickness')
    Insulin = st.number_input('Insulin')
    BMI = st.number_input('BMI')
    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
    Age = st.number_input('Age')
    
    
    # Inside this list we get all the input features. Also for features with categorical feature here we get the values from dictionary
    # To get the value we use function get_value()
    feature_list = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]   
    st.write('No of features: ')
    st.write(len(feature_list))
    st.write('Your Input: ')
    result = {'Pregnancies':Pregnancies,'Glucose': Glucose,'BloodPressure': BloodPressure,'SkinThickness':SkinThickness,'Insulin': Insulin,'BMI':BMI,'DiabetesPedigreeFunction':DiabetesPedigreeFunction,'Age': Age}
    st.json(result)
    
    # pressing the button predict will take the inputs and predict with the loaded model     
    if st.button('Predict'):
        result = model1.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        st.write('Prediction probability')
        pred_prob = model1.predict_proba([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        pred_prob_score = {'No_Diabetes':pred_prob[0][0]*100,'Diabetes':pred_prob[0][1]*100}
        st.json(pred_prob_score)
        if result==1:
            st.success('Sorry, it seems you have diabetes. Please consult a doctor')
        else:
            st.success('You donot have diabetes!!')
            
        st.write('Prevent Diabetes')
        st.markdown('''
                       1. Lose extra weight
                    
                       2. Be more physically active
                    
                       3. Eat healthy plant foods
                    
                       4. Eat healthy fats
                    
                       5. Skip fad diets and make healthier choices
                   
                    ''')
            
            
    
 
            



# Created dictionaries with key value pairs for categorical features , so that easy to get input from the users
# The categorical features are encoded as in the model 
nab_dict = {'normal': 1,'abnormal': 0}
pnp_dict = {'present': 1,'notpresent':0 }
Appetite_dict = {'poor': 1,'good': 0}
feature_dict = {'yes':1 ,'no': 0}

# Within the fun we check if the input value is equal to the key and return the value
def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val==key:
            return value
        
# checks for other prediction, if prediction is True gets the input       
if selected_pred=='Chronic Kidney Disease':
    
    st.markdown('''***Chronic kidney disease (CKD)*** means your kidneys are damaged and can't filter blood the way they should. The main risk factors for developing kidney disease are diabetes, high blood pressure, heart disease, and a family history of kidney failure''')
    image = Image.open(r"C:\Users\rajal\Desktop\Streamlit\kidney.png")
    st.image(image, use_column_width= True)
    st.subheader('Enter the values to check if you have Ckd or Not')
    
    
    Age = st.number_input('Age')
    Blood_pressure = st.number_input('Blood_pressure')
    Specific_gravity = st.number_input('Specific_gravity')
    Albumin	= st.number_input('Albumin')
    Sugar  = st.number_input('Sugar ')
                                                                           
    Blood_glucose_random = st.number_input('Blood_glucose_random')
    Blood_urea = st.number_input('Blood_urea')
    Serum_creatinine = st.number_input('Serum_creatinine')
    Sodium = st.number_input('Sodium')
    Potassium = st.number_input('Potassium')
    Hemoglobin = st.number_input('Hemoglobin')
    Packed_cell_volume = st.number_input('Packed_cell_volume')
    White_blood_cell_count = st.number_input('White_blood_cell_count')
    Red_blood_cell_count = st.number_input('Red_blood_cell_count')
    
    # Got the input as categorical value using st.radio and getting the key values from a dictionary 
    # Here inside the radio button we get the keys from dictionary
    Red_blood_cells  = st.radio('Red_blood_cells',tuple(nab_dict.keys()))              
    Pus_cell =   st.radio('Pus_cell',tuple(nab_dict.keys()))                                                                                          
    Pus_cell_clumps  =  st.radio('Pus_cell_clumps',tuple(pnp_dict.keys()))                                                                       
    Bacteria  =    st.radio('Bacteria',tuple(pnp_dict.keys()))  
    Hypertension=    st.radio('Hypertension',tuple(feature_dict.keys()))                                                                      
    Diabetes_mellitus =   st.radio('Diabetes_mellitus',tuple(feature_dict.keys()))                                                                     
    Coronary_artery_disease =   st.radio('Coronary_artery_disease',tuple(feature_dict.keys()))                                                          
    Appetite =  st.radio('Appetite ',tuple(Appetite_dict.keys()))                                                                         
    Pedal_edema	=  st.radio('Pedal_edema',tuple(feature_dict.keys()))                                                                       
    Anemia		=  st.radio('Anemia',tuple(feature_dict.keys()))
    
    # Inside this list we get all the input features. Also for features with categorical feature here we get the values from dictionary
    # To get the value we use function get_value()
    feature_list_ckd = [Age, Blood_pressure, Specific_gravity, Albumin, Sugar, Blood_glucose_random, Blood_urea,Serum_creatinine, Sodium, Potassium, Hemoglobin, Packed_cell_volume, White_blood_cell_count, Red_blood_cell_count, get_value(Anemia,feature_dict),  get_value(Pedal_edema,feature_dict), get_value(Coronary_artery_disease,feature_dict), get_value(Diabetes_mellitus,feature_dict),get_value(Hypertension,feature_dict),  get_value(Appetite , Appetite_dict), get_value(Pus_cell_clumps,pnp_dict) ,get_value(Bacteria,pnp_dict),get_value(Red_blood_cells, nab_dict), get_value(Pus_cell,nab_dict)]   
    st.write('No of features: ')
    st.write(len(feature_list_ckd))
    st.write('Your Input: ')
    result = {'Age': Age, 'Blood_pressure': Blood_pressure, 'Specific_gravity': Specific_gravity, 'Albumin': Albumin,'Sugar': Sugar, 'Blood_glucose_random': Blood_glucose_random, 'Blood_urea': Blood_urea,'Serum_creatinine': Serum_creatinine, 'Sodium': Sodium,'Potassium':  Potassium,'Hemoglobin':  Hemoglobin, 'Packed_cell_volume': Packed_cell_volume,'White_blood_cell_count':  White_blood_cell_count, 'Red_blood_cell_count': Red_blood_cell_count,'Anemia':  get_value(Anemia,feature_dict),'Pedal_edema':get_value(Pedal_edema,feature_dict),'Coronary_artery_disease': get_value(Coronary_artery_disease,feature_dict), 'Diabetes_mellitus': get_value(Diabetes_mellitus,feature_dict),'Hypertension': get_value(Hypertension,feature_dict),'Appetite':  get_value(Appetite , Appetite_dict) ,'Pus_cell_clumps,': get_value(Pus_cell_clumps,pnp_dict),'Bacteria': get_value(Bacteria,pnp_dict),'Red_blood_cell': get_value(Red_blood_cells, nab_dict), 'Pus_cell':get_value(Pus_cell,nab_dict)}
    st.json(result)

                                                                  
    
    
    if st.button('Predict'):
        result = model2.predict([feature_list_ckd])
        st.write('Prediction probability')
        pred_prob = model2.predict_proba([[feature_list_ckd]])
        pred_prob_score = {'No_ckd':pred_prob[0][0]*100,'ckd':pred_prob[0][1]*100}
        st.json(pred_prob_score)
       
        if result==1:
            st.success('Sorry, it seems you have Chronic Kidney Disease. Please consult a doctor')
        else:
            st.success('You donot have CKD!!')
    								

if selected_pred=='Heart Disease':
    
    st.markdown('''**Heart disease** encompasses a wide range of cardiovascular problems. Several diseases and conditions fall under the umbrella of heart disease. 
                Types of heart disease include:
                *Arrhythmia* An arrhythmia is a heart rhythm abnormality.
                *Atherosclerosis*. Atherosclerosis is a hardening of the arteries.
                *Cardiomyopathy* This condition causes the heart’s muscles to harden or grow weak.
                *Congenital heart defect* Congenital heart defects are heart irregularities that are present at birth.
                *Coronary artery disease (CAD)* CAD is caused by the buildup of plaque in the heart’s arteries. It’s sometimes called ischemic heart disease.
                *Heart infections* Heart infections may be caused by bacteria, viruses, or parasites.
                The term *cardiovascular disease* may be used to refer to heart conditions that specifically affect the blood vessels''')
                
    image = Image.open(r"C:\Users\rajal\Desktop\Streamlit\heart.png")
    st.image(image, use_column_width= True)
    st.subheader('Enter the values to check if you have Heart Disease or Not')
    
    age	 = st.number_input('Age')
    sex	 = st.number_input('Sex')
    cp= st.number_input('Chest pain')
    trestbps = st.number_input('Resting blood pressure')
    chol = st.number_input('Serum cholestoral')
    fbs = st.number_input('Fasting Blood sugar')
    restecg= st.number_input('Resting electrocardiographic results( Enter 0,1 or 2)')
    thalach = st.number_input('Maximum heart rate achieved')
    exang= st.number_input('Exercise induced angina')
    oldpeak = st.number_input('ST depression induced by exercise relative to rest')
    slope = st.number_input('Slope of the peak exercise ST segment')
    ca = st.number_input('Number of major vessels (0-3) colored by flourosopy')
    thal = st.number_input('Thalassemia (Enter 0, 1 or 2 where 0 = normal; 1 = fixed defect; 2 = reversable defect)')
    
    feature_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]   
    st.write('No of features: ')
    st.write(len(feature_list ))
    st.write('Your Input: ')
    result = {'Age': age, 'Sex':sex, 'Chest pain':cp, 'Resting blood pressure': trestbps,'Serum cholestoral': chol, 'Fasting Blood sugar':  fbs, 'Resting electrocardiographic results( Enter 0,1 or 2)': restecg,'Maximum heart rate achieved': thalach, 'Exercise induced angina': exang,'ST depression induced by exercise relative to rest': oldpeak,'Slope of the peak exercise ST segment': slope, 'Number of major vessels (0-3) colored by flourosopy':  ca,'Thalassemia (Enter 0, 1 or 2 where 0 = normal; 1 = fixed defect; 2 = reversable defect)':thal}
    st.json(result)
    
    if st.button('Predict'):
        result = model3.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        st.write('Prediction probability')
        pred_prob = model3.predict_proba([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        pred_prob_score = {'No_Heart_Diesase':pred_prob[0][0]*100,'Heart Disease':pred_prob[0][1]*100}
        st.json(pred_prob_score)
       
        if result== 0:
            st.success('You donot have Heart disease!!')
            
        else:
            st.success('Sorry, it seems you have Heart Disease. Please consult a doctor')
            
    								
    
    
    




    
    


