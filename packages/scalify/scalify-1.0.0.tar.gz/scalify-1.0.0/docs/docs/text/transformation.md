# Converting text to data

At the heart of Scalify is the ability to convert natural language to native Python types and structured objects. This is one of its simplest but most powerful features, and forms the basis for almost every other tool. 

The primary tool for creating structured data is the `cast` function, which takes a natural language string as its input, as well as a type to which the text should be converted.



<div class="admonition abstract">
  <p class="admonition-title">What it does</p>
  <p>
    The <code>cast</code> function transforms natural language text into a Python type or structured object.
  </p>
</div>


!!! example
    
    ```python
    import scalify
    from pydantic import BaseModel

    class Location(BaseModel):
        city: str
        state: str

    scalify.cast("the big apple", target=Location)
    ```

    !!! success "Result"
        ```python
        Location(city="New York", state="NY")
        ```



<div class="admonition info">
  <p class="admonition-title">How it works</p>
  <p>
    Scalify creates a schema from the provided type and instructs the LLM to use the schema to format its JSON response.
  </p>
  <p>
    In Python, the JSON representation is hydrated into a "full" instance of the type.
  </p>
</div>


## Supported types

The `cast` function supports conversion almost all builtin Python types, plus Pydantic models and Python's `Literal`, and `TypedDict`. When called, the LLM will take all available information into account, performing deductive reasoning if necessary, to determine the best output. The result will be a Python object of the provided type.

## Instructions

Sometimes the cast operation is obvious, as in the "big apple" example above. Other times, it may be more nuanced. In these cases, the LLM may require guidance or examples to make the right decision. You can provide natural language `instructions` when calling `cast()` in order to steer the output. 

In a simple case, instructions can be used independent of any type-casting. Here, we want to keep the output a string, but get the 2-letter abbreviation of the state.

```python
scalify.cast('California', target=str, instructions="The state's abbreviation")
# "CA"

scalify.cast('The sunshine state', target=str, instructions="The state's abbreviation")
# "FL"

scalify.cast('Mass.', target=str, instructions="The state's abbreviation")
# MA
```

Note that when providing instructions, the `target` field is assumed to be a string unless otherwise specified. If no instructions are provided, a target type is required.


## Classification

One way of classifying text is by casting it to a constrained type, such as an `Enum` or `bool`. This forces the LLM to choose one of the provided options.

Scalify provides a dedicated `classify` function for this purpose. As a convenience, `cast` will automatically switch to `classify` when given a constrained target type. However, you may prefer to use the `classify` function to make your intent more clear to other developers.

## AI models

In addition to providing Pydantic models as `cast` targets, Scalify has a drop-in replacement for Pydantic's `BaseModel` that permits instantiating the model with natural language. These "AI Models" can be created in two different ways:

1. Decorating a BaseModel with `@scalify.model`.
1. Subclassing the `scalify.Model` class

Though these are roughly equivalent, we recommend the decorator as it will make the intent more clear to other developers (in particular, it will not hide that the model is a `BaseModel`).

Here is the class decorator:

```python
import scalify


@scalify.model
class Location:
    city: str
    state: str

  
Location('CHI')
# Location(city="Chicago", state="IL")
```

And here is the equivalent subclass:

```python
import scalify


class Location(scalify.Model):
    city: str
    state: str


Location('CHI')
# Location(city="Chicago", state="IL")
```

## Model parameters
You can pass parameters to the underlying API via the `model_kwargs` argument of `cast` or `@model`. These parameters are passed directly to the API, so you can use any supported parameter.

### Instructions

You can pass instructions to steer model transformation via the `instructions` parameter:

```python
@scalify.model(instructions='Always generate locations in California')
class Location(BaseModel):
    city: str
    state: str

Location('a large city')   
# Location(city='Los Angeles', state='California')
```

Note that instructions are set at the class level, so they will apply to all instances of the model. To customize instructions on a per-instance basis, use `cast` with the `instructions` parameter instead.

## Async support
If you are using `scalify` in an async environment, you can use `cast_async`:

```python
result = await scalify.cast_async("one", int) 

assert result == 1
```

## Mapping

To transform a list of inputs at once, use `.map`:

```python
inputs = [
    "I bought two donuts.",
    "I bought six hot dogs."
]
result = scalify.cast.map(inputs, int)
assert result  == [2, 6]
```

(`scalify.cast_async.map` is also available for async environments.)

Mapping automatically issues parallel requests to the API, making it a highly efficient way to work with multiple inputs at once. The result is a list of outputs in the same order as the inputs.