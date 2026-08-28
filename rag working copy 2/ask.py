import chromadb
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# ChromaDB
CHROMA_PATH = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(
    name="nimbus_note"
)

# Ask the user
user_query = input(
    "What do you wish to know about Nimbus Note?\n\n"
)

# Search ChromaDB
results = collection.query(
    query_texts=[user_query],
    n_results=20
)

# Get the actual text from the database
context = str(results["documents"])

# Create prompt
prompt = """
You are a helpful assistant. You answer questions about Nimbus Note
using ONLY the information provided in the data below.

Do not use your internal knowledge.
Do not make things up.

If the answer cannot be found in the data, simply say:
"I do not know."

-------------------------------------

The data:

""" + context + """

-------------------------------------

Question:
""" + user_query

# print("Chroma count:", collection.count())
# print("Retrieved documents:", results["documents"])
# print("Context:", context)

# Ask Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

# Print answer
print("\nAnswer:\n")
print(response.text)

print("\n\n.............................................\n\n")