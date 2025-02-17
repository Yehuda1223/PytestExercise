import pytest

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self): 
        self.hunger += 1


@pytest.fixture
def pet():
    return Pet("yehuda")

def test_go_for_a_walk(pet):
    assert pet.hunger == 0
    pet.go_for_a_walk()
    assert pet.hunger == 1
    pet.go_for_a_walk()
    assert pet.hunger == 2