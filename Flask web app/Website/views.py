from flask import Blueprint ,render_template,request
from flask_login import login_required, current_user
from .models import Upload

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('remarks')

        if len(note) < 1:
            flash('Remarks is too short!', category='error')
        else:
            new_remark = Upload(remarks=note, user_id=current_user.id)
            db.session.add(new_remark)
            db.session.commit()
            flash('Remark Added!', category='success')

    return render_template("home.html", user=current_user)





