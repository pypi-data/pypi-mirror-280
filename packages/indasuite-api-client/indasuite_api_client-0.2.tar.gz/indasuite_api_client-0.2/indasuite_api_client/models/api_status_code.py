from enum import IntEnum


class ApiStatusCode(IntEnum):
    VALUE_1010 = 1010
    VALUE_1020 = 1020
    VALUE_1021 = 1021
    VALUE_1022 = 1022
    VALUE_1050 = 1050
    VALUE_1060 = 1060
    VALUE_1300 = 1300
    VALUE_1301 = 1301
    VALUE_1302 = 1302
    VALUE_1303 = 1303
    VALUE_1305 = 1305
    VALUE_1310 = 1310
    VALUE_1350 = 1350
    VALUE_1360 = 1360
    VALUE_1400 = 1400
    VALUE_1403 = 1403
    VALUE_1404 = 1404
    VALUE_1405 = 1405
    VALUE_1406 = 1406
    VALUE_1500 = 1500
    VALUE_1501 = 1501
    VALUE_1502 = 1502
    VALUE_1503 = 1503

    def __str__(self) -> str:
        return str(self.value)
