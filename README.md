## Проект UI автотестов demoqa.com

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo_stacks/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo_stacks/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo_stacks/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo_stacks/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo_stacks/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo_stacks/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo_stacks/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo_stacks/tg.png"></code>
</p>

### Что проверяем
* Отправка формы и проверка данных всей заполненной формы
* Отправка формы и проверка данных только с заполнением главных полей
* Отправка пустой формы
* Валидация поля номера телефона
* Валидация поля Email

### Запуск проекта в jenkins
##### <img width="2%" title="Jenkins" src="images/logo_stacks/jenkins.png"> [Jenkins](https://jenkins.autotests.cloud/job/UI_demoqa_qa_guru_python_2/)
##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](images/screenshots/jenkins.png)


### Allure report
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshots/allure_suites.png)

##### Видео прохождение теста
![This is an image](images/screenshots/tests_ui.gif)


### Интеграция с Allure TestOps
##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshots/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграю с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshots/allure_testops_suites.png)


### Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/jira.png)


### Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/tg_bot.png)
