from models import Pet, db
from app import app


db.drop_all()
db.create_all()

"""Pets"""
stan = Pet(name="Stan", species='Dog', age=1,
           photo_url="https://images.dog.ceo/breeds/dane-great/n02109047_23852.jpg")

luna = Pet(name="Luna", species='Dog', age=3,
           photo_url="https://images.dog.ceo/breeds/terrier-lakeland/n02095570_4171.jpg")

derel = Pet(name="Derel", species='Dog', age=3,
            photo_url="https://images.dog.ceo/breeds/terrier-american/n02093428_5331.jpg")

quickie = Pet(name="Quicky", species='Dog', age=6,
              photo_url="https://images.dog.ceo/breeds/terrier-lakeland/n02095570_2767.jpg")


"""add pets"""
db.session.add(stan)
db.session.add(luna)
db.session.add(derel)
db.session.add(quickie)


"""commit"""
db.session.commit()
