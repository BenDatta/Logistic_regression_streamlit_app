import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(to bottom, #f8f9fa 0%, #e9ecef 100%);
    }
    .prediction-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to bottom, #f8f9fa 0%, #ffffff 100%);
    }
    h1 {
        font-weight: 700;
        font-size: 2.5rem;
    }
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin: 0.5rem 0;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-size: 0.9rem;
        margin-top: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    import os
    model_path = 'cancer_prediction_model.pkl'
    
    if not os.path.exists(model_path):
        st.error(f"❌ Model file not found at: {os.path.abspath(model_path)}")
        st.info("Please ensure 'cancer_prediction_model.pkl' is in the same directory as this script.")
        st.stop()
    
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()

pipeline = load_model()

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="header-container">
            <h1>🔬 Breast Cancer Prediction System</h1>
            <p style="font-size: 1.2rem; margin-top: 1rem; opacity: 0.9;">
                Advanced machine learning model for early detection and diagnosis
            </p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    try:
        image = Image.open('cancer.png')
        st.image(image, use_container_width=True)
    except:
        st.info("Place 'cancer.png' in the same directory as this script")

st.markdown("""
    <div style="background: white; padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <h3 style="color: #667eea; margin-bottom: 1rem;">📊 About This Tool</h3>
        <p style="color: #666; line-height: 1.6;">
            This application uses a <strong>Logistic Regression model</strong> trained on the Wisconsin Breast Cancer Dataset 
            to predict whether a tumor is <strong>Benign</strong> (non-cancerous) or <strong>Malignant</strong> (cancerous) 
            based on 30 cellular characteristics extracted from digitized images of fine needle aspirate (FNA) of breast masses.
        </p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 10px; margin-bottom: 1.5rem;">
        <h2 style="color: white; margin: 0;">⚙️ Input Features</h2>
        <p style="color: rgba(255,255,255,0.9); margin-top: 0.5rem; font-size: 0.9rem;">
            Adjust the tumor characteristics below
        </p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 📏 Mean Values")
radius_mean = st.sidebar.slider('Radius Mean', 6.0, 30.0, 14.0, 0.1)
texture_mean = st.sidebar.slider('Texture Mean', 9.0, 40.0, 19.0, 0.1)
perimeter_mean = st.sidebar.slider('Perimeter Mean', 43.0, 190.0, 92.0, 0.5)
area_mean = st.sidebar.slider('Area Mean', 143.0, 2501.0, 654.0, 1.0)
smoothness_mean = st.sidebar.slider('Smoothness Mean', 0.05, 0.16, 0.10, 0.001)
compactness_mean = st.sidebar.slider('Compactness Mean', 0.02, 0.35, 0.10, 0.01)
concavity_mean = st.sidebar.slider('Concavity Mean', 0.0, 0.43, 0.09, 0.01)
concave_points_mean = st.sidebar.slider('Concave Points Mean', 0.0, 0.20, 0.05, 0.01)
symmetry_mean = st.sidebar.slider('Symmetry Mean', 0.10, 0.30, 0.18, 0.01)
fractal_dimension_mean = st.sidebar.slider('Fractal Dimension Mean', 0.05, 0.10, 0.06, 0.001)

st.sidebar.markdown("### 📊 Standard Error Values")
radius_se = st.sidebar.slider('Radius SE', 0.1, 2.9, 0.4, 0.01)
texture_se = st.sidebar.slider('Texture SE', 0.4, 5.0, 1.2, 0.1)
perimeter_se = st.sidebar.slider('Perimeter SE', 0.8, 22.0, 2.9, 0.1)
area_se = st.sidebar.slider('Area SE', 6.0, 542.0, 40.0, 1.0)
smoothness_se = st.sidebar.slider('Smoothness SE', 0.001, 0.03, 0.007, 0.001)
compactness_se = st.sidebar.slider('Compactness SE', 0.002, 0.14, 0.025, 0.001)
concavity_se = st.sidebar.slider('Concavity SE', 0.0, 0.40, 0.03, 0.01)
concave_points_se = st.sidebar.slider('Concave Points SE', 0.0, 0.05, 0.01, 0.001)
symmetry_se = st.sidebar.slider('Symmetry SE', 0.008, 0.08, 0.02, 0.001)
fractal_dimension_se = st.sidebar.slider('Fractal Dimension SE', 0.001, 0.03, 0.004, 0.001)

st.sidebar.markdown("### 📈 Worst Values")
radius_worst = st.sidebar.slider('Radius Worst', 7.0, 36.0, 16.0, 0.1)
texture_worst = st.sidebar.slider('Texture Worst', 12.0, 50.0, 25.0, 0.1)
perimeter_worst = st.sidebar.slider('Perimeter Worst', 50.0, 251.0, 107.0, 0.5)
area_worst = st.sidebar.slider('Area Worst', 185.0, 4254.0, 880.0, 1.0)
smoothness_worst = st.sidebar.slider('Smoothness Worst', 0.07, 0.22, 0.13, 0.01)
compactness_worst = st.sidebar.slider('Compactness Worst', 0.03, 1.06, 0.25, 0.01)
concavity_worst = st.sidebar.slider('Concavity Worst', 0.0, 1.25, 0.27, 0.01)
concave_points_worst = st.sidebar.slider('Concave Points Worst', 0.0, 0.29, 0.11, 0.01)
symmetry_worst = st.sidebar.slider('Symmetry Worst', 0.16, 0.66, 0.29, 0.01)
fractal_dimension_worst = st.sidebar.slider('Fractal Dimension Worst', 0.055, 0.21, 0.08, 0.001)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
    <div style="background: #fff3cd; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #dc3545; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin: 1rem 0;">
        <p style="color: #721c24; font-weight: 700; margin: 0; font-size: 1.1rem; line-height: 1.6;">
            ⚠️ <strong>Medical Disclaimer:</strong> This is a machine learning prediction tool and should NOT replace professional medical diagnosis. Always consult with qualified healthcare professionals for accurate diagnosis and treatment.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button('🔍 Predict Diagnosis'):
    features = pd.DataFrame({
        'radius_mean': [radius_mean],
        'texture_mean': [texture_mean],
        'perimeter_mean': [perimeter_mean],
        'area_mean': [area_mean],
        'smoothness_mean': [smoothness_mean],
        'compactness_mean': [compactness_mean],
        'concavity_mean': [concavity_mean],
        'concave points_mean': [concave_points_mean],
        'symmetry_mean': [symmetry_mean],
        'fractal_dimension_mean': [fractal_dimension_mean],
        'radius_se': [radius_se],
        'texture_se': [texture_se],
        'perimeter_se': [perimeter_se],
        'area_se': [area_se],
        'smoothness_se': [smoothness_se],
        'compactness_se': [compactness_se],
        'concavity_se': [concavity_se],
        'concave points_se': [concave_points_se],
        'symmetry_se': [symmetry_se],
        'fractal_dimension_se': [fractal_dimension_se],
        'radius_worst': [radius_worst],
        'texture_worst': [texture_worst],
        'perimeter_worst': [perimeter_worst],
        'area_worst': [area_worst],
        'smoothness_worst': [smoothness_worst],
        'compactness_worst': [compactness_worst],
        'concavity_worst': [concavity_worst],
        'concave points_worst': [concave_points_worst],
        'symmetry_worst': [symmetry_worst],
        'fractal_dimension_worst': [fractal_dimension_worst]
    })
    
    with st.spinner('Analyzing tumor characteristics...'):
        prediction = pipeline.predict(features)[0]
        prediction_proba = pipeline.predict_proba(features)[0]
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    if prediction == 1:
        with col1:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); 
                            padding: 2rem; border-radius: 15px; color: white; text-align: center;
                            box-shadow: 0 8px 16px rgba(238, 90, 111, 0.3);">
                    <h2 style="margin: 0;">🔴 Malignant</h2>
                    <p style="font-size: 2rem; margin: 1rem 0; font-weight: bold;">
                        {prediction_proba[1]:.1%}
                    </p>
                    <p style="opacity: 0.9;">Probability of malignancy</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div style="background: white; padding: 2rem; border-radius: 15px; 
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <h3 style="color: #ff6b6b; margin-top: 0;">⚠️ Recommendation</h3>
                    <p style="color: #666; line-height: 1.6;">
                        This result suggests the tumor may be <strong>malignant</strong>. 
                        Please consult with an oncologist immediately for further diagnostic 
                        tests and treatment options.
                    </p>
                </div>
            """, unsafe_allow_html=True)
    else:
        with col1:
            st.markdown(f"""
                <div style="background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%); 
                            padding: 2rem; border-radius: 15px; color: white; text-align: center;
                            box-shadow: 0 8px 16px rgba(86, 171, 47, 0.3);">
                    <h2 style="margin: 0;">🟢 Benign</h2>
                    <p style="font-size: 2rem; margin: 1rem 0; font-weight: bold;">
                        {prediction_proba[0]:.1%}
                    </p>
                    <p style="opacity: 0.9;">Probability of being benign</p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div style="background: white; padding: 2rem; border-radius: 15px; 
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <h3 style="color: #56ab2f; margin-top: 0;">✅ Recommendation</h3>
                    <p style="color: #666; line-height: 1.6;">
                        This result suggests the tumor is likely <strong>benign</strong>. 
                        Continue regular monitoring and follow-up appointments as recommended 
                        by your healthcare provider.
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        <p><strong>Model Information</strong></p>
        <p>Logistic Regression trained on Wisconsin Breast Cancer Dataset</p>
        <p style="font-size: 0.8rem; margin-top: 1rem; opacity: 0.7;">
            © 2025 Breast Cancer Prediction System | For Educational Purposes Only
        </p>
    </div>
""", unsafe_allow_html=True)