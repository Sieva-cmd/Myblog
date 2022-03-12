
from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import current_user, login_required
from ..models import User,Post
from .forms import PostForm, UpdateProfile
from .. import db,photos
from ..requests import get_quote

#views
@main.route('/')
@login_required
def index():

    title = 'My blog'
    my_quote =get_quote()
    blogs =Post.query.all()


    return render_template('index.html',title=title,my_quote=my_quote,blogs=blogs)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username =uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user) 


@main.route('/user/<uname>/update',methods=["GET","POST"])   
@login_required
def update_profile(uname):
    user =User.query.filter_by(username =uname).first()
    if user is None:
        abort(404)

    form =UpdateProfile()

    if form.validate_on_submit():
        user.bio =form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)  


@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user =User.query.filter_by(username =uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path =f'photos/{filename}'
        user.profile_pic_path =path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    

@main.route('/create_new',methods=["GET","POST"])
@login_required
def new_blog():
    form =PostForm()
    if form.validate_on_submit():
        title =form.title.data
        blog =form.blog.data
        new_blog =Post(title=title,blog=blog,user=current_user)
        new_blog.save_post()
        return redirect(url_for('main.index'))
    return render_template('new_blog.html',form =form)    