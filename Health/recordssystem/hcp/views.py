import random

import nexmo
import shortuuid
from flask import Blueprint, flash, jsonify, redirect, render_template,g,request, url_for,abort
from werkzeug.security import check_password_hash, generate_password_hash

from models.enrollee import *
from models.Hcp import *

health_care_provider = Blueprint('hcp', __name__)


NEXMO_API_KEY = '90389872'
NEXMO_API_SECRET = 'uwt4vYJX3ujMBj3r'

client=nexmo.Client(
	key=NEXMO_API_KEY,
	secret=NEXMO_API_SECRET
)

def logger(userid):
    user = Enrollee.query.filter_by(id=userid).first()
    post_cost = request.form['post_cost']
    ailment = request.form['ailment']
    user.post_cost += int(post_cost)
    user.ailment=ailment
    New_histories = Histories(Hospital_Name=current_user.hospital_name, Hospital_ID=current_user.id,
    Patient_name=user.first_name,Patient_nin=user.nin,Patient_fhss=user.fhss,post_cost=request.form['post_cost'],
                              ailment=request.form['ailment'],Patient_id=user.id,hmo_name=current_user.hmo_name,hmo_id=current_user.hmo_id)
    db.session.add(New_histories)
    db.session.commit()



def hcp_required():
    if current_user.hcp_role == True:
        pass
    else:
        return abort(404)

@health_care_provider.route('/hcp')
def index():
    return render_template('./hcp/index.html')


@health_care_provider.route('/hcpmain',methods=['GET','POST'])
@login_required
def hcpmain():
    hcp_required()
    user=None
    if request.method =='POST':
        fhssid = request.form['fhssid']
        user = Enrollee.query.filter_by(fhss=fhssid).first()
        if user:
            return render_template('./hcp/dashboard.html', user=user)

        else:
            flash('FHSS ID does not exist')
            return redirect(url_for('hcp.hcpmain'))

    return render_template('./hcp/dashboard.html',user=user)

@health_care_provider.route('/eprofile/<int:id>',methods=['GET','POST'])
@login_required
def eprofile(id):
    hcp_required()
    if request.method == 'POST':
        logger(id)
        user = Enrollee.query.filter_by(id=id).first()
        post_cost = request.form['post_cost']
        ailment = request.form['ailment']
        user.post_cost +=int(post_cost)
        user.ailment = ailment
        db.session.flush()
        db.session.commit()
        
        return render_template('/hcp/profile.html', user=user)
    user = Enrollee.query.filter_by(id=id).first()
    return render_template('/hcp/profile.html', user=user)

    


@health_care_provider.route('/eprocess/<int:id>',methods=['GET','POST'])
def eprocess(id):
    hcp_required()
    
    if request.method=='POST':
        sent_otp=request.form['otp']
        check_otp = otp.query.filter_by(id=id).first()
        if check_otp == sent_otp:
            flash('verified please close')
            return redirect(url_for('hcp.eprofile',id=check_otp.user_id  ))

    user = Enrollee.query.filter_by(id=id).first()
    ur_id = shortuuid.ShortUUID().random(length=3)
    sms = client.send_message({
        'from': current_user.hospital_name,
        'to': user.phone,
        'text': 'your opt is '+str(ur_id)

    })
    new_otp = otp(token=ur_id, expire='6000',
                  user_id=user.id)
    flash('One time password has been sent')
    return redirect(url_for('hcp.main'))


@health_care_provider.route('/hcp/logout')
def logout():
	logout_user()
	flash("sign out successful")
	return redirect(url_for('homepage.home'))


@health_care_provider.route('/hcp/histories/<int:user_id>')
def hist(user_id):
    user = Histories.query.filter_by(Patient_id=user_id).all()
    return render_template('./hcp/history/index.html',user=user)


@health_care_provider.route('/hcp_claim')
@login_required
def hcp_claim():
    hcp_required()
    postcost = Histories.query.filter_by(Hospital_ID=current_user.id,approved=True).all()
    i = 0
    for costs in postcost:
        #print(costs.post_cost)
        i += costs.post_cost
        print(i)
        current_user.post_cost = i
    new_claim = payments_claims(Hmo_Name=current_user.organ, Hmo_ID=current_user.id,
                                hmo_reg_no=current_user.hmo_reg_no, cost_claim=i)
    db.session.add(new_claim)
    db.session.commit()
    flash('claim notification has been sent to the HMO')
    return redirect(url_for('hcp.hcpmain'))

@health_care_provider.route('/test')
def test():
    
    cal = Histories.query.filter_by(Hospital_ID=current_user.id).all()
    i = 0
    for cals in cal:
        print(cals.post_cost)
        i += costs.post_cost
        #var = cals.post_cost
        #total_sum=total.append(var)
        current_user.post_cost = i
    db.session.commit()
    return str(current_user.id)


