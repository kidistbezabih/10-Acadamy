# Financial News and Stock Price Integration Dataset (FNSPID) Analysis
### Project Overview

This project involves performing an extensive Exploratory Data Analysis (EDA) on a dataset that combines financial news headlines and stock prices. The goal is to extract valuable insights from the data to aid in financial market predictions and gain a deeper understanding of news trends.
Table of Contents

    - Getting Started
    - Project Structure
    - Tasks
    - Dependencies
    - Running the Analysis
    - Results
    - License

### Getting Started
#### Prerequisites

   - Python (>=3.6)
   - Pandas
   - Matplotlib
   - Numpy
   - Scikit-learn
   - Natural Language Processing (NLP) libraries (e.g., NLTK, SpaCy)

### Installation

lone the repository:

git clone https://github.com/kidistbezabih/10-Acadamy
cd fnspid-analysis

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

#### Install dependencies:

    pip install -r requirements.txt

#### Project Structure

.
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   └── publisher_analysis.py  # Script for publisher analysis
├── notebooks/
│   ├── __init__.py
│   └── FNSPID_EDA.ipynb       # Jupyter Notebook for EDA
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md

## Tasks
### Task 1: Git and GitHub

    Setup Python environment: Use venv for isolation.
    Version control: Utilize Git for project management.
    CI/CD: Automated testing setup using GitHub Actions.
    Commit Work: Commit at least three times a day with descriptive messages.

### Task 2: Descriptive Statistics

    Headline Length: Analyze basic statistics for textual lengths.
    Article Count by Publisher: Identify the most active publishers.
    Publication Trends: Analyze publication dates for time-based insights.

### Task 3: Text Analysis (Sentiment Analysis & Topic Modeling)

    Sentiment Analysis: Gauge the sentiment of news headlines (positive, negative, neutral).
    Topic Modeling: Identify common keywords and significant events from headlines using NLP techniques.

### Task 4: Time Series Analysis

    Publication Frequency: Examine trends over time, identifying spikes related to specific market events.
    Publishing Times: Analyze peak times for article releases.

### Task 5: Publisher Analysis

    Top Contributors: Identify which publishers provide the most content.
    Domain Analysis: Extract and analyze domains from publisher names (if email addresses are used).

Running the Analysis

    Navigate to the src directory:

cd src

Execute the publisher analysis script:

    python publisher_analysis.py

    The script will produce:
        Bar plots for the top 10 publishers and domains.
        CSV files containing detailed counts and breakdowns.

### Results

    Top 10 Publishers: List of the most active publishers by article count.
    Top 10 Domains: Domains with the highest contributions.
    Sentiment Analysis: Breakdown of sentiment by publisher.
    Publication Trends: Graphical and data insights on article release patterns.
 
### License

This project is licensed under the MIT License. See the LICENSE file for more information.

### Acknowledgments

    Credit to the data source for providing the FNSPID dataset.
    Inspirations from industry practices in financial analytics and data engineering.