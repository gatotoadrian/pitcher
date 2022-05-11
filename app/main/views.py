from app.main.forms import EditProfile, PitchForm
from app.models import Dislikes, Likes, Pitch, User
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from .. import db
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pitches', methods=['GET', 'POST'])
@login_required
def pitches():

    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        pitch = Pitch(pitch=pitch_form.pitch.data, name=pitch_form.name.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('.pitches'))
    posts = Pitch.query.all()
    return render_template('pitches.html',posts=posts,pitches=pitches, pitch_form=pitch_form)

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    posts = user.pitches.all()
    
    return render_template('profile.html', user=user, pitches=posts)

@main.route('/like/<id>', methods=['GET', 'POST'])
@login_required
def like(id):
    get_pitches = Likes.get_likes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string + " " + to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches', id=id))
        else:
            continue
    new_vote = Likes(user=current_user, pitch_id=id, like=like(id))
    new_vote.save()
    return redirect(url_for('main.pitches', id=id))


@main.route('/like/<id>', methods=['GET', 'POST'])
@login_required
def dislike(id):
    get_pitches = Dislikes.get_dislikes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string + " " + to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitches', id=id))
        else:
            continue
    new_vote = Dislikes(dislike=current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.pitches', id=id))


@main.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfile()
    if form.validate_on_submit():
        current_user.username = form.name.data
        current_user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been update')
        return redirect(url_for('.profile', username = current_user.username))
    form.name.data  = current_user.username
    form.bio.data = current_user.bio
    return render_template('edit.html', form=form)




    