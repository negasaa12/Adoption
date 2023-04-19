from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, Optional, DataRequired, URL


class AddPetForm(FlaskForm):

    name = StringField('Pet Name')

    species = SelectField('Select Species', choices=[
                          ('dog', 'Dogs'), ('cat', 'Cat'),  ('porcupine', 'Porcupine')],)

    photo_url = StringField("Pet Image", validators=[
                            URL(message="Please be sure it's a URL image")])

    age = IntegerField('Age', validators=[
                       InputRequired(message="Please choose age")])

    note = StringField('Notes')


class EditPetForm(FlaskForm):

    photo_url = StringField("Pet Image", validators=[
        URL(message="Please be sure it's a URL image")])

    note = StringField('Notes')
