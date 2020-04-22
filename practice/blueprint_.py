'''
플라스크는 어플리케이션 컴포넌트를 만들고 
어플리케이션 내부나 어플리케이션 간에 공통 패턴을 지원하기 위해 
블루프린트라는 개념을 사용한다. 

블루프린트는 보통 대형 어플리케이션이 동작하는 방식을 
단순화하고 어플리케이션의 동작을 등록하기 위한 플라스크 확장에 대한 
중앙 집중된 수단을 제공할 수 있다. 

Blueprint 객체는 flask 어플리케이션 객체와 유사하게 동작하지만 
실제로 어플리케이션은 아니다. 
'''

'''

'''

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                    template_folder='templates')

@simple_page.route("/", defaults={'page':'index'})
@simple_page.route("/<page")
def show(page):
    try : return render_template("pages/%s.html" % page)
    except TemplateNotFound:
        abort(404)