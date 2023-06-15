python -m pytest -vsm sanity --html=./Reports/testloginchrome.html D:\Project\SeleniumHandsonProject\TestCases --browser chrome
python -m pytest -vsm regression --html=./Reports/testloginchromeheadless.html D:\Project\SeleniumHandsonProject\TestCases --browser chromeheadless
python -m pytest -vsm sanity --html=./Reports/testloginedge.html D:\Project\SeleniumHandsonProject\TestCases --browser edge
python -m pytest -vsm regression --html=./Reports/testloginedgeheadless.html D:\Project\SeleniumHandsonProject\TestCases --browser edgeheadless
