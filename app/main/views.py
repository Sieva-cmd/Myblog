
from curses import flash
from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import current_user, login_required
from ..models import User,Post,Comment
from .forms import CommentForm, PostForm, UpdateProfile
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
    blogs =Post.query.filter_by(user =current_user).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user,blogs =blogs) 


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

@main.route('/create_new',methods=['POST','GET'])
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


@main.route('/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):
    post_delete =Post.query.get(post_id)
    db.session.delete(post_delete)
    db.session.commit()
    return redirect(url_for('main.index',post_id=post_id))


        
@main.route('/comment/<int:post_id>',methods=['POST','GET'])
@login_required
def comment(post_id):
    form =CommentForm()
    blog =Post.query.get(post_id)
    comments =Comment.query.filter_by(post_id=post_id).all()
    if form.validate_on_submit():
        comment =form.comment.data
        post_id =post_id
        new_comment =Comment(comment= comment,post_id=post_id,user =current_user)
        new_comment.save_comment()
        return redirect(url_for('main.comment',post_id=post_id))
    return render_template('comment.html', form=form,blog=blog,comments=comments)    
 
@main.route('/delete_comment/<comment_id>', methods =["GET","POST"])
@login_required
def delete_comment(comment_id):
    delete_comment =Comment.query.get(comment_id)
    db.session.delete(delete_comment)
    db.session.commit()
    return redirect(url_for('main.index',comment_id=comment_id))
