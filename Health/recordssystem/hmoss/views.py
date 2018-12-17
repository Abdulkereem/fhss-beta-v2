from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for,abort
from werkzeug.security import generate_password_hash, check_password_hash
import random
from models.Hcp import *
from models.enrollee import * 
import shortuuid
import nexmo


hmos = Blueprint('hmos', __name__)
def hmo_required():
    if current_user.hmo_role == False:
        return abort(404)
    else:
        pass

@hmos.route('/hmo')
def homehmo():
    return render_template('./hmo/index.html')


@hmos.route('/hmain')
@login_required
def main():
    hmo_required()
    test = Enrollee.query.filter_by(hcp_role=True).all()

    return render_template('./hmo/dashboard.html',test=test)


@hmos.route('/hprofile/<int:id>')
@login_required
def hprofile(id):
    hmo_required()
    user = Enrollee.query.filter_by(id=id).first()
    return render_template('/hmo/profile.html', user=user)

@hmos.route('/hsignup')

def hsignup():
    
    return render_template('hmo/signup/index.html')

@hmos.route('/view/<int:id>')
@login_required
def view(id):
    hmo_required()
    user = Histories.query.filter_by(Hospital_ID=id).all()
    return render_template('./hmo/view/index.html', user=user)

@hmos.route('/claim')
@login_required
def claim():
    hmo_required()
    postcost = Histories.query.filter_by(hmo_id=current_user.id).all()
    i = 0
    for costs in postcost:
        #print(costs.post_cost)
        i+=costs.post_cost
        print(i)
        current_user.post_cost = i
    new_claim = payments_claims(Hmo_Name=current_user.organ, Hmo_ID=current_user.id,
                                hmo_reg_no=current_user.hmo_reg_no,cost_claim=i)
    db.session.add(new_claim)
    db.session.commit()
    flash('claim notification has been sent to the FHSS')
    return redirect(url_for('hmos.main'))

@hmos.route('/view_claims')
@login_required
def view_claims():
    hmo_required()
    user = payments_claims.query.filter_by(Hmo_ID=current_user.id).all()
    return render_template('./hmo/view/payment.html', user=user)

    







