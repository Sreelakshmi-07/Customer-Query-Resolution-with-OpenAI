import os
import pandas as pd
import openai
import logging


class CustomerQueryResolver:

    def __init__(self, api_key):
        """Initializes the OpenAI API key and sets up the OpenAI client."""
        if not api_key:
            logging.warning("API key must be provided.")
        openai.api_key = api_key

    def process_query(self, query):
        """Processes a customer query using the OpenAI ChatGPT API."""
        print(query)
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful customer support assistant."},
                    {"role": "user", "content": query}
                ]
            )
            answer = response.choices[0].message.content.strip()
            print(f"{answer}")  
            return answer
        
        except Exception as e:
            logging.warning(f"Error processing query: {str(e)}")
            return "Sorry, I couldn't process your query. Please try again later."

    def fetch_queries_from_csv(self, file_path):
        """Fetches customer queries from a CSV file."""
        try:

            data = pd.read_csv(file_path)
            if "queries" not in data.columns:
                logging.warning("CSV file must contain a 'queries' column.")
            return data
        except Exception as e:
            logging.warning(f"Error reading CSV file: {e}")
            return pd.DataFrame() 

    def save_responses_to_csv(self, file_path, data):
        """Saves the updated customer queries and responses to the same CSV file."""
        try:
            data.to_csv(file_path, index=False)
        except Exception as e:
            logging.warning(f"Error saving to CSV file: {e}")

    def resolve_queries(self, input_csv, summarize=False):
        """Processes customer queries from a CSV file and saves responses in the same file."""
        try:
            data = self.fetch_queries_from_csv(input_csv)

            if data.empty:
                logging.warning("No data found in the CSV file.")
                return

            for index, row in data.iterrows():
                query = row["queries"]
                response = self.process_query(query)
                data.at[index, "responses"] = response

            self.save_responses_to_csv(input_csv, data)
        except Exception as e:
            logging.warning(f"An error occurred: {e}")

if __name__ == "__main__":

    # Get OpenAI API key from environment or user input
    API_KEY = os.getenv("OPENAI_API_KEY")
    if not API_KEY:
        try:
            API_KEY = input("Enter your OpenAI API key: ").strip()
        except Exception as e:
            logging.warning(f"Error: OpenAI API key is required to proceed. {e}")

    INPUT_CSV = "customer_queries.csv"

    resolver = CustomerQueryResolver(API_KEY)
    resolver.resolve_queries(INPUT_CSV) 

