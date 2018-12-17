from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, abort
from datetime import datetime

db=SQLAlchemy()


class Enrollee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    mode_of_reg=db.Column(db.String(255))#formal or informal
    sector_type=db.Column(db.String(255))#private or public
    sector=db.Column(db.String(255)) #department or secteriat etc
    fhss = db.Column(db.String(255))
    sector = db.Column(db.String(255))
    first_name=db.Column(db.String(255))
    middle_name=db.Column(db.String(255))
    last_name=db.Column(db.String(255))
    gender=db.Column(db.String(255))
    blood_group=db.Column(db.String(255))
    marital_status=db.Column(db.String(255))
    dob=db.Column(db.String(255))
    phone=db.Column(db.String(255),unique=True)
    email=db.Column(db.String(255),unique=True)
    nin=db.Column(db.String(255),unique=True)
    passport=db.Column(db.String(255))
    username=db.Column(db.String(255),unique=True)
    password=db.Column(db.String(255))
    registerd_relative=db.Column(db.Integer, default=0)
    role = db.Column(db.Boolean,default=False)
    suppend = db.Column(db.Boolean,default=False)
    ailment = db.Column(db.String(255))


    #Health Care Service Provider
    hospital_name = db.Column(db.String(255))
    address = db.Column(db.String(225))
    medical_regno = db.Column(db.String(255))
    rc_number = db.Column(db.String(255))
    tax_id = db.Column(db.String(255))
    date_registerd = db.Column(db.String(255),default=datetime.now())
    block = db.Column(db.Boolean, default=False)
    hmo_name=db.Column(db.String(255))
    hmo_id=db.Column(db.Integer,default=0)
    ###roles####
    enrollee_role=db.Column(db.Boolean, default=False)
    hcp_role=db.Column(db.Boolean, default=False)
    hmo_role=db.Column(db.Boolean, default=False)
    fhss_role=db.Column(db.Boolean, default=False)



    #Health Mangement Organisation

    organ=db.Column(db.String(255))
    address=db.Column(db.String(255))
    hmo_reg_no=db.Column(db.String(255))
    rc_no=db.Column(db.String(255))
    post_cost = db.Column(db.BigInteger, default=0)

    uplaod_doc=db.Column(db.String(255))
    tax=db.Column(db.String(255))

class Relative(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    creator=db.Column(db.String(255))
    first_name=db.Column(db.String(255))
    middle_name=db.Column(db.String(255))
    last_name=db.Column(db.String(255))
    gender=db.Column(db.String(255))
    dob=db.Column(db.String(255))
    passport=db.Column(db.String(255))
    blood_group=db.Column(db.String(10))


class otp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token=db.Column(db.String(60))
    expire=db.Column(db.String(255))
    user_id = db.Column(db.BigInteger)


"""
class Health_Care_Service_Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_name = db.Column(db.String(255))
    address = db.Column(db.String(225))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    medical_regno = db.Column(db.String(255))
    rc_number = db.Column(db.String(255))
    tax_id = db.Column(db.String(255))
    date_registerd = db.Column(db.String(255),default=datetime.now())
    post_cost = db.Column(db.BigInteger, default=0)
    block = db.Column(db.Boolean, default=False)








class hmo(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    organ=db.Column(db.String(255))
    address=db.Column(db.String(255))
    username=db.Column(db.String(255))
    password=db.Column(db.String(255))
    hmo_reg_no=db.Column(db.String(255))
    rc_no=db.Column(db.String(255))
    uplaod_doc=db.Column(db.String(255))
    tax=db.Column(db.String(255))

class fhss(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String(255))
    mname=db.Column(db.String(255))
    lname=db.Column(db.String(255))
    gender=db.Column(db.String(255))
    phone=db.Column(db.String(255))
    email=db.Column(db.String(255))
    personal_file_no=db.Column(db.String(255))
    nin=db.Column(db.String(255))
    passport=db.Column(db.String(255))
    username=db.Column(db.String(255))
    password=db.Column(db.String(255))
"""


class Histories(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Hospital_Name = db.Column(db.String(255))
    Hospital_ID = db.Column(db.String(255))
    Patient_name = db.Column(db.String(255))
    Patient_nin = db.Column(db.String(255))
    Patient_id = db.Column(db.Integer)
    Patient_fhss = db.Column(db.String(255))
    hmo_id=db.Column(db.BigInteger,default=0)
    hmo_name=db.Column(db.String(255))
    date_time=db.Column(db.String(255),default=datetime.now())
    post_cost = db.Column(db.BigInteger, default=0)
    ailment = db.Column(db.String(255))


class payments_claims(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date_claim=db.Column(db.String(255),default=datetime.now())
    Hmo_Name = db.Column(db.String(255))
    Hmo_ID = db.Column(db.String(255))
    Hcp_Name = db.Column(db.String(255))
    Hcp_ID = db.Column(db.String(255))
    hmo_reg_no = db.Column(db.String(255))
    cost_claim=db.Column(db.String(255))
    approved = db.Column(db.Boolean, default=False)
    pending = db.Column(db.Boolean, default=False)
    paid = db.Column(db.Boolean, default=False)


class hmo_claims(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date_claim=db.Column(db.String(255),default=datetime.now())
    Hmo_Name = db.Column(db.String(255))
    Hmo_ID = db.Column(db.String(255))
    hmo_reg_no = db.Column(db.String(255))
    cost_claim=db.Column(db.String(255))
    approved = db.Column(db.Boolean, default=False)
    pending = db.Column(db.Boolean, default=False)
    paid = db.Column(db.Boolean, default=False)

class scuccess_payments(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Hospital_Name = db.Column(db.String(255))
    Hospital_ID = db.Column(db.String(255))
    medical_regno = db.Column(db.String(255))
    amount_paid = db.Column(db.String(255))
    cost_claim = db.Column(db.String(255))
    paid_date = db.Column(db.String(255))


    

    










'''
class backend_permission(self):
    try:
        if current_user.role==True:
            return current_user.is_authenticated
        else:
            return self.inaccessible_callback(abort(404))
    except AttributeError:
        return self.inaccessible_callaback(abort(404))

'''
