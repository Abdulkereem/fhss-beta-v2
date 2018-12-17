from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_uploads import UploadSet, configure_uploads, IMAGES

from models.enrollee import * 
dash = Blueprint('dashboard', __name__)
photos = UploadSet('photos', IMAGES)

@dash.route('/dashboard')
@login_required
def dashboard():
    relatives = Relative.query.filter_by(creator=current_user.id).all()
    return render_template('./dashboard/index.html', relatives=relatives)


@dash.route('/processor',methods=['POST'])
@login_required
def processor():
    if current_user.registerd_relative == 4:
        flash('Access Denied!!!')
        return redirect(url_for('dashboard.dashboard'))
    else:
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        dob = request.form['DoB']
        gender = request.form['Gender']
        blood_group=request.form['Blood_group']
        passport=request.files['passport']

        filename = photos.save(passport)
        url = photos.url(filename)
        new_membe = Relative(creator=current_user.id, first_name=fname,dob=dob,
        gender=gender,passport=url,blood_group=blood_group,
                             last_name=lname, middle_name=mname)
        current_user.registerd_relative +=1 
        db.session.add(new_membe)
        db.session.commit()
        flash('Record Saved')
        return redirect(url_for('dashboard.dashboard'))


@dash.route('/enrollee/histories')
def hist():
    user = Histories.query.filter_by(Patient_id=current_user.id).all()
    return render_template('./hcp/history/index.html', user=user)

