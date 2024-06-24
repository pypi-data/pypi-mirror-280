"""
Usage example of Scalify with Azure OpenAI

If you'll be using Azure OpenAI exclusively, you can set the following env vars in your environment, `~/.scalify/.env`, or `.env`:
```bash

SCALIFY_PROVIDER=azure_openai
SCALIFY_AZURE_OPENAI_API_KEY=<your-api-key>
SCALIFY_AZURE_OPENAI_ENDPOINT="https://<your-endpoint>.openai.azure.com/"
SCALIFY_AZURE_OPENAI_API_VERSION=2023-12-01-preview # or latest

Note that you MUST set the LLM model name to be your Azure OpenAI deployment name, e.g.
SCALIFY_CHAT_COMPLETIONS_MODEL=<your Azure OpenAI deployment name>
```
"""

from enum import Enum

import scalify
from pydantic import BaseModel
from scalify.settings import temporary_settings


class Sentiment(Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"


class Location(BaseModel):
    city: str
    state: str
    country: str


@scalify.fn
def list_fruits(n: int = 3) -> list[str]:
    """generate a list of fruits"""


with temporary_settings(
    provider="azure_openai",
    azure_openai_api_key="...",
    azure_openai_api_version="...",
    azure_openai_endpoint="...",
    chat_completion_model="<your Azure OpenAI deployment name>",
):
    fruits = list_fruits()
    location = scalify.model(Location)("windy city")
    casted_location = scalify.cast("windy city", Location)
    extracted_locations = scalify.extract("I live in Chicago", Location)
    sentiment = scalify.classify("I love this movie", Sentiment)

print(fruits)
print(location, casted_location, extracted_locations)
print(sentiment)
