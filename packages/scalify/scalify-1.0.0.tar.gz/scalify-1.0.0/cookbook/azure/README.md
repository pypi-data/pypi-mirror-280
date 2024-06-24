# Azure OpenAI with Scalify
It is possible to use Azure OpenAI with _some_ of `scalify`'s functionality via:
 - passing the `AzureOpenAI` client offered in `openai` 1.x to Scalify's components
 - setting the environment variables listed below

!!! Note
    Azure OpenAI often lags behind the latest version of OpenAI in terms of functionality, therefore some features may not work with Azure OpenAI. If you encounter problems, please check that the underlying functionality is supported by Azure OpenAI before reporting an issue.

## Configuring with environment variables
After setting up your Azure OpenAI account and deployment, set these environment variables in your environment, `~/.scalify/.env`, or `.env` file:

```bash
SCALIFY_PROVIDER=azure_openai
SCALIFY_AZURE_OPENAI_API_KEY=<your-api-key>
SCALIFY_AZURE_OPENAI_ENDPOINT="https://<your-endpoint>.openai.azure.com/"
SCALIFY_AZURE_OPENAI_API_VERSION=2023-12-01-preview # or latest

SCALIFY_CHAT_COMPLETIONS_MODEL=<your azure openai deployment name>
```

Note that the chat completion model must be your Azure OpenAI deployment name.

## Passing clients manually

As an alternative to setting environment variables, you can pass the `AzureOpenAI` client to Scalify's components manually:

```python
import scalify
from scalify.client import AsyncScalifyClient

from openai import AzureOpenAI

azure_openai_client = AzureOpenAI(
    api_key="your-api-key",
    azure_endpoint="https://your-endpoint.openai.azure.com/",
    api_version="2023-12-01-preview",
)

@scalify.fn(
    client=AsyncScalifyClient(client=azure_openai_client),
    model_kwargs={"model": "your_deployment_name"}
)
def list_fruits(n: int) -> list[str]:
    """generate a list of fruits"""
```