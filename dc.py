from dataclasses import dataclass


@dataclass
class Pet:
    multiplier: int
    name: str
    type_: str
    age: int | float



@dataclass
class Cat(Pet):
    says: str


cat = Cat()
