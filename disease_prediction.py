
# Importing libraries
from PIL import Image

import streamlit as st
import numpy as np
import pandas as pd
import pickle


# Loading the trained models 

model2 = pickle.load(open(r'C:/Users/kling/Downloads/Diseases-Prediction-with-Streamlit-master/Diseases-Prediction-with-Streamlit-master/kidney.pkl','rb'))


# Title of the webpage
st.title('Disease Prediction')

# List of predictions to be made
dis =['Chronic Kidney Disease',]

# List of predictions are given under dropdown or select box in sidebar
selected_pred = st.sidebar.selectbox('Predict',dis)

    
# checks for other prediction, if prediction is True gets the input       
if selected_pred=='Chronic Kidney Disease':
    
    st.markdown('''***Chronic kidney disease (CKD)*** means your kidneys are damaged and can't filter blood the way they should. The main risk factors for developing kidney disease are diabetes, high blood pressure, heart disease, and a family history of kidney failure''')
    image = Image.open(r"C:/Users/kling/Downloads/Diseases-Prediction-with-Streamlit-master/Diseases-Prediction-with-Streamlit-master/images")
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
    								


            
    								
    
    
    




    
    


