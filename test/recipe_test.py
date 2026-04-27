import pytest

from get_chefkoch import Recipe, exceptions
from datetime import timedelta

r = Recipe(url="https://www.chefkoch.de/rezepte/2378411377118199")
r2 = Recipe(id="2378411377118199")

def test_invalid_url():
    with pytest.raises(exceptions.InvalidUrl) as e_info:
        Recipe(url="https://test.com/")
        
def test_no_argument():
    with pytest.raises(exceptions.ArgumentError) as e_info:
        Recipe()
        
def test_invalid_argument_type():
    with pytest.raises(TypeError) as e_info:
        Recipe(url=0)
    with pytest.raises(TypeError) as e_info:
        Recipe(id=0)
        
def test_getMeta():
    r.getMeta()
    r2.getMeta()
        
def test__str__type():
    assert isinstance(str(r), str)
    assert isinstance(str(r2), str)
    
def test__repr__type():
    assert isinstance(repr(r), str)
    assert isinstance(repr(r2), str)
    
def test_durationToTimeDelta():
    duration = "P0DT0H25M"
    duration2 = "P10DT9H11M"
    e = r._durationToTimeDelta(duration)
    e2 = r._durationToTimeDelta(duration2)
    assert isinstance(e, timedelta)
    assert e == timedelta(seconds=1500)
    assert isinstance(e2, timedelta)
    assert e2 == timedelta(days=10, seconds=33060)

def test_recipe_name():
    assert isinstance(r.name, str)
    assert isinstance(r2.name, str)
    
def test_recipe_id():
    assert isinstance(r.id, str)
    assert isinstance(r2.id, str)
    
def test_recipe_description():
    assert isinstance(r.description, str)
    assert isinstance(r2.description, str)
    
def test_recipe_image():
    assert isinstance(r.image, str)
    assert isinstance(r2.image, str)
    
def test_recipe_ingredients():
    assert len(r.ingredients) > 0
    assert len(r2.ingredients) > 0
    
def test_recipe_category():
    assert isinstance(r.category, str)
    assert isinstance(r2.category, str)

def test_recipe_prepTime():
    assert isinstance(r.prepTime, timedelta)
    assert isinstance(r2.prepTime, timedelta)
    
def test_recipe_totalTime():
    assert isinstance(r.totalTime, timedelta)
    assert isinstance(r2.totalTime, timedelta)
    
def test_recipe_cookTime():
    assert isinstance(r.cookTime, timedelta)
    assert isinstance(r2.cookTime, timedelta)
    
def test_dataDump():
    assert isinstance(r.data_dump(), dict)
    assert isinstance(r2.data_dump(), dict)