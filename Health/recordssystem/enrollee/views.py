from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import random
from models.enrollee import *


hom = Blueprint('homepage', __name__)

@hom.route('/')
def home():
    hmos_list = Enrollee.query.filter_by(hmo_role=True)
    return render_template('./home/index.html', hmos_list=hmos_list)


