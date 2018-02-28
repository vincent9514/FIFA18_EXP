DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'vincentwang'
PASSWORD = 'wangziwen199514'
HOST = 'flaskfinal.cow2gkwr2fps.us-west-2.rds.amazonaws.com'

PORT = '3306'
DATABASE = 'flaskfinal'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS=False
