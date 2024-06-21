import hmac
import hashlib
import base64
import json


class HMACUtil:

    def __init__(self, data, secret):
        if isinstance(data, dict):
            # if verify third part signature, should be request.body avoid this problem,
            # not drf request.data
            data = self.sort_dict_string(data)

        if not isinstance(data, bytes):
            data = data.encode('utf-8')

        self.data = data
        self.secret = secret

    def verify_signature(self, signature):
        if not isinstance(signature, bytes):
            signature = signature.encode('utf-8')
        computed_hmac = self.sign()
        return hmac.compare_digest(computed_hmac, signature)

    def sign(self):
        digest = hmac.new(self.secret.encode('utf-8'), self.data, digestmod=hashlib.sha256).digest()
        return base64.b64encode(digest)

    @staticmethod
    def clean_string_data(prepare_data):
        data = prepare_data.replace(' ', '')
        data = data.replace('\n', '')
        data = data.replace('\t', '')
        data = data.replace('\r', '')

        return data

    @staticmethod
    def sort_dict_string(data):
        string_data = json.dumps(data, sort_keys=True)
        return string_data
