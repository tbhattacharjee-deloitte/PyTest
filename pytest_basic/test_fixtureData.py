import pytest
from BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestDataLoad(BaseClass):
    def test_accessData(self, dataLoad):
        # since dataLoad is returning data, it must be passed as parameter
        logger = self.get_logger()
        logger.debug(dataLoad)
        print(dataLoad)

    def test_crossBrowser(self, cross_browser):
        logger = self.get_logger()
        logger.debug(cross_browser)
        print(cross_browser)
