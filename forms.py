'''
All forms for the website
'''

from flask_uploads import IMAGES, UploadSet
from flask_wtf import FlaskForm,  RecaptchaField    
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, PasswordField, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError, equal_to, regexp, NumberRange
from wtforms import ValidationError
import re 
import models

images = UploadSet('images', IMAGES)


def email_exists(form, field):
    if models.User.select().where(models.User.email == field.data).exists():
        raise ValidationError('User with email already exists')

class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email(),email_exists])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(),equal_to('password', message='Passwords must match')])
    mobile_no = StringField('Mobile Number', validators=[DataRequired(),regexp('^(\d{3})(\d{3})(\d{4})$', message="Enter 10 digit phone number.")])
    accept_tos = BooleanField('I accept the TOS', validators=[DataRequired(message="Accept this to proceed.")])
    recaptcha = RecaptchaField()


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    recaptcha = RecaptchaField()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    mobile_no = StringField("Mobile No", validators=[DataRequired(),regexp('^(\d{3})(\d{3})(\d{4})$', message="Enter 10 digit phone number.")])
    message = TextAreaField('Your Message', validators=[DataRequired()])
    recaptcha = RecaptchaField()

class new_product_form(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    image_1 = FileField('Smallest Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    image_2 = FileField('Medium Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    image_3 = FileField('Large Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    count = IntegerField('Product Count', validators=[DataRequired()])
    actual_price = IntegerField('Product Price')
    off_percent = IntegerField('Off Percent %')
    buy_price = IntegerField('Buy Price')
    style = StringField('Style')
    brand_name = StringField('Brand Name')
    frame_material = StringField('Basic Ingredients')
    usage = StringField('Usage')
    packaging = StringField('Packaging')
    model_no = StringField('Model No.')
    suitable_for = StringField('Suitable For')
    size = StringField('Quantity per Crate')
    ideal_for = StringField('Ideal For')
    typ_e = StringField('Type')
    features = StringField('Features')
    case_type = StringField('Transportation Availibility')
    dimensions_bridgesize = StringField('Bridge Size (dimensions)')
    dimensions_hrizontal_width = StringField('Horizontal Width (dimensions)')
    dimensions_frame_arm_lenght = StringField('Frame Arm Lenghth (dimensions)')
    weight = StringField('Weight')
    other_details = TextAreaField('Other Details')

class edit_product_form(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    image_1 = FileField('Smallest Image', validators=[ FileAllowed(images, 'Images only!')])
    image_2 = FileField('Medium Image', validators=[FileAllowed(images, 'Images only!')])
    image_3 = FileField('Large Image', validators=[FileAllowed(images, 'Images only!')])
    count = IntegerField('Product Count', validators=[DataRequired()])
    actual_price = IntegerField('Product Price')
    off_percent = IntegerField('Off Percent %')
    buy_price = IntegerField('Buy Price')
    style = StringField('Style')    
    brand_name = StringField('Brand Name')
    frame_material = StringField('Basic Ingredients')
    usage = StringField('Usage')
    packaging = StringField('Packaging')
    model_no = StringField('Model No.') 
    suitable_for = StringField('Suitable For')
    size = StringField('Quantity per Crate')
    ideal_for = StringField('Ideal For')
    typ_e = StringField('Type')
    features = StringField('Features')
    case_type = StringField('Transportation Availibility')
    dimensions_bridgesize = StringField('Bridge Size (dimensions)')
    dimensions_hrizontal_width = StringField('Horizontal Width (dimensions)')
    dimensions_frame_arm_lenght = StringField('Frame Arm Lenghth (dimensions)')
    weight = StringField('Weight')
    other_details = TextAreaField('Other Details')


class Checkout_form(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    room_no = StringField('Room no', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mobile = StringField("Mobile No", validators=[DataRequired(),regexp('^(\d{3})(\d{3})(\d{4})$', message="Enter 10 digit phone number.")])

class new_password(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6), equal_to('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    recaptcha = RecaptchaField()

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

class new_review(FlaskForm):
    user = StringField('User')
    order_id = StringField('Order-ID')
    text = TextAreaField('Review')
