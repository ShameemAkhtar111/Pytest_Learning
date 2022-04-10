import sys


sys.path.append("D:\\Shameem\\SeleniumPython\\Pytest_Learning")
sys.path.append("D:\\Shameem\\SeleniumPython\\Pytest_Learning\\webTest_Pytest")
print(sys.path)
from Utils.ConfigReader import ConfigReader
print(ConfigReader().get_url())

