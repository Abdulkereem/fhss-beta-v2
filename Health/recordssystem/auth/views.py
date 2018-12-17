from flask import Blueprint , render_template,request,flash,jsonify,redirect,url_for,session,g
from models.enrollee import *
import random
from werkzeug.security import generate_password_hash, check_password_hash
#import mailer 
from flask_mail import Mail, Message
from sqlalchemy.exc import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import nexmo
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import shortuuid
from werkzeug.utils import secure_filename
import os
from flask import current_app as app
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class 

s= URLSafeTimedSerializer('fjkdjljsdlkjdlkdjkldjkdj')

photos = UploadSet('photos', IMAGES)



NEXMO_API_KEY = '90389872'
NEXMO_API_SECRET = 'uwt4vYJX3ujMBj3r'

client=nexmo.Client(
	key=NEXMO_API_KEY,
	secret=NEXMO_API_SECRET
)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


login=Blueprint('login',__name__)


@login.route('/signup',methods=['POST'])
def signup():
    
    #mode=request.form['mode']
    sector = request.form['sector']
    if sector == 'Informal':
        print("it informal")
        #app.config['UPLOADED_PHOTOS_DEST'] = UPLOADFOLDER
        configure_uploads(app, photos)
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        gender = request.form['gender']
        blood_group = request.form['Blood_group']
        marital_status = request.form['marital_status']
        phone_number = request.form['phone_number']
        email = request.form['email']
        nin = request.form['nin']
        falpha=fname[0]
        username=request.form['username']
        password=request.form['password']
        passport = request.files['passport']
        filename=photos.save(passport,name=nin+'.')
        url = photos.url(filename)
        dob = request.form['DoB']
        hashed_password = generate_password_hash(password, method='sha256')
        lalpha = len(lname)
        lalpha=str(lalpha)
        lalpha = int(lalpha)
        new_sequence=random.randint(356356536,5763737676376)
        newlalpha=lname[(lalpha)-1:]
        fhss = falpha+str(newlalpha)+str(new_sequence)
        try:

            new_enrollee = Enrollee(fhss=fhss, mode_of_reg="informal", sector=sector, first_name=fname,
            middle_name=mname,last_name=lname,gender=gender,
            blood_group=blood_group,marital_status=marital_status,
            phone=phone_number,email=email,
            nin=nin, username=username, 
        
            password=hashed_password,
            dob=dob,passport=url,enrollee_role=True)
            db.session.add(new_enrollee)
            db.session.commit()
            flash('Congratulation your registration s successful')
            return redirect(url_for('homepage.home'))
        except IntegrityError:
            flash('Sorry!!! user already exist')
            return redirect(url_for('homepage.home'))
    else:
        mode = request.form['mode']
        if mode == 'Public':
            sector_public = request.form['sector_public']
            fname = request.form['fname']
            mname = request.form['mname']
            lname = request.form['lname']
            gender = request.form['gender']
            blood_group = request.form['Blood_group']
            marital_status = request.form['marital_status']
            phone_number = request.form['phone_number']
            email = request.form['email']
            nin = request.form['nin']
            falpha = fname[0]
            username = request.form['username']
            password = request.form['password']
            passport = request.files['passport']
            filename = photos.save(passport, name=nin+'.')
            url = photos.url(filename)
            dob = request.form['DoB']
            hashed_password = generate_password_hash(password, method='sha256')
            lalpha = len(lname)
            lalpha = str(lalpha)
            lalpha = int(lalpha)
            new_sequence = random.randint(356356536, 5763737676376)
            newlalpha = lname[(lalpha)-1:]
            fhss = falpha+str(newlalpha)+str(new_sequence)
            try:

                new_enrollee = Enrollee(fhss=fhss, mode_of_reg=mode,first_name=fname,
                                        middle_name=mname, last_name=lname, gender=gender,
                                        blood_group=blood_group, marital_status=marital_status,
                                        phone=phone_number, email=email,
                                        nin=nin, username=username,
                                        password=hashed_password,passport=url,dob=dob,enrollee_role=True)
                db.session.add(new_enrollee)
                db.session.commit()
                flash('Congratulation your registration s successful')
                return redirect(url_for('homepage.home'))
            except IntegrityError:
                flash('Sorry!!! user already exist')
                return redirect(url_for('homepage.home'))
                
            #return jsonify({'success': 'Registration Successful'})
        #return jsonify({'fail':'Error'})
        else:
            sector_private = request.form['sector_private']
            fname = request.form['fname']
            mname = request.form['mname']
            lname = request.form['lname']
            gender = request.form['gender']
            blood_group = request.form['Blood_group']
            marital_status = request.form['marital_status']
            phone_number = request.form['phone_number']
            email = request.form['email']
            nin = request.form['nin']
            falpha = fname[0]
            username = request.form['username']
            password = request.form['password']
            passport = request.files['passport']
            filename = photos.save(passport, name=nin+'.')
            url = photos.url(filename)
            dob = request.form['DoB']
            hashed_password = generate_password_hash(password, method='sha256')
            lalpha = len(lname)
            lalpha = str(lalpha)
            lalpha = int(lalpha)
            new_sequence = random.randint(356356536, 5763737676376)
            newlalpha = lname[(lalpha)-1:]
            fhss = falpha+str(newlalpha)+str(new_sequence)
            try:

                new_enrollee = Enrollee(fhss=fhss, mode_of_reg=mode, first_name=fname,
                                        middle_name=mname, last_name=lname, gender=gender,
                                        blood_group=blood_group, marital_status=marital_status,
                                        phone=phone_number, email=email,
                                        nin=nin, username=username,
                                        password=hashed_password, passport=url, dob=dob, enrollee_role=True, sector=sector_private)
                db.session.add(new_enrollee)
                db.session.commit()
                flash('Congratulation your registration s successful')
                return redirect(url_for('homepage.home'))
            except IntegrityError:
                flash('Sorry!!! user already exist')
                return redirect(url_for('homepage.home'))




@login.route('/create')
def creat():
    db.create_all()
    return("table created")
@login.route('/drop')
def drop():
    db.drop_all()
    return'table dropped'


@login.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    user = Enrollee.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password,password): 
            if user.enrollee_role==True:
                """
                ur_id = shortuuid.ShortUUID().random(length=3)
                sms=client.send_message({
                    'from': 'FHSS',
                    'to': user.phone,
                    'text': 'your opt is '+str(ur_id)

                })
                expire = s.dumps(user.email, salt='exp')
                new_token = otp(token=ur_id, 
                user_id=user.id,expire=expire)
                db.session.add(new_token)
                db.session.commit()
                id=user.username
                
                return redirect(url_for('login.verify'))
                """
                login_user(user)
                return redirect(url_for('dashboard.dashboard'))
            elif user.hcp_role==True:
                login_user(user)
                return redirect(url_for('hcp.hcpmain'))
            elif user.hmo_role==True:
                login_user(user)
                return redirect(url_for('hmos.main'))
            elif user.fhss_role==True:
                login_user(user)
                return redirect(url_for('fhss.fmain'))
            else:
                return 'sorry invalid permission'
        else:
            flash("invalid username or password")
            return redirect(url_for('homepage.home'))
    else:
        flash("invalid username or password")
        return redirect(url_for('homepage.home'))
        #return redirect(url_for('homepage.index'))

@login.route('/verify',methods=['GET','POST'])
def verify():
    if request.method =='POST':
        try:
            
            token = request.form['token']
            
            code = otp.query.filter_by(token=token).first()
            ckeck_top = s.loads(code.expire, salt='exp', max_age=60604800)
            if code:
                user = Enrollee.query.filter_by(id=code.user_id).first()
                if user:
                    login_user(user)
                    return redirect(url_for('dashboard.dashboard'))
        except SignatureExpired:
            return 'otp expired'
    return render_template('./auth/otp.htm')


@login.route('/logout')
def logout():
	logout_user()
	flash("sign out successful")
	return redirect(url_for('homepage.home'))


@login.route('/hcp/join', methods=['POST'])
def create():
    hsp = request.form['hsp']
    address = request.form['address']
    username = request.form['username']
    password = request.form['password']
    medic_no = request.form['medic']
    rc = request.form['rc']
    tax_id = request.form['tx']
    hmo=request.form['hmo']
    check_hmo = Enrollee.query.filter_by(organ=hmo).first()
    hmo_id = check_hmo.id
    hashed_password = generate_password_hash(password, method='sha256')

    new_hcp = Enrollee(hospital_name=hsp, address=address,
                                            username=username, password=hashed_password,
                                            medical_regno=medic_no, rc_number=rc,
                       tax_id=tax_id, hcp_role=True, hmo_name=hmo,hmo_id=hmo_id)
    db.session.add(new_hcp)
    db.session.commit()
    flash('Your account has been created as Health Care Service Provider, please click signin')
    return redirect(url_for('homepage.home'))





@login.route('/hmo/signup',methods=['POST'])
def hmosignup():
    try:
        org = request.form['orgname']
        addr= request.form['addrs']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = Enrollee(organ=org,
        address=addr,username=username,
                    password=hashed_password,
                    hmo_role=True)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration Complete')
        return redirect(url_for('homepage.home'))
    except IntegrityError:
        flash('sorry user already exist')
        return redirect(url_for('homepage.home'))



