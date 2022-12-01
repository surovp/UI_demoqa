from selene.support.shared import browser
from selene import have
from demoqa.utils.selene import command

ads = browser.all('[id^=google_ads][id$=container__]')


def remove_ads(*, amount, timeout):
    if ads.with_(timeout=timeout).wait.until(have.size_greater_than_or_equal(amount)):
        ads.perform(command.js.remove)
