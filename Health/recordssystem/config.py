userpass = 'mysql://root:@'
basedir = '127.0.0.1'

#basedir = '192.168.1.139'
dbname = '/computer'


SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/record.db'  # userpass + basedir + dbname

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'kcsjjjcjdfiojdiofioaidsiuyaudiyausidyiucguyzh'

NEXMO_API_KEY = '90389872'
NEXMO_API_SECRET = 'uwt4vYJX3ujMBj3r'
NEXMO_NUMBER = '+2347085028240'

UPLOAD_FOLDER = '/static/passport'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])




#userpass = 'mysql://root:@'
#basedir = '127.0.0.1'

#basedir = '192.168.1.139'
#dbname = '/locker'


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/test.db'#userpass + basedir + dbname  #userpass + basedir + dbname #
