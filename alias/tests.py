import pytest
import datetime


def test_check_if_date_is_in_range(self):
    str_date, from_date, to_date = (
        datetime(2020, 11, 11), datetime(
            2020, 1, 1), datetime(2020, 10, 10)
    )
    self.assertTrue((str_date, from_date, to_date), False)
