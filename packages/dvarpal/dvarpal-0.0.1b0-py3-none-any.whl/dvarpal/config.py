import os


class SessionConfig:

    def __init__(self):

        self.authn_url: str = 'https://api.upstox.com/v2/login/authorization/dialog'
        self.authz_url: str = 'https://api.upstox.com/v2/login/authorization/token'
        self.redirect_uri: str = 'https://www.google.com'
        self.session_validation_url: str = 'https://api-v2.upstox.com/user/profile'
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'

        self.client_id: str = '4aa6ccfd-4bdc-4910-b6df-0a82146b1bd0'
        self.client_secret: str = 'rkkq1g6q11'
        self.mobile: str = '9008002380'
        self.totp_secret_key: str = 'ZUPMAK65A76WZWOE2CEC22VXE25BO4M6'
        self.pin: str = '847284'

        self.access_token_file = os.path.join(os.getenv('HOME'), 'dvarpal_session.txt')


