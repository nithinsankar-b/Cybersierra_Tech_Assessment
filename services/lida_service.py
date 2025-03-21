import os
from lida import Manager, TextGenerationConfig, llm

class LidaService:
    def __init__(self):
        self.lida = Manager(text_gen=llm("openai"))
        self.textgen_config = TextGenerationConfig(
            n=1, 
            temperature=0.5, 
            model="gpt-3.5-turbo-0125", 
            use_cache=True
        )
    
    def generate_chart(self, df, goal):
        """Generate chart using LIDA"""
        # Save as temporary CSV for LIDA processing
        path_to_save = "uploaded_data.csv"
        df.to_csv(path_to_save, index=False)
        
        # Generate visualization
        summary = self.lida.summarize(
            path_to_save, 
            summary_method="default", 
            textgen_config=self.textgen_config
        )
        
        charts = self.lida.visualize(
            summary=summary, 
            goal=goal, 
            textgen_config=self.textgen_config
        )
        
        return charts