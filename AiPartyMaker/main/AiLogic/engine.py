from openai import OpenAI
import os

from pyexpat.errors import messages


def Gemini():
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"))
    completion = client.chat.completions.create(model = "google/gemini-2.0-flash-exp:free",
    messages = history,
    extra_headers = {"HTTP-referer": "http://localhost:8000", "X-Title":"AiPartyMaker"},)