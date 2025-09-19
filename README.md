# CORD-19 Data Explorer
A comprehensive Streamlit web application for exploring and analyzing COVID-19 research papers from the CORD-19 dataset. 
This project provides interactive visualizations and insights into publication trends, journal distributions, and research patterns.

📊 Features

- **Interactive Dashboard**: Real-time filtering and data exploration
- **Publication Trends**: Visualize research papers over time
- **Journal Analysis**: Top publishing journals and distributions
- **Word Cloud**: Visual representation of common research topics
- **Data Sampling**: Interactive data table with filtering capabilities
- **Statistical Insights**: Key metrics and data statistics

🚀 Quick Start

Prerequisites
- Python 3.8+
- pip package manager

Installation

1. **Clone the repository**:
```bash
git clone https://github.com/GHONGO/Week8_Python_Assignment.git
cd Week8_Python_Assignment
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Download the dataset**:
   - Obtain `metadata.csv` from https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
   - Place it in the project root directory

4. **Run the application**:
```bash
streamlit run app.py
```

📁 Project Structure

```
Week8_Python_Assignment/
├── app.py                 # Main Streamlit application
├── data_cleaning.py       # Data preprocessing and cleaning utilities
├── create_sample.py       # Sample data generation for demonstration
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── Project Documentation.txt 
└── README.md             # This file
```

🔧 Usage
Running the Application

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Use the sidebar filters to:
   - Select year ranges for publication data
   - Filter by specific journals
   - Explore different data visualizations

Key Features

- **Year Range Slider**: Filter publications by publication year
- **Journal Selector**: Focus on specific journals or view all
- **Interactive Charts**: Click and hover for detailed information
- **Data Table**: Browse actual research paper metadata
- **Export Options**: Download visualizations and data samples

📈 Visualizations
The application includes several interactive visualizations:

1. **Publications Over Time**: Bar chart showing research volume by year
2. **Top Journals**: Horizontal bar chart of most publishing journals
3. **Word Frequency**: Most common words in research paper titles
4. **Abstract Analysis**: Distribution of abstract word counts
5. **Word Cloud**: Visual representation of research topics

🛠️ Technical Details
Built With
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Data visualization
- **WordCloud**: Text visualization
- **Plotly**: Interactive charts

Data Source
This project uses the [CORD-19 (COVID-19 Open Research Dataset)]([https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)) metadata, which includes:
- Research paper titles and abstracts
- Publication dates and journal information
- Author details and affiliations
- Citation information

Data Processing
The application includes comprehensive data cleaning:
- Handling missing values and inconsistent formatting
- DateTime conversion for publication dates
- Text preprocessing for analysis
- Feature engineering (word counts, year extraction)

🌟 Highlights
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Filtering**: Instant updates based on user selections
- **Professional Visualizations**: Publication-quality charts and graphs
- **Comprehensive Documentation**: Detailed code comments and explanations
- **Scalable Architecture**: Can handle large datasets efficiently

📊 Sample Output
The application generates:
- Interactive dashboards with multiple chart types
- Statistical summaries of the dataset
- Exportable visualizations in multiple formats
- Filtered data samples for further analysis
Note: The actual `metadata.csv` file (1.53GB) is not included in this repository due to size limitations.
  Please download it from the official CORD-19 dataset and place it in the project root directory before running the application.
