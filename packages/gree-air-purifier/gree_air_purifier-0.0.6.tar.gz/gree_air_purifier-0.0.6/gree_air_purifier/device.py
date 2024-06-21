from gree_air_purifier.client import Client
from enum import unique, Enum, IntEnum


class State(Enum):
    POWER = 'Pow'
    MODE = 'mode'
    FAN_SPEED = 'wspd'
    PM25 = 'wipm25'
    AIR_CHILD_LOCK = 'AirChildLock'


@unique
class Mode(IntEnum):
    AUTO = 1
    SLEEP = 2
    TURBO = 3


@unique
class FanSpeed(IntEnum):
    LOW = 1
    MEDIUM_LOW = 2
    MEDIUM = 3
    MEDIUM_HIGH = 4
    HIGH = 5


class Device:
    def __init__(self, ip, port, name, mac):
        self.ip = ip
        self.port = port
        self.name = name
        self.mac = mac

        self._key = None

    def __str__(self):
        """Return a string representation of the car."""
        return f"name: {self.name} mac: {self.mac} @{self.ip}:{self.port}"

    def __eq__(self, value):
        if isinstance(value, Device):
            return self.mac == value.mac

        return False

    def bind(self):
        client = Client(self.ip, self.port)
        _, data = client.send({
            'cid': 'app',
            'i': 1,
            't': 'pack',
            'uid': 0,
            'tcid': self.mac,
            'pack': {
                'mac': self.mac,
                't': 'bind',
                'uid': 0
            },
        })

        pack = data['pack']

        if pack:
            result = pack.get('t')

            if result == 'bindok':
                key = pack.get('key')

                self._key = key

                return

        raise Exception

    def get_state(self, cols: list[str | State]):
        if not self._key:
            self.bind()

        client = Client(self.ip, self.port)
        _, data = client.send({
            'cid': 'app',
            'i': 0,
            't': 'pack',
            'uid': 0,
            'tcid': self.mac,
            'pack': {
                'mac': self.mac,
                't': 'status',
                'cols': [col.value if isinstance(col, State) else col for col in cols]
            }
        }, self._key)

        pack = data.get('pack')

        return dict(zip(
            pack.get('cols', []),
            pack.get('dat', [])
        ))

    def set_state(self, states: dict[str | State, int]):
        if not self._key:
            self.bind()

        keys = list([key.value if isinstance(key, State) else key for key in states.keys()])
        values = list(states.values())

        client = Client(self.ip, self.port)
        _, data = client.send({
            'cid': 'app',
            'i': 0,
            't': 'pack',
            'uid': 0,
            'tcid': self.mac,
            'pack': {
                'opt': keys,
                'p': values,
                't': 'cmd',
            }
        }, self._key)

        pack = data.get('pack')

        return dict(zip(
            pack.get('opt'),
            pack.get('val')
        ))
