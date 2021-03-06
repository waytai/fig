from docker import Client
from fig.service import Service
import os
from unittest import TestCase


class DockerClientTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        if os.environ.get('DOCKER_URL'):
            cls.client = Client(os.environ['DOCKER_URL'])
        else:
            cls.client = Client()
        cls.client.pull('ubuntu')

    def setUp(self):
        for c in self.client.containers(all=True):
            self.client.kill(c['Id'])
            self.client.remove_container(c['Id'])

    def create_service(self, name, **kwargs):
        return Service(
            name=name,
            client=self.client,
            image="ubuntu",
            command=["/bin/sleep", "300"],
            **kwargs
        )



