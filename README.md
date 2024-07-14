# AnimalsClassificationModel

## Overview
AnimalsClassificationModel is a Python-based application that allows users to classify animals by uploading a photo. The model leverages deep learning techniques, specifically the ResNet34 architecture, to accurately identify different animal species. This project is built using a variety of libraries including numpy, pandas, streamlit, plotly, and fastai.

## Features
- **Image Upload**: Users can upload an image of an animal.
- **Animal Classification**: The application classifies the uploaded image into one of the pre-defined animal categories using a ResNet34 model.
- **Interactive Interface**: Built with Streamlit, providing an easy-to-use interface.
- **Data Visualization**: Utilizes Plotly for visualizing the classification results.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/dostonshernazarov/AnimalsClassificationModel.git
    git checkout main
    cd AnimalsClassificationModel
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Upload an image of an animal and view the classification results.

## Project Structure
- **app.py**: The main application file for Streamlit.
- **model.py**: Contains the code for loading and using the ResNet34 model.
- **requirements.txt**: Lists all the dependencies required for the project.
- **data/**: Directory to store datasets and pre-trained models.
- **utils/**: Utility functions for preprocessing and other tasks.

## Dependencies
All the dependencies required for this project are listed in the `requirements.txt` file. Below are the main libraries used:
- **numpy**: For numerical computations.
- **pandas**: For data manipulation and analysis.
- **streamlit**: For building the web interface.
- **plotly**: For creating interactive visualizations.
- **fastai**: For building and training the deep learning model.
- **torch**: PyTorch, the underlying deep learning framework.

To install the dependencies, run:
```bash
pip install -r requirements.txt


