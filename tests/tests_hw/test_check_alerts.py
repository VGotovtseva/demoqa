import time

from pages.alerts import Alerts


def test_check_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    assert alert_page.btn_timer_alert.exist()
    alert_page.btn_timer_alert.click()
    for i in range(4):
        time.sleep(1)
        assert not alert_page.alert()
    time.sleep(1)
    assert alert_page.alert()

   # times_temp = 0 решение с помощью бесконечного цикла
   # while True:
   #     time.sleep(1)
   #     times_temp += 1
   #     if times_temp == 5:
   #        assert alert_page.alert()
   #         break
   #     else:
   #         assert not alert_page.alert()
