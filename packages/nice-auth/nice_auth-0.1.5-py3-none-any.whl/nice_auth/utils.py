import hmac
import hashlib
import base64
import json
import random
import string
from datetime import datetime

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES 암호화 함수
def encrypt_aes(data, key, iv):
    secure_key = key.encode()  # 키를 바이트 형식으로 인코딩
    iv = iv.encode()  # IV를 바이트 형식으로 인코딩
    json_data_str = json.dumps(data)  # 딕셔너리를 JSON 문자열로 변환
    cipher = AES.new(secure_key, AES.MODE_CBC, iv)  # AES CBC 모드 암호화 객체 생성
    encrypted = cipher.encrypt(pad(json_data_str.encode(), AES.block_size))  # 데이터를 패딩하여 암호화
    enc_data = base64.b64encode(encrypted).decode()  # 암호화된 데이터를 Base64로 인코딩
    return enc_data  # 인코딩된 암호화 데이터 반환

# HMAC-SHA256 해시 생성 함수
def hmac_sha256(secret_key, message):
    hmac256 = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).digest()  # HMAC-SHA256 해시 생성
    integrity_value = base64.b64encode(hmac256).decode()  # 해시를 Base64로 인코딩
    return integrity_value  # 인코딩된 해시 값 반환

# 고유 요청 번호 생성 함수
def generate_request_no():
    current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # 현재 타임스탬프 생성
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))  # 10자리 랜덤 문자열 생성
    return f"{current_timestamp}{random_str}"  # 타임스탬프와 랜덤 문자열 결합하여 반환

# AES 복호화 함수
def decrypt_aes(data, key, iv):
    key = key.encode('utf-8')  # 키를 바이트 형식으로 인코딩
    iv = iv.encode('utf-8')  # IV를 바이트 형식으로 인코딩
    cipher = AES.new(key, AES.MODE_CBC, iv)  # AES CBC 모드 복호화 객체 생성
    encrypted_data = base64.b64decode(data)  # 암호화된 데이터를 Base64로 디코딩
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)  # 패딩을 제거하여 데이터 복호화
    return decrypted_data.decode('euc-kr')  # 복호화된 데이터를 euc-kr로 디코딩하여 반환
