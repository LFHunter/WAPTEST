from Baselib.ui_lib import UILib
from Baselib.file_lib import *
from Twitch_Proj import twitch_locators as tlocator
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from logging import Logger
import time


class TwitchPage(UILib):
    def __init__(self, twitch_url: str, driver: webdriver, logger: Logger):
        super().__init__(driver, logger)
        self.logger_msg = "=====[{msg}]====={self.driver}"
        self.twitch_url = twitch_url
        self.driver.set_page_load_timeout(45)

    def get_twitch_page(self):
        try:
            self.driver.get(self.twitch_url)
            self.logger.debug(f"Successfully get {self.twitch_url}")
        except Exception as exp:
            self.logger.debug(f"Exception:{exp}")
            self.logger.debug(f"get {self.twitch_url} again")
            self.driver.get(self.twitch_url)
        # self.wait_ele_visible(wa_locator.H1_warranty_intro, 5)

    def click_browse_icon(self):
        self.click(tlocator.DIV_browse_icon)

    def input_text_in_searchbar(self, msg: str):
        self.send_keys(tlocator.INPUT_search_bar, msg=msg)

    def send_enter(self):
        self.send_keys(tlocator.INPUT_search_bar,
                       msg=Keys.ENTER, need_check=False)

    def click_streamer_in_top(self, streamer_order: int):
        streamers = [tlocator.streamer1_within_channels_in_top_page,
                     tlocator.streamer2_within_channels_in_top_page,
                     tlocator.streamer3_within_channels_in_top_page]
        self.click(streamers[streamer_order+1])

    def check_streamer_page_is_loaded(self, timeout: int = 10):
        document_ready_state = self.driver.execute_script(
            "return document.readyState")
        self.logger.debug(f"Current url : {self.driver.current_url}")
        if document_ready_state == "complete":
            self.click(tlocator.SPAN_chatroom)
            video_element = self.wait_ele_visible(
                tlocator.VIDEO_element, timeout=timeout)
            # video.readyState = 4 in  HTML5 中 means have enough data to play,
            ready_state = self.driver.execute_script(
                "return arguments[0].readyState;", video_element)
            paused = self.driver.execute_script(
                "return arguments[0].paused;", video_element)

            if ready_state == 4 and not paused:
                self.logger.debug("The video is playing (or ready to play).")
                return True
            else:
                self.logger.debug(
                    "The video is not fully loaded or is paused.")
        self.logger.debug("The website is not ready")

    def wait_streamer_page_is_ready(self, timeout: int = 20):
        n = 0
        while n <= timeout/10:
            n += 1
            if self.check_streamer_page_is_loaded():
                break
            time.sleep(10)
        write_txt_file("page.html", self.driver.page_source)

    def accept_modal(self):
        try:
            ele = self.wait_ele_visible(tlocator.Text_modal)
            self.logger.debug(f"Modal text:{ele.text}")
            return True
        except:
            self.logger.debug("No modal show")

    def click_accept_modal(self):
        self.click(tlocator.BUTTON_modal_accept)

    def take_twitch_screenshot(self, filename: str):
        self.take_screenshot(filename)
