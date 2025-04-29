import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
print("Clé API chargée :", API_KEY[:5] + "...")
