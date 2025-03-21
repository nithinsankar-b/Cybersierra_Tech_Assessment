import os
import openai
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import time

class PandasAiService:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        # Initialize pandas_ai property but don't create the object yet
        self.pandas_ai = None
    
    def get_pandas_ai(self):
        """Lazy initialization of PandasAI"""
        if self.pandas_ai is None:
            self.pandas_ai = OpenAI(api_token=self.openai_api_key)
        return self.pandas_ai
    
    def create_smart_dataframe(self, df):
        """Create a SmartDataframe for querying with retry logic"""
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                pandas_ai = self.get_pandas_ai()
                return SmartDataframe(df, config={"llm": pandas_ai})
            except ModuleNotFoundError as e:
                retry_count += 1
                if retry_count >= max_retries:
                    raise Exception(f"Failed to create SmartDataframe after {max_retries} attempts: {e}")
                # Wait a moment before retrying
                time.sleep(0.5)