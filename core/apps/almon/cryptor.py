import base64
import logging
import traceback
from django.conf import settings
from cryptography.fernet import Fernet


class SecurePasswordCryptor:
    def __init__(self, encrypt_key=settings.ENCRYPTION_KEY):
        self.cipher_pass = Fernet(encrypt_key)

    def encrypt(self, passwd):
        try:
            passwd = str(passwd)
            encrypt_passwd = self.cipher_pass.encrypt(passwd.encode('ascii'))
            encrypt_passwd = base64.urlsafe_b64encode(encrypt_passwd).decode("ascii")
            return encrypt_passwd
        except Exception as e:
            logging.getLogger("error_logger").error(traceback.format_exc())
            return None

    def decrypt(self, passwd):
        
        try:
            passwd = base64.urlsafe_b64decode(passwd)
            decode_password = self.cipher_pass.decrypt(passwd).decode("ascii")

            return decode_password
        except Exception as e:
            print(f"Error decoding: {e}")
            logging.getLogger("error_logger").error(traceback.format_exc())
            return None


Cryptor = SecurePasswordCryptor()
