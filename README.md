# 🔬 Breast Cancer Prediction App

A beautiful, interactive web application for breast cancer diagnosis prediction using machine learning. Built with Streamlit and powered by Logistic Regression.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- **Interactive UI**: Modern, gradient-based design with intuitive controls
- **Real-time Predictions**: Instant breast cancer diagnosis classification (Benign/Malignant)
- **Probability Scores**: Displays confidence levels for each prediction
- **30 Input Features**: Comprehensive tumor characteristic analysis including:
  - Mean values (radius, texture, perimeter, area, etc.)
  - Standard error measurements
  - Worst-case measurements
- **Medical Recommendations**: Provides actionable next steps based on predictions
- **Responsive Design**: Works seamlessly on desktop and mobile devices

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/BenDatta/Logistic_regression_streamlit_app.git
   cd Logistic_regression_streamlit_app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run cancer_app.py
   ```

5. **Open your browser**
   
   The app will automatically open at `http://localhost:8502`

## 📦 Project Structure

```
Logistic_regression_streamlit_app/
│
├── cancer_app.py                    # Main Streamlit application
├── cancer_prediction_model.pkl      # Trained Logistic Regression model
├── cancer.png                       # App header image
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## 🧠 Model Information

- **Algorithm**: Logistic Regression
- **Dataset**: Wisconsin Breast Cancer Dataset
- **Features**: 30 cellular characteristics
- **Target Classes**: 
  - Benign (0)
  - Malignant (1)

### Features Used

The model uses 30 features derived from digitized images of fine needle aspirate (FNA) of breast masses:

**Mean Values:**
- Radius, Texture, Perimeter, Area, Smoothness
- Compactness, Concavity, Concave Points
- Symmetry, Fractal Dimension

**Standard Error (SE) Values:**
- Same 10 features as above

**Worst Values:**
- Same 10 features as above (worst/largest values)

## 📊 Usage

1. **Adjust Input Features**: Use the sidebar sliders to input tumor characteristics
2. **Click Predict**: Press the "🔍 Predict Diagnosis" button
3. **View Results**: 
   - See the prediction (Benign/Malignant)
   - Check the probability score
   - Read the medical recommendation

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[scikit-learn](https://scikit-learn.org/)**: Machine learning model
- **[pandas](https://pandas.pydata.org/)**: Data manipulation
- **[NumPy](https://numpy.org/)**: Numerical computing
- **[Pillow](https://pillow.readthedocs.io/)**: Image processing

## ⚠️ Medical Disclaimer

**IMPORTANT**: This application is for educational and informational purposes only. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare professionals with any questions you may have regarding a medical condition.
