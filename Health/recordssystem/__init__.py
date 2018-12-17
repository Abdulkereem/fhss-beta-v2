from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
 
import os 


from models.enrollee import *
 


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png', 'jpeg'])
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+'/static/passport'
photos = UploadSet('photos', IMAGES) 
configure_uploads(app, photos)
patch_request_class(app)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)



login_manager.login_view = 'login.signin'
@login_manager.user_loader
def load_user(user_id):
    return Enrollee.query.get(int(user_id))



admin = Admin(app, name='Control Panel')
admin.add_view(ModelView(Enrollee, db.session))
admin.add_view(ModelView(Relative,db.session))
admin.add_view(ModelView(otp,db.session))

#admin.add_view(ModelView(Health_Care_Service_Provider, db.session))
admin.add_view(ModelView(payments_claims, db.session))
admin.add_view(ModelView(Histories,db.session))
admin.add_view(ModelView(scuccess_payments, db.session))




from recordssystem.enrollee.views import hom
from recordssystem.auth.views import login
from recordssystem.dashboard.views import dash
from recordssystem.hcp.views import health_care_provider
from recordssystem.hmoss.views import hmos
from recordssystem.fhssmodule.views import fhss




app.register_blueprint(enrollee.views.hom)
app.register_blueprint(auth.views.login)
app.register_blueprint(dashboard.views.dash)
app.register_blueprint(hcp.views.health_care_provider)
app.register_blueprint(hmoss.views.hmos)
app.register_blueprint(fhssmodule.views.fhss)



