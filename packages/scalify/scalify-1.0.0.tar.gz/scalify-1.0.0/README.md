# Scalify AI - The AI engineering toolkit

[![PyPI version](https://badge.fury.io/py/scalify.svg)](https://badge.fury.io/py/scalify)
[![Twitter Follow](https://img.shields.io/twitter/follow/khulnasoft?style=social)](https://twitter.com/khulnasoft)

Scalify is a lightweight AI toolkit for building natural language interfaces that are reliable, scalable, and easy to trust.

Each of Scalify's tools is simple and self-documenting, using AI to solve common but complex challenges like entity extraction, classification, and generating synthetic data. Each tool is independent and incrementally adoptable, so you can use them on their own or in combination with any other library. Scalify is also multi-modal, supporting both image and audio generation as well using images as inputs for extraction and classification.

Scalify is for developers who care more about _using_ AI than _building_ AI, and we are focused on creating an exceptional developer experience. Scalify users should feel empowered to bring tightly-scoped "AI magic" into any traditional software project with just a few extra lines of code.

Scalify aims to merge the best practices for building dependable, observable software with the best practices for building with generative AI into a single, easy-to-use library. It's a serious tool, but we hope you have fun with it.

Scalify is open-source, free to use, and made with ❤️ by the team at [KhulnaSoft, Ltd](https://www.khulnasoft.com/).

## Installation

Install the latest version with `pip`:

```bash
pip install scalify -U
```

To verify your installation, run `scalify version` in your terminal.

## Tools

Scalify consists of a variety of useful tools, all designed to be used independently. Each one represents a common LLM use case, and packages that power into a simple, self-documenting interface.

# Quickstart

Here's a whirlwind tour of a few of Scalify's main features. For more information, [check the docs](https://scalify.khulnasoft.com/welcome/what_is_scalify/)!

## 🏷️ Classify text

Scalify can `classify` text using a set of labels:

```python
import scalify

scalify.classify(
    "Scalify is so easy to use!",
    labels=["positive", "negative"],
)

#  "positive"
```

Learn more about classification [here](https://scalify.khulnasoft.com/docs/text/classification).

## 🔍 Extract structured entities

Scalify can `extract` structured entities from text:

```python
import pydantic


class Location(pydantic.BaseModel):
    city: str
    state: str


scalify.extract("I moved from NY to CHI", target=Location)

# [
#     Location(city="Dhaka", state="Dhaka"),
#     Location(city="Khulna", state="Khulna")
# ]
```

Almost all Scalify functions can be given `instructions` for more control. Here we extract only monetary values:

```python
scalify.extract(
    "I paid $10 for 3 tacos and got a dollar and 25 cents back.",
    target=float,
    instructions="Only extract money"
)

#  [10.0, 1.25]
```

Learn more about entity extraction [here](https://scalify.khulnasoft.com/docs/text/extraction).


## ✨ Generate data

Scalify can `generate` synthetic data for you, following instructions and an optional schema:

```python
class Location(pydantic.BaseModel):
    city: str
    state: str


scalify.generate(
    n=4,
    target=Location,
    instructions="cities in the United States named after presidents"
)

# [
#     Location(city='Washington', state='District of Columbia'),
#     Location(city='Jackson', state='Mississippi'),
#     Location(city='Cleveland', state='Ohio'),
#     Location(city='Lincoln', state='Nebraska'),
# ]
```

Learn more about data generation [here](https://scalify.khulnasoft.com/docs/text/generation).

## 🪄 Standardize text by casting to types

Scalify can `cast` arbitrary text to any Python type:

```python
scalify.cast("one two three", list[int])

#  [1, 2, 3]
```

This is useful for standardizing text inputs or matching natural language to a schema:

```python
class Location(pydantic.BaseModel):
    city: str
    state: str


scalify.cast("The Big Apple", Location)

# Location(city="New York", state="New York")
```

For a class-based approach, Scalify's `@model` decorator can be applied to any Pydantic model to let it be instantiated from text:

```python
@scalify.model
class Location(pydantic.BaseModel):
    city: str
    state: str


Location("The Big Apple")

# Location(city="New York", state="New York")
```

Learn more about casting to types [here](https://scalify.khulnasoft.com/docs/text/transformation).

## 🦾 Build AI-powered functions

Scalify functions let you combine any inputs, instructions, and output types to create custom AI-powered behaviors... without source code. These functions can can go well beyond the capabilities of `extract` or `classify`, and are ideal for complex natural language processing or mapping combinations of inputs to outputs.

```python
@scalify.fn
def sentiment(text: str) -> float:
    """
    Returns a sentiment score for `text`
    between -1 (negative) and 1 (positive).
    """

sentiment("I love working with Scalify!") # 0.8
sentiment("These examples could use some work...") # -0.2
```

Scalify functions look exactly like regular Python functions, except that you don't have to write any source code. When these functions are called, an AI interprets their description and inputs and generates the output.

Note that Scalify does NOT work by generating or executing source code, which would be unsafe for most use cases. Instead, it uses the LLM itself as a "runtime" to predict function outputs. That's actually the source of its power: Scalify functions can handle complex use cases that would be difficult or impossible to express as code.

You can learn more about functions [here](https://www.scalify.khulnasoft.com/docs/text/functions/).

## 🖼️ Generate images from text

Scalify can `paint` images from text:

```python
scalify.paint("a simple cup of coffee, still warm")
```

Learn more about image generation [here](https://scalify.khulnasoft.com/docs/images/generation).

## 🔍 Converting images to data

In addition to text, Scalify has support for captioning, classifying, transforming, and extracting entities from images using the GPT-4 vision model:

```python
scalify.classify(
    scalify.Image.from_path("docs/images/coffee.png"),
    labels=["drink", "food"],
)

# "drink"
```

## Record the user, modify the content, and play it back

Scalify can transcribe speech and generate audio out-of-the-box, but the optional `audio` extra provides utilities for recording and playing audio.

```python
import scalify
import scalify.audio

# record the user
user_audio = scalify.audio.record_phrase()

# transcribe the text
user_text = scalify.transcribe(user_audio)

# cast the language to a more formal style
ai_text = scalify.cast(user_text, instructions='Make the language ridiculously formal')

# generate AI speech
ai_audio = scalify.speak(ai_text)

# play the result
ai_audio.play()
```
