from demoqa.models import app


def test_practice_form():

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