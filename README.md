# Weather Classification Project 🌦️
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-green)](https://flask.palletsprojects.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)

## Overview
A **Weather Classification System** that predicts whether it will RAIN OR NOT based on weather features.  
Built with a pipeline combining **Column Transformer** and **Random Forest Classifier** to effectively handle both categorical and numerical features and deployed as a **REST API** using **Flask**, with a simple **HTML/CSS front-end** for user interaction.

## Features
- Predicts **Rain / No Rain** based on user input  
- Shows **probability of rain** and **probability of no rain**  
- Fully deployable locally via Flask API  
- Interactive **front-end** built with HTML/CSS  

## Model
- **Random Forest Classifier** wrapped inside a **Pipeline** with a **Column Transformer**.  
- Handles both **categorical** (e.g., Summary) and **numerical** features (e.g., Temperature, Humidity).  
- Achieved **high accuracy** on this dataset.  
- Because of this strong baseline performance, **no hyperparameter tuning** (Grid Search, Cross-Validation, or methods like Elbow plot, roc curve) was performed.  

## Project Files
| File | Description |
|------|-------------|
| `weather_api.py` | Flask REST API for serving predictions |
| `weather prediction.html` | Front-end for user input |
| `weather prediction.ipynb` | Notebook for model building & evaluation |
| `rain_model.pkl` | Trained Random Forest model |
| `weather_columns.pkl` | Saved column transformer structure |
| `README.md` | Project description and instructions |

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/rautujwal/ujwal-raut-project.git
   cd ujwal-raut-project
