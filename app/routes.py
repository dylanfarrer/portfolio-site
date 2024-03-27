from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

"""
@bp.route('/')
def index():
    return render_template('index.html')
"""

@bp.route('/')
def my_home():
    return render_template('index.html')

@bp.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@bp.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            #write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return 'hmm, something went wrong'