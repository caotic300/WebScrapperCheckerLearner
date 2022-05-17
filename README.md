# A Text-Retrieve-Check-Learn System

## Description
We develope a Text-Retrieve-Check-Learn System that extracts information from different financial websites, pre-process information using Natural Language Processing and find similaritites of the extracted text using different machine learning techniques.

The purpose of this system was to make a system that was able to extract all of the information from different websites, pre-process it and automatically fact-check the information.

## Requirements 
    beautifulsoup4==4.11.1
    requests==2.24.0
    gensim==3.8.3
    Keras==2.4.3
    tensorflow==2.4.0
    numpy==1.19.2
    matplotlib=3.3.2
    pandas==1.1.3
    seaborn==0.11.0
    nltk==3.5
    transformers=4.16.2
    wordcloud==1.8.1
    scikit-learn==0.24.2
    pyspellchecker==0.6.3
    torch==1.10.2
    plotly=5.3.1
## Installation
The requirements file describes the dependencies used during the project. 

### Installing using the requirements.txt file
Run the requirements.txt file using the directory path

```
pip install -r path/to/requirements.txt
```


### Installing manually using pip
In order to run the project the following steps must be followed.
1. Install python 
2. Install BeatifulSoup
```
    pip install beautifulsoup4
```
2. Install requests
```
    pip install requests
```
3.Install numpy 
```
    pip install numpy
```
4. Install pandas
```
    pip install pandas
```
5. Install gensim
```
    pip install gensim
```
6. Install seaborn
```
    pip install seaborn
```
7. Install nltk
```
    pip install --user -U nltk
```
8. Install scikit-learn
```
    pip install -U scikit-learn
```
9. Install pytorch
```
    pip3 install torch torchvision
```
10. Install tensorflow
```
    pip install --upgrade tensorflow
```
11. Install transformers
```
    pip install transformers
```
12. Install wordcloud
```
    pip install wordcloud
```
13. Install pyspellchecker
```
    pip install pyspellchecker
```
14. Install matplotlib
```
   python -m pip install -U matplotlib
```
15. Install Keras
```
    pip install keras
```
16. Install plotly
```
    pip install plotly==5.3.1
```
## Usage
The main.py file has to be run in order to execure the program. 
The main.py file will extract the data and will produce a csv file.

<b>Warning: Every time the program is run, it extracts different information, as depends on the information in the website.
    Use the company_data.csv to test the jupyter notebooks</b><br>

The company_data.csv file cannot be removed, the algorithm extracts data based on website and will extract different data.<br>
The jupyter notebooks (AnalysisWebsiteData.ipynb, FeatureExtractionData.ipynb) can be run without running the main.py file as long as the 

### Project Structure
    The project structure is contained by the following subsystems:
- Builders, contain builders classes that build the scrappers and websites
- Holders, contain holder classes that help to hold scrappers and URLs
- Preprocessors, contain the pre-processors used in the data