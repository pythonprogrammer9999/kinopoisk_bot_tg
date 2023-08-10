from kinopoisk_dev import KinopoiskDev

from secret import kp_token

kp = KinopoiskDev(token=kp_token)
headers = {"X-API-KEY": kp_token}
