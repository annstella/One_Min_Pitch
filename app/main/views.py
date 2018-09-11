from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Group,Line,Comment
from .forms import LineForm,CommentForm,GroupForm
from flask_login import login_required,current_user

# Views
@main.route('/')
def index():

    title = 'Home'

    groups = Group.get_groups()

    return render_template('index.html', title = title, groups=groups )

@main.route('/group/new', methods=['GET','POST'])
@login_required
def new_group():

    '''
    View new group route function that returns a page with a form to create a category
    '''

    form = GroupForm()

    if form.validate_on_submit():
        name = form.name.data
        new_group = Group(name=name)
        new_group.save_group()

        return redirect(url_for('.index'))

    title = 'New Group'
    return render_template('new-group.html', group_form = form)


@main.route('/group/<int:id>')
def group(id):

    '''
    View group route function that returns a list of pitches in the route and allows a user to create a pitch for the selected route
    '''
    group = Group.query.get(id)

    if group is None:
        abort(404)

    lines = Line.get_lines(id)
    title = f'{group.name} page'

    return render_template('group.html', title=title, group=group, lines=lines)