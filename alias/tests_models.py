from django.test import TestCase
from alias.models import Alias
from django.utils import timezone
from datetime import timedelta


class AliasTestCase(TestCase):
    def setUp(self):
        Alias.objects.create(
            alias='useful',
            target='types-slug-023xf',
            start=timezone.now() - timedelta(days=50),
            end=None
        )
        Alias.objects.create(
            alias='useful2',
            target='types-slug-023xf',
            start=timezone.now() - timedelta(days=60),
            end=None
        )

    def test_alias_object_exists(self):
        useful = Alias.objects.get(alias='useful')
        self.assertEqual(useful.alias, 'useful')
        self.assertNotEqual(useful.alias, 'trash')

    def test_get_all_aliases_from_database(self):
        aliases = Alias.objects.all()
        self.assertEqual(len(aliases), 2)
