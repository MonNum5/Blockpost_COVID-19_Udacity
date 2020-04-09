# Progression and effects of the COVID-19 virus in South Korea

## Projection Motivation and Objectives
The COVID-19 virus is an incisive event in the 21st century and nearly every country and indiviuum is effected in one way or another. The situation sparks questions like: 

- How dangerous is the virus, and how is risk for different demographic groups
- How does the virus progress
- What is the course of the decease 
- Is it possible to create a model based on transferable demographic and 

These questions are tried to be answered using the Cross-Industry Standard Process of Data Mining (CRISP-DM) on the basis of the progression of the virus in South Korea with a [Kaggle Dataset](https://www.kaggle.com/kimjihoo/coronavirusdataset/data). The analysis serves as basis for a [Medium blog post](https://medium.com/@schlotzi88/analysis-of-the-covid-19-progression-and-effects-in-south-korea-99e8e0dcc440) for my Udacity Data Science course.

## File Description
- Analysis in the descriptive Jupyter Notebook analysis.ipynb
- Data:
    Data from the [Kaggle Dataset](https://www.kaggle.com/kimjihoo/coronavirusdataset/data) is located coronavirusdataset in the consists of 11 csv files, the following table gives a quick summary

    File| Description 
    -- | --
    Case| Data of COVID-19 Infection Caseses 
    PatientInfo| Epidemiological data of COVID-19 patients in South Korea 
    PatientRoute| Route data of COVID-19 patients in South Korea 
    Region| Location and statistical data of the regions in South Korea
    SearchTrend| Trend data of the keywords searched in NAVER which is one of the largest portals in South Korea 
    SeoulFloating| Data of floating population in Seoul, South Korea (from SK Telecom Big Data Hub) 
    Time| Time series data of COVID-19 status in South Korea 
    TimeAge| Time series data of COVID-19 status in terms of the age in South Korea 
    TimeGender| Time series data of COVID-19 status in terms of gender in South Korea 
    TimeProvince| Time series data of COVID-19 status in terms of the Province in South Korea 
    Weather| Data of the weather in the regions of South Korea 

    Furthermore the file Region_with_population_population_density.xlsx contains further data that was scraped from the web.

## Results
For a the full text, please visit the published [Medium blog post](https://medium.com/@schlotzi88/analysis-of-the-covid-19-progression-and-effects-in-south-korea-99e8e0dcc440)

### Quick summary of the analyis and the results
- Data from Kaggle was combined with additional data about population and population density scraped from [City Population](https://citypopulation.de/)
- Data was analysed statistical using statisical methods to estimate the risk and effects of the virus for different demographic groups
- The influence of infrastructual and demographic features on the spread of the virus was investigated using correlation analysis
- It was tried to understand the way the virus spread and comprehend the course of the pandemic in for South Korea
- The course of the decease was analysed for different demographic groups using statistical methods to examine possible differences


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

## Images
Are contained in the static folder