import unittest
from unittest.mock import patch

from scripts.events_module.relation_events import Relation_Events
from scripts.cat.cats import Cat
from scripts.cat_relations.relationship import Relationship
from scripts.clan import Clan

class CanHaveKits(unittest.TestCase):
    def test_prevent_kits(self):
        # given
        relation_events = Relation_Events()
        cat = Cat()
        cat.no_kits = True

        # then
        self.assertFalse(relation_events.check_if_can_have_kits(cat,unknown_parent_setting=True))



class Pregnancy(unittest.TestCase):
    @patch('scripts.events_module.relation_events.Relation_Events.check_if_can_have_kits')
    def test_single_cat_female(self, check_if_can_have_kits):
        # given
        relation_events = Relation_Events()
        clan = Clan()
        cat = Cat(gender = 'female')
        clan.pregnancy_data = {}

        # when
        check_if_can_have_kits.return_value = True
        relation_events.handle_zero_moon_pregnant(cat,None,None,clan)

        # then
        self.assertIn(cat.ID, clan.pregnancy_data.keys())

    @patch('scripts.events_module.relation_events.Relation_Events.check_if_can_have_kits')
    def test_pair(self, check_if_can_have_kits):
        # FIXME
        pass


class Mates(unittest.TestCase):
    def test_platonic_kitten_mating(self):
        # given
        relation_events = Relation_Events()
        cat1 = Cat(moons=3)
        cat2 = Cat(moons=3)

        relationship1 = Relationship(cat1,cat2)
        relationship2 = Relationship(cat2,cat1)
        relationship1.opposite_relationship = relationship2
        relationship2.opposite_relationship = relationship1
        cat1.relationships[cat2.ID] = relationship1
        cat2.relationships[cat1.ID] = relationship2

        # when
        relationship1.platonic_like = 100
        relationship2.platonic_like = 100

        # then
        self.assertFalse(relation_events.check_if_new_mate(relationship1,relationship2,cat1,cat2))

    def test_platonic_apprentice_mating(self):
        # given
        relation_events = Relation_Events()
        cat1 = Cat(moons=6)
        cat2 = Cat(moons=6)

        relationship1 = Relationship(cat1,cat2)
        relationship2 = Relationship(cat2,cat1)
        relationship1.opposite_relationship = relationship2
        relationship2.opposite_relationship = relationship1
        cat1.relationships[cat2.ID] = relationship1
        cat2.relationships[cat1.ID] = relationship2

        # when
        relationship1.platonic_like = 100
        relationship2.platonic_like = 100

        # then
        self.assertFalse(relation_events.check_if_new_mate(relationship1,relationship2,cat1,cat2))

    def test_romantic_kitten_mating(self):
        # given
        relation_events = Relation_Events()
        cat1 = Cat(moons=3)
        cat2 = Cat(moons=3)

        relationship1 = Relationship(cat1,cat2)
        relationship2 = Relationship(cat2,cat1)
        relationship1.opposite_relationship = relationship2
        relationship2.opposite_relationship = relationship1
        cat1.relationships[cat2.ID] = relationship1
        cat2.relationships[cat1.ID] = relationship2

        # when
        relationship1.romantic_love = 100
        relationship2.romantic_love = 100

        # then
        self.assertFalse(relation_events.check_if_new_mate(relationship1,relationship2,cat1,cat2))

    def test_romantic_apprentice_mating(self):
        # given
        relation_events = Relation_Events()
        cat1 = Cat(moons=6)
        cat2 = Cat(moons=6)

        relationship1 = Relationship(cat1,cat2)
        relationship2 = Relationship(cat2,cat1)
        relationship1.opposite_relationship = relationship2
        relationship2.opposite_relationship = relationship1
        cat1.relationships[cat2.ID] = relationship1
        cat2.relationships[cat1.ID] = relationship2

        # when
        relationship1.romantic_love = 100
        relationship2.romantic_love = 100

        # then
        self.assertFalse(relation_events.check_if_new_mate(relationship1,relationship2,cat1,cat2))
