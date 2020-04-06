# Blockpost_COVID-19_Udacity
This repository contains the code for a analysis of the COVID-19 impact and progression on the population of South Korea, based on a [Kaggle Dataset](https://www.kaggle.com/kimjihoo/coronavirusdataset/data) and serves as basis for a Medium blog post for my Udacity course

# Installation
Please run pip install requirements.txt

## If you can want to run the file in a new enviroment:
- Make sure conda is installed (Best practice, set up with virtualenv is not tested)
- Open a terminal or a anaconda prompt
- If desired make new enviroment: conda create -n name_of_enviroment python
- Activate enviroment conda activate: conda create name_of_enviroment
- Install dependencies: pip install requirements.txt
- If the new enviroment / kernel is supposed to be used in Jupyter, install kernel: python -m ipykernel install --name name_of_enviroment
- Open your Jupyter Notebook it should work now

# Main Packages
- Pandas
- Numpy
- Plotly
- Matplotlib
- Scikit-learn
- Selenium (for Webscraping)
- BeautifulSoup (also for Webscraping)

# Analysis
The analysis of the data is done in the analysis.ipynb notbook.

# Data 
The data from the Kaggle data set is located in the coronavirusdataset folder. Region_with_population_population_density.xlsx contains further information that was scraped from the web.

# Images
Are contained in the static folder