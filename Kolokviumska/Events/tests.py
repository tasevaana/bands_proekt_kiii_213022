# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Band, Event, EventBand
from datetime import date


class BandTestCase(TestCase):
    def setUp(self):
        self.band = Band.objects.create(name="The Rockers", country="USA", year=1990, numOfEvents=100)

    def test_band_creation(self):
        self.assertEqual(self.band.name, "The Rockers")
        self.assertEqual(self.band.country, "USA")
        self.assertEqual(self.band.year, 1990)
        self.assertEqual(self.band.numOfEvents, 100)

    def test_band_str_method(self):
        self.assertEqual(str(self.band), "The Rockers USA")


class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        self.event = Event.objects.create(
            name="Music Festival",
            date=date(2025, 5, 1),
            poster="path/to/poster.jpg",
            user=self.user,
            isOpen=True
        )

    def test_event_creation(self):
        self.assertEqual(self.event.name, "Music Festival")
        self.assertEqual(self.event.date, date(2025, 5, 1))
        self.assertEqual(self.event.user.username, "testuser")
        self.assertTrue(self.event.isOpen)

    def test_event_str_method(self):
        self.assertEqual(str(self.event), "Music Festival 2025-05-01")


class EventBandTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.band = Band.objects.create(name="The Rockers", country="USA", year=1990, numOfEvents=100)
        self.event = Event.objects.create(
            name="Music Festival",
            date=date(2025, 5, 1),
            poster="path/to/poster.jpg",
            user=self.user,
            isOpen=True
        )
        
        self.event_band = EventBand.objects.create(event=self.event, band=self.band)

    def test_event_band_creation(self):
        self.assertEqual(self.event_band.event.name, "Music Festival")
        self.assertEqual(self.event_band.band.name, "The Rockers")

    def test_event_band_str_method(self):
        self.assertEqual(str(self.event_band), "Music Festival The Rockers")
