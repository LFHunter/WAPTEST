from selenium.webdriver.common.by import By

DIV_browse_icon = (By.XPATH, "//div[text()='Browse'][1]")
INPUT_search_bar = (By.XPATH, "//input[@type='search'][1]")
VIDEO_element = (By.XPATH, "//video")


BUTTON_modal_accept = (By.XPATH, "\\button[@data-a-target=\
                       'content-classification-gate-overlay-start-watching-button'][1]")
#modal check string
Text_modal = (By.XPATH,"//p[contains(text(),'appropriate for you to watch')][1]")

SPAN_chatroom = (By.XPATH,"//span[text()='Welcome to the chat room!'][1]")
#now, only 3 streamers in top (in CHANNELS)
streamer1_within_channels_in_top_page = (By.XPATH, "//h2[text()='CHANNELS'][1]/../../div[2]/button")
streamer2_within_channels_in_top_page =  (By.XPATH, "//h2[text()='CHANNELS'][1]/../../div[3]/button")
streamer3_within_channels_in_top_page =  (By.XPATH, "//h2[text()='CHANNELS'][1]/../../div[4]/button")


