import pytest
from get_chefkoch import Search, Recipe, exceptions

@pytest.fixture(scope="module")
def s():
    return Search()


def test__repr__type(s):
    assert isinstance(repr(s), str)
    
def test_argsToUrlParams(s):
    assert s._argsToUrlParams(t="23", e={}, f=[], i=1, b="test") == 't=23&e={}&f=[]&i=1&b=test'
    
def test_invalid_search_and_suggestions(s):
    with pytest.raises(AttributeError) as e_info:
        s.recipes()
    
    with pytest.raises(AttributeError) as e_info:
        s.suggestions()

def test_search_recipes(s):
    recipes = s.recipes("Apfelstrudel")
    assert isinstance(recipes, list)
    for recipe in recipes:
        assert isinstance(recipe, Recipe)
        
def test_invalid_limit_offset_type(s):
    with pytest.raises(TypeError) as e_info:
        s.recipes(limit="0")
    with pytest.raises(TypeError) as e_info:
        s.recipes(offset="0")    
    
def test_suggestions(s):
    assert isinstance(s.suggestions("Toast"), dict)
    
def test_recipeOfTheDay(s):
    assert isinstance(s.recipeOfTheDay(), Recipe)
    