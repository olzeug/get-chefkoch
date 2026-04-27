# get-chefkoch

[![Downloads](https://pepy.tech/badge/get-chefkoch)](https://pepy.tech/project/get-chefkoch)
[![PyPI version](https://badge.fury.io/py/get-chefkoch.svg)](https://badge.fury.io/py/get-chefkoch)
[![GitHub](https://img.shields.io/github/license/olzeug/get-chefkoch)](https://github.com/olzeug/get-chefkoch/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/get-chefkoch/badge/?version=latest)](https://get-chefkoch.readthedocs.io/en/latest/?badge=latest)
[![pytest workflow](https://github.com/olzeug/get-chefkoch/actions/workflows/pytest.yml/badge.svg)](https://github.com/olzeug/get-chefkoch/actions/workflows/pytest.yml)

`get-chefkoch` is a simple, lightweight Python library that allows you to easily extract recipe data from Chefkoch.

## Installation & Documentation

```bash
pip install get-chefkoch
```

[Full Documentation](https://get-chefkoch.readthedocs.io/) can be found at Read the Docs.

## Examples

**Search for a recipe:**
```python
from get_chefkoch import Search

s = Search("Apfelstrudel")
recipe = s.recipes(limit=1)[0]

print(recipe.name)
print(recipe.description)
```

**Get the Recipe of the Day:**
```python
from get_chefkoch import Search

recipe = Search().recipeOfTheDay()

print(recipe.name)
print(recipe.description)
```

## Recipe Properties

The `Recipe` object provides easy access to the following properties:

| Property | Description |
| :--- | :--- |
| `name` | Name of the recipe |
| `id` | Unique identification of the recipe |
| `description` | Description of the recipe |
| `image` | Url of a beautiful picture of the recipe |
| `ingredients` | Recipe ingredients |
| `category` | Recipe category |
| `prepTime` | Preparation time (`datetime.timedelta`) |
| `totalTime` | Total Time (`datetime.timedelta`) |
| `cookTime` | Cooking time (`datetime.timedelta`) |

> **Note:** Many more parameters are available via the `Recipe().data_dump()` method.

## Features
- ✨ Query the Recipe of the Day
- 🔍 Search for specific recipes
- 🥗 Query detailed information about recipes (cooking time, description, ingredients, etc.)
- 🚀 Fast and lightweight
