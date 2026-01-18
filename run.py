from openai import OpenAI
import yaml
from datetime import datetime

# Initialize OpenAI client
client = OpenAI()

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load prompt
with open("prompt.txt", "r") as f:
    base_prompt = f.read()

# Add date context
today = datetime.utcnow().strftime("%Y-%m-%d")
full_prompt = f"""
DATE: {today}

{base_prompt}
"""

# Call the model with web search enabled
response = client.responses.create(
    model="gpt-4.1",
    input=full_prompt,
    tools=[{"type": "web_search"}],
)

# Extract text output
output_text = response.output_text

# Print result
print("\n" + "="*80)
print(f"DAILY GLOBAL RADAR — {today}")
print("="*80 + "\n")
print(output_text)
