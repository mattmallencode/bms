from unittest import TestCase
from ms_modules import metrics
import config

class TestHealthModule(TestCase):

    def test_adjust_lifespan(self):
        """
        Tests the adjust_lifespan function of the health module.

        We pass a "dif_in_soc" of 50000, as this would equate to 500 charge cycles, which should result in 20% battery degradation i.e. lifespan being reduced to 80%.
        """
        metrics.adjust_lifespan(50000)
        self.assertEqual(config.lifespan, 0.8)