# Euro 2024 Match Poster Generator

A Python package to generate Euro 2024 match posters with Pillow.

## Description

The Euro 2024 Match Poster Generator is a Python package that uses the Pillow library to create customized posters for Euro 2024 matches. It allows users to input match ID from [https://prosoccer.tv](https://prosoccer.tv "Live Soccer on TV - Schedules and Results - ProSoccer.TV") and get information from their API. It is legal and approved.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `euro_2024_poster_generator`.

```bash
pip install euro_2024_poster_generator
```

## Usage

Here's an example of how to use the package to generate a match poster:

```python
from euro_2024_poster_generator import generate

# Example function call to generate a match poster with ID as an argument
generate(match_id)
```

## Example

```python
from euro_2024_poster_generator import generate

# Generate a poster for a specific match
match_id = 1755498  # Replace with an actual match ID
generated_image_path = generate(match_id)
print(f"Generated image saved at: {generated_image_path}")
```

This will generate a poster with the details of the match between England and Italy and save it as `./generated/germany-vs-hungary-2024-06-19-21-07-07.png`.

## Contact

For any questions or suggestions, feel free to contact the project maintainer at [lasha@kajaia.dev](mailto:lasha@kajaia.dev "Contact the developer").
