import json
import socket
import base64
from typing import Tuple

from Crypto.Cipher import AES
from gree_air_purifier.const import GENERIC_KEY, NETWORK_TIMEOUT

Address = Tuple[str, int]


class Client:
    def __init__(self, ip, port, timeout=NETWORK_TIMEOUT, is_broadcast=False):
        self._ip = ip
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._is_broadcast = is_broadcast

        self._socket.settimeout(timeout)

        if is_broadcast:
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self._socket.bind(('0.0.0.0', port))

    @property
    def server_address(self) -> Address:
        return self._ip, self._port

    def _transform_response(self, response: bytes, key):
        data = json.loads(response.decode())

        if data.get('pack'):
            data['pack'] = self.decrypt_payload(data['pack'], key)

        return data

    def send(self, data, key=GENERIC_KEY) -> list[Address] | Address:
        if data.get('pack'):
            data['pack'] = self.encrypt_payload(data['pack'], key)

        message = json.dumps(data)

        self._socket.sendto(message.encode(), self.server_address)

        if self._is_broadcast:
            responses = []

            while True:
                try:
                    response, address = self._socket.recvfrom(4096)
                    data = self._transform_response(response, key)

                    responses.append((address, data))
                except socket.timeout:
                    break

            self._socket.close()

            return responses
        else:
            response, address = self._socket.recvfrom(4096)
            data = self._transform_response(response, key)

            self._socket.close()

            return address, data

    @staticmethod
    def encrypt_payload(payload, key=GENERIC_KEY):
        def pad(s):
            bs = 16
            return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

        cipher = AES.new(key.encode(), AES.MODE_ECB)
        encrypted = cipher.encrypt(pad(json.dumps(payload)).encode())
        encoded = base64.b64encode(encrypted).decode()

        return encoded

    @staticmethod
    def decrypt_payload(payload, key=GENERIC_KEY):
        cipher = AES.new(key.encode(), AES.MODE_ECB)
        decoded = base64.b64decode(payload)
        decrypted = cipher.decrypt(decoded).decode()
        t = decrypted.replace(decrypted[decrypted.rindex('}') + 1:], '')

        return json.loads(t)
