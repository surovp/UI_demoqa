from demoqa.models import app


def test_fill_full_form():

    app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    app.registration_form\
        .fill_first_name("Ivan")\
        .fill_last_name("Ivanov")\
        .fill_email("user123@test.com")\
        .set_gender("Other")\
        .fill_mobile_phone("7904111222")\
        .set_date_birthday("25 January,1997")\
        .fill_subjects(("English","Economics"))\
        .set_hobbies("Sports")\
        .download_file('file_test.jpg')\
        .fill_current_adress("Russia,Moscow")\
        .set_state("Haryana")\
        .set_city("Karnal")\
        .submit()

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


def test_fill_only_required_fields():
    app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    app.registration_form\
        .fill_first_name("Elena")\
        .fill_last_name("Andreeva")\
        .set_gender("Female")\
        .fill_mobile_phone("9876543210")\
        .submit()

    app.registration_form\
        .check_data("Elena")\
        .check_data("Andreeva")\
        .check_data("Female")\
        .check_data("9876543210")\


def test_submit_empty_form():
    app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    app.registration_form.submit()

    app.registration_form\
        .check_validation_first_name()\
        .check_validation_last_name()\
        .check_validation_gender()\
        .check_validation_phone_number()


def test_validation_count_numbers_less_than_ten():
    app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    app.registration_form\
        .fill_first_name("Ivan")\
        .fill_last_name("Ivanov")\
        .set_gender("Male")\
        .fill_mobile_phone("123456789")\
        .submit()

    app.registration_form.check_validation_phone_number()


def test_validation_field_email():
    app.registration_form.open_page("https://demoqa.com/automation-practice-form")

    app.registration_form\
        .fill_first_name("Andrew")\
        .fill_last_name("Ivanov")\
        .set_gender("Male")\
        .fill_mobile_phone("123456789")\
        .fill_email("user123.ru")\
        .submit()

    app.registration_form.check_validation_email()
