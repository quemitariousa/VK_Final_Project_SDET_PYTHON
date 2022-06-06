# VK_FP_sdet_python



## Баги
### API
- test_auth_invalid_login: При некорректном логине отдает 401 
- test_auth_non_exist_user: При логине несуществующего юзера отдает 200
- test_correct_new_user_with_mn: При создании сущности отдает 210
- test_correct_username_new_user_without_mn: Сущность без middlename не создана, отдает 401
- test_incorrect_username_new_user: При невалидных значениях отдает 500
- test_incorrect_pw_new_user: При значении None отдает 210 
- test_incorrect_email_new_user: При слишком коротком значении в поле email отдает 210, должен как минимум ругаться на отсутстиве собаки
- test_correct_change_pw_user: При корректной смене пароля отдает 204


### UI
- test_python_button: При нажатии на python перекидывает на начальный экран
- test_navbar: centos ведет на fedora
- test_correct_user_with_mn: При любом middlename отдает NULL в нем
- test_incorrect_long_username: При большом значении обрезается username 
- test_incorrect_name: Отсутствует лимит на значения, сущности создаются
- test_empty_name_beautifull_warn: Internal Server Error при регистрации с пустым name
