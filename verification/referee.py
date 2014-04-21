from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee


cover = """def cover(func, in_data):
    return func(tuple(tuple(row) for row in in_data))
"""

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(tests=TESTS,
                   cover_code={
                       'python-27': cover,  # or None
                       'python-3': cover
                   },
                   function_name="count_gold"
    ).on_ready)
