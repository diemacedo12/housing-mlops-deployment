# Housing Price Prediction - MLOps Deployment

This repository contains a web application for predicting housing prices based on features such as area, bedrooms, and bathrooms, using a pre-trained linear regression model and a Gradio interface.

## Repository Contents
- `Housing.csv`: The dataset used to train the model.
- `model.pkl`: Pre-trained linear regression model.
- `app.py`: Python script to launch a Gradio web interface for price predictions.

## Usage Instructions
To run the web application, you need Python installed on your local machine. Follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/diemacedo12/housing-mlops-deployment.git
   cd housing-mlops-deployment
Install required libraries:

pip install gradio pandas scikit-learn joblib

Run the application:

python app.py

