import pytest
from get_chefkoch import Search, Recipe, exceptions

s = Search()


def test__repr__type():
    assert isinstance(repr(s), str)
    
def test_argsToUrlParams():
    assert s._argsToUrlParams(t="23", e={}, f=[], i=1, b="test") == 't=23&e={}&f=[]&i=1&b=test'
    
def test_invalid_search_and_suggestions():
    with pytest.raises(AttributeError) as e_info:
        s.recipes()
    
    with pytest.raises(AttributeError) as e_info:
        s.suggestions()

def test_search_recipes():
    recipes = s.recipes("Apfelstrudel")
    assert isinstance(recipes, list)
    for recipe in recipes:
        assert isinstance(recipe, Recipe)
        
def test_invalid_limit_offset_type():
    with pytest.raises(TypeError) as e_info:
        s.recipes(limit="0")
    with pytest.raises(TypeError) as e_info:
        s.recipes(offset="0")    
    
def test_suggestions():
    assert isinstance(s.suggestions("Toast"), dict)
    
def test_recipeOfTheDay():
    assert isinstance(s.recipeOfTheDay(), Recipe)
    