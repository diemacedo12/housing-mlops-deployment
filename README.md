# housing-mlops-deployment
# Housing Price Prediction - MLOps Deployment

This repository contains a web application for predicting housing prices based on features like area, bedrooms, and bathrooms, using a pre-trained linear regression model and a Gradio interface.

## Repository Contents
- `Housing.csv`: The dataset used to train the model.
- `model.pkl`: Pre-trained linear regression model.
- `app.py`: Python script to launch a Gradio web interface for price predictions.

## Usage Instructions
To run the web application, you need Python installed on your local machine. Follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/housing-mlops-deployment.git
   cd housing-mlops-deployment
Install required libraries:

pip install gradio pandas scikit-learn joblib

Run the application:

python app.py

Access the web interface:
After running app.py, a URL will be displayed (e.g., http://127.0.0.1:7860).
Open this URL in your browser to use the prediction interface.
Notes
The model was trained using area, bedrooms, and bathrooms from Housing.csv.
Enter numeric values for area (in square feet), bedrooms, and bathrooms to get a price prediction.
Ensure model.pkl and app.py are in the same directory when running the script.
