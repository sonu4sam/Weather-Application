import os
from selenium import webdriver


class Request:
    def __init__(self) -> None:
        self._phantomjs_path = os.path.join(os.curdir, 'phantomjs/bin/phantomjs')
        self._driver = webdriver.PhantomJS(self._phantomjs_path)
        self._base_url = base_url
        self._driver = webdriver.PhantomJS(self._phantomjs_path)
        
        
    def fetch_data(self, forecast):
        url = self._base_url.format(forecast.value)
        self._driver.get(url)
        
        if self._driver.title == '404 Not Found':
            error_message = ('Could not find the city {}'
                             'Please check your spelling and try again.')
            raise Exception(error_message)
        
        return self._driver.page_source
    