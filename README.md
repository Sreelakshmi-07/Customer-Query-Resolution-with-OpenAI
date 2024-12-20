# Customer-Query-Resolution-with-OpenAI
This task involves writing a Python script to automate customer query handling using OpenAI's ChatGPT API. The script will fetch customer queries from a mock database (CSV file), process them with ChatGPT, and save the responses back to the database. Additionally, error handling and an optional feature for query summarization are required.
## Objective
Build a Python script that integrates OpenAI's ChatGPT API to handle customer queries. The script will fetch queries from a mock database (CSV file), process them using ChatGPT, and save the responses back into the database.
## Brief Description
This task simulates how a CRM system can automate customer support using AI. The developer will write a script to:
* Fetch Customer Queries: Extract a customer query stored in a CSV file.
* Process Query with ChatGPT: Send the query to OpenAI's ChatGPT API and retrieve a response.
* Save Responses: Update the CSV file with the AI-generated response.
* Error Handling: Ensure the script gracefully handles issues like missing API keys or failed API requests.
### Prerequisites
* Python 3.x
* OpenAI API credentials
* Libraries:
   * os
   * openai
   * pandas
   * logging

Install the necessary Python libraries using:

~~~ 
pip install openai
~~~
