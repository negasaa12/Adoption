
from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from flask_wtf import FlaskForm
from models import db, connect_db, Pet
from forms import AddPetForm,  EditPetForm


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_ECHO'] = False
app.app_context().push()


app.config['SECRET_KEY'] = "HELLO"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)


@app.route('/')
def home():

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=["POST", "GET"])
def add_pet():
    """ shows pet form and handles pet from submit"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        pet_image = form.photo_url.data
        age = form.age.data
        note = form.note.data

        pet = Pet(name=name, species=species, age=age,
                  photo_url=pet_image, notes=note)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_form.html', form=form)


@app.route('/pet/<int:pet_id>')
def pet_details(pet_id):
    """Show details of Pet"""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('details.html', pet=pet)


@app.route('/pet/<int:pet_id>/edit', methods=["POST", "GET"])
def edit_pet(pet_id):
    """show form to edit and handle said edit form"""
    form = EditPetForm()

    if form.validate_on_submit():
        url = form.photo_url.data
        notes = form.note.data

        pet = Pet.query.get_or_404(pet_id)

        pet.photo_url = url
        pet.notes = notes
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/pet/{pet_id}')
    else:
        return render_template('edit_pet_form.html', form=form, pet_id=pet_id)
