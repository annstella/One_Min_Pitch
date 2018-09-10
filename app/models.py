from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    lines = db.relationship('Line', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    votes = db.relationship('Vote', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
     lines = db.relationship('Line', backref='group', lazy='dynamic')

      def save_group(self):

        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_groups(cls):

         groups = Group.query.all()

         return groups

class Line(db.Model):
    __tablename__ = 'lines'
    id = db.Column(db.Integer, primary_key = True)
     line_content = db.Column(db.String(200))
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id") )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )
    comments = db.relationship('Comment', backref='line', lazy='dynamic')

    def save_line(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_lines(cls,group_id)

        lines = Line.query.order_by(Line.id.desc()).filter_by(group_id=group_id).all()

        return lines


