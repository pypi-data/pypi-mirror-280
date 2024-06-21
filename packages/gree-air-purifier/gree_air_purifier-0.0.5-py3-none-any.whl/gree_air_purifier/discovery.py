from gree_air_purifier.client import Client
from gree_air_purifier.const import NETWORK_TIMEOUT
from gree_air_purifier.device import Device
import logging

_logger = logging.getLogger(__name__)


class Discovery:
    def __init__(self, discovery_time=NETWORK_TIMEOUT):
        self._discovery_time = discovery_time

    def scan(self, broadcast_ip):
        client = Client(broadcast_ip, 7000, timeout=self._discovery_time, is_broadcast=True)
        result = client.send({'t': 'scan'})

        devices: list[Device] = []

        for address, data in result:
            pack = data.get('pack')

            if pack:
                name = pack.get('name')
                mac = pack.get('mac')

                device = Device(
                    ip=address[0],
                    port=address[1],
                    name=name,
                    mac=mac
                )
                devices.append(device)

                _logger.info('Found GREE air purifier device %s', str(device))

        return devices
