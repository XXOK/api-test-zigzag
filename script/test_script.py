from gql.script_query import *
from gql.script_variables import *
import requests
import json

rs = requests.Session()

def test_user_sign_up(): # 회원가입 성공 여부를 검증합니다.
    q = rs.post(api2, json={'query': user_sign_up, 'variables': sign_up_account})
    json_data = json.loads(q.text)
    assert json_data['data']['signup']['user_account']['email'] == sign_up_account['input']['email']

def test_user_login(): # 가입한 계정으로 로그인 성공 여부를 검증합니다.
    q = rs.post(api2, json={'query': user_login, 'variables': login_account})
    json_data = json.loads(q.text)
    assert json_data['data']['login']['success'] == True

def test_user_info(): # 로그인한 계정의 이름 정보를 검증합니다.
    q = rs.post(api2, json={'query': user_info})
    json_data = json.loads(q.text)
    assert json_data['data']['user_account']['full_name'] == '회원'

def test_user_delete(): # 계정 삭제 성공 여부를 검증합니다.
    q = rs.post(api2, json={'query': user_delete, 'variables': delete_account})
    json_data = json.loads(q.text)
    assert json_data['data']['deleteUserAccount']['success'] == True

