
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    def __init__(self,author,quote):
        self.author =author
        self.quote =quote
        
    


class User(UserMixin,db.Model):
    __tablename__ ='users'
    id =db.Column(db.Integer, primary_key =True)
    username =db.Column(db.String(255))
    role_id =db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure =db.Column(db.String(255))
    email =db.Column(db.String(255), unique =True,index =True)
    bio =db.Column(db.String(255))
    profile_pic_path =db.Column(db.String())
    blogs =db.relationship("Post",backref='user',lazy ='dynamic')
    comment = db.relationship("Comment",backref="user",lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('You can not read the password atribute')

    @password.setter
    def password(self,password):
        self.pass_secure =generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)        




    def __repr__(self):
        return f'User{self.username}'




class Role(db.Model):
    __tablename__ ='roles'
    id = db.Column(db.Integer,primary_key =True) 
    name = db.Column(db.String(255))
    users =db.relationship('User',backref ='role',lazy ="dynamic")
  

    def __repr__(self):
        return f'Role{self.name}'   

class Post(db.Model):
    __tablename__ ='post'
    id =db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    blog =db.Column(db.String(255))  
    user_id =db.Column(db.Integer,db.ForeignKey('users.id'))  
    comment = db.relationship("Comment",backref="post",lazy="dynamic")
     

    def save_post(self):
        db.session.add(self)
        db.session.commit() 

    @classmethod    
    def delete_blog(cls,blog_id):
        deleted =Post.query.filter_by(id=blog_id).all()
        deleted.remove()   


    def __repr__(self):
      return f'Post {self.blog}'     

class Comment(db.Model):
    __tablename__ ='comments'
    id =db.Column(db.Integer, primary_key =True)
    comment =db.Column(db.Text())
    post_id = db.Column(db.Integer,db.ForeignKey("post.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        comments =Comment.query.filter_by(post_id=post_id).all()

        return comments
    @classmethod
    def delete_comment(cls,post_id):
        comment =Comment.query.filter_by(post_id=post_id).first() 
        comment.remove()      
          