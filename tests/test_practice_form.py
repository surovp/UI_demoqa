from demoqa.models import app
import allure


def test_fill_full_form(setup_browser):

    with allure.step("open browser"):
        app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    with allure.step("fill all fields"):
        app.registration_form\
            .fill_first_name("Ivan")\
            .fill_last_name("Ivanov")\
            .fill_email("user123@test.com")\
            .set_gender("Other")\
            .fill_mobile_phone("7904111222")\
            .set_date_birthday()\
            .fill_subjects(("English","Economics"))\
            .set_hobbies("Sports")\
            .download_file('file_test.jpg')\
            .fill_current_adress("Russia,Moscow")\
            .set_state("Haryana")\
            .set_city("Karnal")\
            .submit()

    with allure.step("check all information about user"):
        app.registration_form\
            .check_data("Ivan")\
            .check_data("Ivanov")\
            .check_data("user123@test.com")\
            .check_data("Other")\
            .check_data("7904111222")\
            .check_data("25 January,1997") \
            .check_data("English, Economics")\
            .check_data("Sports")\
            .check_data("Russia,Moscow")\
            .check_data("Haryana")\
            .check_data("Karnal")


def test_fill_only_required_fields(setup_browser):

    with allure.step("open browser"):
        app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    with allure.step("fill main fields"):
        app.registration_form\
            .fill_first_name("Elena")\
            .fill_last_name("Andreeva")\
            .set_gender("Female")\
            .fill_mobile_phone("9876543210")\
            .submit()

    with allure.step("check the filled data"):
        app.registration_form\
            .check_data("Elena")\
            .check_data("Andreeva")\
            .check_data("Female")\
            .check_data("9876543210")\


def test_submit_empty_form(setup_browser):

    with allure.step("open browser"):
        app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    with allure.step("submit empty form"):
        app.registration_form.submit()

    with allure.step("check validation"):
        app.registration_form\
            .check_validation_first_name()\
            .check_validation_last_name()\
            .check_validation_gender()\
            .check_validation_phone_number()


def test_validation_count_numbers_less_than_ten(setup_browser):

    with allure.step("open browser"):
        app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    with allure.step("fill main fields and 9x number phone"):
        app.registration_form\
            .fill_first_name("Ivan")\
            .fill_last_name("Ivanov")\
            .set_gender("Male")\
            .fill_mobile_phone("123456789")\
            .submit()

    with allure.step("check validation field"):
        app.registration_form.check_validation_phone_number()


def test_validation_field_email(setup_browser):

    with allure.step("open browser"):
        app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    with allure.step("fill main fields and email without @"):
        app.registration_form\
            .fill_first_name("Andrew")\
            .fill_last_name("Ivanov")\
            .set_gender("Male")\
            .fill_mobile_phone("123456789")\
            .fill_email("user123.ru")\
            .submit()

    with allure.step("check validation field email"):
        app.registration_form.check_validation_email()
