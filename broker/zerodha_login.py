import pyotp
import requests

def get_enctoken(userid, password, totp_secret):

    session = requests.Session()

    login_url = "https://kite.zerodha.com/api/login"

    r = session.post(
        login_url,
        data={
            "user_id": userid,
            "password": password
        }
    )

    data = r.json()

    request_id = data["data"]["request_id"]

    totp = pyotp.TOTP(totp_secret).now()

    twofa_url = "https://kite.zerodha.com/api/twofa"

    session.post(
        twofa_url,
        data={
            "user_id": userid,
            "request_id": request_id,
            "twofa_value": totp
        }
    )

    enctoken = session.cookies.get("enctoken")

    return enctoken