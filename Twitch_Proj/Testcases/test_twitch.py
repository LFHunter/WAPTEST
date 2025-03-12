from Baselib.webdriver_manager import WebDriverManager
from Twitch_Proj.twitch_page import TwitchPage
from Twitch_Proj.config import driver_setting, \
    current_folder_name, twitch_url, chrome_driver_path
import time
import logging


class TestTwitch:

    logger = logging.getLogger(__name__)

    @classmethod
    def setup_class(cls):
        cls.logger.info("Initial Test")
        cls.wda = WebDriverManager(
            driver_setting, driver_path=chrome_driver_path)
        cls.driver = cls.wda.driver
        cls.testpage = TwitchPage(twitch_url, cls.driver, cls.logger)
        cls.logger.info(f"generate TwitchPage")

    @classmethod
    def teardown_class(cls):
        time.sleep(10)
        cls.wda.close_driver()
        cls.logger.info("End Test")

    def setup_method(self, method):
        self.logger.info(f"----starting {method.__name__} execution----")

    def teardown_method(self, method):
        self.logger.info(f"----end {method.__name__} execution----")

    def test_1_go_to_twitch(self):
        self.testpage.get_twitch_page()

    def test_2_click_search_icon(self):
        self.testpage.click_browse_icon()

    def test_3_input_message_in_search_bar(self):
        self.testpage.input_text_in_searchbar(msg="StarCraft II")
        self.testpage.send_enter()

    def test_4_scroll_down_2_times(self):
        for _ in range(2):
            self.testpage.scroll_down(movepixels=800, wait_time=0)
        time.sleep(2)

    def test_5_select_one_streamer(self):
        if self.testpage.accept_modal():
            self.testpage.take_screenshot(
                f"{current_folder_name}/modal.png")
            self.testpage.click_accept_modal()
        self.testpage.click_streamer_in_top(1)

    def test_6_check_and_take_photo_the_streamer_page(self):
        self.testpage.wait_streamer_page_is_ready(timeout=20)
        self.testpage.take_screenshot(
            f"{current_folder_name}/StarCraftII_streamer.png")
