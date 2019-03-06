from unittest import TestCase

from mvn_pack import Mvn_Pack


class TestMvn_Pack(TestCase):
    def test_gen_import(self):
        Mvn_Pack().gen_import('H:\\intelljProjects\\bli-ck2\\target\\dependency\\*.pom')
        self.assertTrue(True)

    # def test_gen_export(self):
    #     Mvn_Pack().gen_export()
    #     self.assertTrue(True)
