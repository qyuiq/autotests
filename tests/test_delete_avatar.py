from pages.main_page import MainPage

def test_delete_avatar(chrome_driver):

    # Открытие главной страницы
    main_page = MainPage(chrome_driver).open_web()

    # Нажатие кнопки 'Посмотреть пример аккаунта'
    demo_account_page = main_page.click_demo_acc_button()

    # Нажатие кнопки 'Настройки'
    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    settings_page = demo_account_page.click_demo_settings()

    # Нажатие кнопки 'Удалить' аватар
    settings_page.click_delete_avatar_button()

    # Ожидание появления popup
    popup = settings_page.wait_for_sandbox_popup()

    # Проверка текста в popup
    popup_text = settings_page.text_in_sandbox_popup()

    assert popup.is_displayed(), "Popup не отображается"
    assert popup_text is not None, "Текст в popup отсутствует"
    print(f"Текст в popup: {popup_text}")