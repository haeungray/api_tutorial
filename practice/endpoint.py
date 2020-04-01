from flask import Flask, request, jsonify
from flask.json import JSONEncoder

# Default JSON encoder는 set 을 JSON으로 변환할 수 없다 
# 그러므로 커스텀 엔코더를 작성해서 SET을 lsit로 변환하여 
# JSON으로 변환 가능하게 해주어야 한다.. 

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return JSONEncoder.default(self,obj)

app = Flask(__name__)
