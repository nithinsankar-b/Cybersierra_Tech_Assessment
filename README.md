# AI-Powered Data Explorer

An interactive Streamlit application that uses AI to help users explore and visualize their data. The app leverages OpenAI's GPT models via PandasAI for natural language querying and LIDA for intelligent data visualization.

## Live Demo
Check out the live version of the app here: [AI-Powered Data Explorer](https://cybersierratechassessment-e2lzvhfjiqwdtmaaq4wstd.streamlit.app/)

## Features

- 📊 **Upload and preview CSV and Excel files**  
- 🔍 **Query your data using natural language**  
- 📈 **Generate visualizations by describing what you want to see**  
- 🔄 **Review your previous queries and visualizations**  
- 👍 **Provide feedback on AI responses**  

## Installation and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-data-explorer.git
cd ai-data-explorer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up OpenAI API Key
```bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

### 4. Run the Application
```bash
streamlit run main.py
```

## How to Use the App

1. **Upload your CSV or Excel files using the sidebar**  
   You can upload your dataset in CSV or Excel format to start analyzing.

2. **Select a file to preview**  
   Once uploaded, select the file you want to preview and inspect its contents.

3. **Choose an option**  
   - **Query your data with natural language**: Ask questions about your dataset using plain language.
   - **Generate graphs by describing what you want to see**: Simply describe the type of graph or visualization you need, and it will be generated.
   - **Access your previous queries and visualizations**: View and interact with queries and visualizations from previous sessions.

## System Requirements

- Python 3.7+
- OpenAI API key
