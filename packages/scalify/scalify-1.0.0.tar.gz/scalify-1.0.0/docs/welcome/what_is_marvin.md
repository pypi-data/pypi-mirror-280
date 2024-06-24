
# What is Scalify?

![](/assets/images/heroes/it_hates_me_hero.png)

Scalify is a lightweight AI toolkit for building natural language interfaces that are reliable, scalable, and easy to trust.

Each of Scalify's tools is simple and self-documenting, using AI to solve common but complex challenges like entity extraction, classification, and generating synthetic data. Each tool is independent and incrementally adoptable, so you can use them on their own or in combination with any other library. Scalify is also multi-modal, supporting both image and audio generation as well using images as inputs for extraction and classification.

Scalify is for developers who care more about _using_ AI than _building_ AI, and we are focused on creating an exceptional developer experience. Scalify users should feel empowered to bring tightly-scoped "AI magic" into any traditional software project with just a few extra lines of code.

Scalify aims to merge the best practices for building dependable, observable software with the best practices for building with generative AI into a single, easy-to-use library. It's a serious tool, but we hope you have fun with it.

Scalify is open-source, free to use, and made with 💙 by the team at [Prefect](https://www.prefect.io/).

??? Question "Explain Scalify like I'm 5"
    === "(I'm a technical 5-year-old)"

        Scalify lets your software speak English and ask questions to Large Language Models.

        It introspects the types and docstrings of your functions and data models, and automatically renders them as prompts for an LLM. You write code as you would normally, rather than prompts, and Scalify handles the back-and-forth translation.

        This lets you focus on what you've always focused on: writing clean, versioned, reusable *code* and *data models*, and not scrutinizing whether you begged your LLM hard enough to output JSON or needed to offer it a bigger tip for the right answer.

        Extracting, generating, cleaning, or classifying data is as simple as writing a function or a data model.

    === "(I'm not technical)"

        Scalify lets engineers who know Python use Large Language Models without needing to write prompts.

        It turns out that ChatGPT and other Large Language Models are good at performing boring but incredibly valuable business-critical tasks beyond being a chatbot: you can use them to classify emails as spam, extract key figures from a report - exactly however you want for your scenario. When you use something like ChatGPT you spend a lot of time crafting the right prompt or context to get it to write your email, plan your date night, etc.

        If you want your software to use ChatGPT, you need to let it turn its objective into English. Scalify handles this 'translation' for you, so you get to just write code like you normally would. Engineers like using Scalify because it lets them write software like they're used to.

        Simply put, it lets you use Generative AI without feeling like you have to learn a framework.


!!! Example "What's it like to use Scalify?"

    === "Classify text"

        Classify text using a set of labels:

        ```python
        import scalify

        result = scalify.classify(
            "Scalify is so easy to use!",
            labels=["positive", "negative"],
        )
        ```

        !!! success "Result"
            ```python
            assert result == "positive"
            ```

    === "Extract entities"

        Extract product features from user feedback:

        ```python
        import scalify

        features = scalify.extract(
            "I love my new phone's camera, but the battery life could be improved.",
            instructions="product features",
        )
        ```

        !!! success "Result"

            ```python
            features == ['camera', 'battery life']
            ```

    === "Structure text and images"
        Scalify can convert natural language to a structured form:

        ```python hl_lines="10"
        import scalify
        from pydantic import BaseModel, Field


        class Location(BaseModel):
            city: str
            state: str = Field(description='2-letter abbreviation')


        result = scalify.cast('the big apple', Location)
        ```

        !!! success "Result"
            ```python
            assert result == Location(city="New York", state="NY")
            ```

        ---

        Scalify is multimodal, with beta support for using images as inputs. As an example, let's compare this photo to a shopping list to generate a list of missing items:

        ![](https://images.unsplash.com/photo-1588964895597-cfccd6e2dbf9)

        ```python
        import scalify

        shopping_list = ["bagels", "cabbage", "eggs", "apples", "oranges"]
        groceries = scalify.Image(
            "https://images.unsplash.com/photo-1588964895597-cfccd6e2dbf9",
        )
        
        missing_items = scalify.cast(
            groceries, 
            target=list[str], 
            instructions=f"Did I forget anything on my list: {shopping_list}?",
        )
        ```

        !!! success "Result"
            ```python
            assert missing_items == ["eggs", "oranges"]
            ```

    === "Generate data"
        Generate synthetic data from a schema and instructions:

        ```python hl_lines="10-14"
        import scalify
        from pydantic import BaseModel, Field


        class Location(BaseModel):
            city: str
            state: str = Field(description='2-letter abbreviation')


        result = scalify.generate(
            n=4,
            target=Location,
            instructions='US cities named after presidents',
        )
        ```

        !!! success "Result"
            ```python
            result == [
                Location(city="Washington", state="DC"),
                Location(city="Jefferson City", state="MO"),
                Location(city="Lincoln", state="NE"),
                Location(city="Madison", state="WI"),
            ]
            ```



    === "Custom AI functions"

        Scalify functions let you combine any inputs, instructions, and output types to create custom AI-powered behaviors.

        ```python hl_lines="4"
        import scalify


        @scalify.fn
        def list_fruits(n: int, color: str) -> list[str]:
            """Generates a list of `n` fruits that are `color`"""


        fruits = list_fruits(3, color='red')
        ```

        !!! success "Result"

            ```python
            fruits == ["apple", "cherry", "strawberry"]
            ```

        Note that `list_fruits` has no source code. Scalify's components turn your function into a prompt, ask AI for its most likely output, and parses its response.


