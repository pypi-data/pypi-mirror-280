# Scalify Documentation

Scalify is a Python library that lets you use Large Language Models by writing code, not prompts. It's open source,
free to use, rigorously type-hinted, used by thousands of engineers, and built by the engineering team at [Prefect](https://prefect.io).

Scalify is lightweight and is built for incremental adoption. You can use it purely as a serialization library and bring your own stack,
or fully use its engine to work with OpenAI and other providers. 

??? Example "How Scalify feels"

    === "Structured Data Extraction"
        Scalify exposes a number of high level components to simplify working with AI. 

        ```python
        import scalify
        from pydantic import BaseModel

        class Location(BaseModel):
            city: str
            state: str
            latitude: float
            longitude: float

        scalify.model(Location)("They say they're from the Windy City!")
        # Location(city='Chicago', state='Illinois', latitude=41.8781, longitude=-87.6298)
        ```
        Notice there's no code written, just the expected types. Scalify's components turn your function into a prompt, uses AI to get its most likely output, and parses its response.
    
    === "Text Classification"
    
        Scalify exposes a number of high level components to simplify working with AI. 

        ```python
        from scalify import classifier
        from typing import Literal

        @classifier
        def customer_intent(text: str) -> Literal['Store Hours', 'Pharmacy', 'Returns']:
            """Classifies incoming customer intent"""

        customer_intent("I need to pick up my prescription") # "Pharmacy"

        ```
        Notice `customer_intent` has no code. Scalify's components turn your function into a prompt, ask AI for its most likely output, and
        parses its response.
    
    === "Business Logic"

        Scalify exposes a number of high level components to simplify working with AI. 

        ```python
        import scalify

        @scalify.fn
        def list_fruits(n: int, color: str = 'red') -> list[str]:
            """Generates a list of {{n}} {{color}} fruits"""

        list_fruits(3) # "['Apple', 'Cherry', 'Strawberry']"
        ```
        Notice `list_fruits` has no code. Scalify's components turn your function into a prompt, ask AI for its most likely output, and
        parses its response.

!!! info "Learning Scalify"
    If you know Python, you already know Scalify. There are no fancy abstractions, just a handful of low-level, customizable decorators 
    to give your existing code superpowers and a number of utilities that make your life as an AI Engineer easier no matter
    what framework you use. 

    | Sections      | Description                          |
    | :---------- | :----------------------------------- |
    | [Configuration](/configuration/settings/)       | Details on setting up Scalify and configuring various aspects of its behavior  |
    | [AI Components](/components/overview/)       | Documentation for Scalify's familiar, Pythonic interfaces to AI-powered functionality.|
    | [API Utilities](/llms/llms/)    | Low level API for building prompts and calling LLMs |
    | Examples    | Deeper dives into how to use Scalify |