from django.test import TestCase
from alias.models import Alias
from django.utils import timezone
from datetime import datetime
from alias.utils import get_aliases, check_if_overlap, check_if_date_is_in_range


class SimpleTest(TestCase):
    def setUp(self):
        Alias.objects.create(
            alias='useful0',
            target='types-slug-023xf',
            start=datetime(2020, 2, 2),
            end=datetime(2020, 2, 2)
        )
        Alias.objects.create(
            alias='useful0',
            target='types-slug-023xf',
            start=datetime(2020, 2, 2),
            end=datetime(2020, 2, 2)
        )
        Alias.objects.create(
            alias='useful1',
            target='types-slug-023xf',
            start=datetime(2020, 2, 2),
            end=datetime(2020, 2, 2)
        )
        Alias.objects.create(
            alias='useful2',
            target='types-slug-023xf',
            start=datetime(2020, 10, 10),
            end=None
        )

    def test_get_aliases(self):
        aliases = get_aliases(
            'types-slug-023xf',
            datetime(2020, 1, 1),
            datetime(2020, 4, 4))
        self.assertFalse(aliases[0].alias is aliases[1].alias)
        self.assertTrue(aliases[0].alias is not aliases[1].alias)

    def test_check_if_overlap_True(self):
        start1, end1, start2, end2 = (
            datetime(2020, 1, 1), datetime(2020, 2, 1),
            datetime(2020, 1, 1), datetime(2020, 2, 5)
        )
        self.assertTrue(check_if_overlap(start1, end1, start2, end2))

    def test_check_if_overlap_False(self):
        start1, end1, start2, end2 = (
            datetime(2020, 1, 1), datetime(2020, 2, 1),
            datetime(2020, 3, 1), datetime(2020, 4, 5)
        )
        self.assertFalse(check_if_overlap(start1, end1, start2, end2))

    def test_check_if_date_is_in_range_True(self):
        str_date, from_date, to_date = (
            datetime(2020, 5, 5), datetime(
                2020, 1, 1), datetime(2020, 10, 10)
        )
        self.assertTrue(check_if_date_is_in_range(
            str_date, from_date, to_date))

    def test_check_if_date_is_in_range_False(self):
        str_date, from_date, to_date = (
            datetime(2020, 11, 11), datetime(
                2020, 1, 1), datetime(2020, 10, 10)
        )
        self.assertFalse(check_if_date_is_in_range(
            str_date, from_date, to_date))
