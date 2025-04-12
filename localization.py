"""
Bot uchun tillar lokalizatsiyasi (O'zbek va Rus tillari)
"""

TEXTS = {
    'uz': {
        'select_language': "🌐 <b>Tilni tanlang / Выберите язык:</b>",
        'language_selected': "✅ O'zbek tili tanlandi. Bot o'zbek tilida ishlamoqda.",
        'bot_welcome': "✨ <b>Quizmaster</b> - Word fayllardan quiz yaratuvchi bot!",
        'menu_placeholder': "Menyudan birini tanlang",
        'btn_create_quiz': "📝 Quiz yaratish",
        'btn_my_tests': "📚 Mening testlarim",
        'btn_results': "📊 Natijalarim",
        'btn_guide': "📖 Qo'llanma",
        'btn_feedback': "💬 Shikoyat/Takliflar",
        'btn_invite': "👥 Do'stlarni taklif qilish",
        'btn_admin_stats': "👤 Admin statistika",
        'btn_main_menu': "🏠 Bosh menyuga qaytish",
        'upload_file': """📄 Iltimos, test faylini yuboring (.docx yoki .txt formatda).

Format quyidagicha bo'lishi kerak:

Eski format (.docx fayllar uchun):
Question 1.
====
# to'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob
+++++
Question 2.
====
# to'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob

Yangi format (.txt fayllar uchun):
?Savol 1
+To'g'ri javob
-Noto'g'ri javob 1
-Noto'g'ri javob 2
-Noto'g'ri javob 3

?Savol 2
+To'g'ri javob
-Noto'g'ri javob 1
-Noto'g'ri javob 2
-Noto'g'ri javob 3""",
        'upload_word': """📄 .docx yoki .txt faylni yuboring.

Eski format (.docx fayllar uchun):
Question 1.
====
# to'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob
+++++
Question 2.
====
# to'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob
====
noto'g'ri javob

Yangi format (.txt fayllar uchun):
?Savol 1
+To'g'ri javob
-Noto'g'ri javob 1
-Noto'g'ri javob 2
-Noto'g'ri javob 3

?Savol 2
+To'g'ri javob
-Noto'g'ri javob 1
-Noto'g'ri javob 2
-Noto'g'ri javob 3""",
        'no_results': "📊 Siz hali hech qanday testda qatnashmadingiz!",
        'no_tests': "📚 Sizda hozircha testlar yo'q. Test yaratish uchun Word faylni yuboring.",
        'available_tests': "📚 <b>Mavjud testlaringiz:</b>",
        'test_not_found': "❌ Test topilmadi. Qaytadan urinib ko'ring.",
        'test_info': "<b>📝 Test: {name}</b>\n\n📊 <b>Malumot:</b>\n📚 Savollar soni: <code>{question_count}</code>\n📆 Yaratilgan vaqt: <code>{created_at}</code>\n\nNimani amalga oshirmoqchisiz?",
        'btn_start_test': "▶️ Testni boshlash",
        'btn_delete_test': "🗑️ Testni o'chirish",
        'btn_back': "🔙 Orqaga",
        'test_deleted': "✅ Test muvaffaqiyatli o'chirildi.",
        'test_delete_error': "❌ Testni o'chirishda xatolik yuz berdi.",
        'help_title': "<b>📌 BOT HAQIDA QO'LLANMA</b>",
        'help_text': """<b>1️⃣ Quiz yaratish:</b>
   • <b>📝 Fayl yuborish</b> - .docx yoki .txt formatdagi fayl yuboring
   • <b>🔢 Savol oralig'ini tanlash</b> - masalan "1-10"
   • <b>🔀 Savollarni aralashtirish</b> - ixtiyoriy
   • <b>🔄 Javoblarni aralashtirish</b> - ixtiyoriy
   
<b>2️⃣ Mening testlarim:</b>
   • <b>📚 Saqlangan testlarni ko'rish</b> - oldin yuborilgan testlar
   • <b>▶️ Testni boshlash</b> - saqlangan testni qayta ishlash
   • <b>🗑️ Testni o'chirish</b> - keraksiz testlarni o'chirish
   
<b>3️⃣ Natijalarim:</b>
   • <b>📊 Statistika ko'rish</b> - to'g'ri/noto'g'ri javoblar
   • <b>💯 Ballar</b> - 50/100 ballik tizimda

<b>💡 Fayl tuzilishi (eski format):</b>
• <i>Savol matni</i>
• <code>#To'g'ri javob</code> (# bilan boshlanadi)
• <i>Boshqa javoblar</i> (# belgisisiz)
• <code>++++</code> (Savollar orasiga qo'yiladi)

<b>💡 Fayl tuzilishi (yangi format):</b>
• <code>?Savol matni</code> (? bilan boshlanadi)
• <code>+To'g'ri javob</code> (+ bilan boshlanadi)
• <code>-Noto'g'ri javob</code> (- bilan boshlanadi)

<b>🔍 Misol (yangi format):</b>
?O'zbekiston poytaxti qayer?
+Toshkent
-Samarqand
-Buxoro
-Namangan

?1+1=?
+2
-3
-0
-4

<b>🤔 Muammolar bo'lsa, tugmasi orqali murojaat qiling.</b>""",
        'only_docx': "⚠️ Iltimos, faqat .docx formatdagi fayllarni yuboring!",
        'only_docx_txt': "⚠️ Iltimos, faqat .docx yoki .txt formatdagi fayllarni yuboring!",
        'no_questions_found': "❌ Faylda savollar topilmadi. Iltimos, to'g'ri formatdagi faylni yuklang.",
        'enter_test_name': "📝 Testga nom bering (masalan: 'Fizika', 'Matematika test 1', ...)",
        'enter_test_name_error': "⚠️ Iltimos, testga nom bering!",
        'test_saved': "✅ Test '{name}' muvaffaqiyatli saqlandi.\n📚 Jami {count} ta savol topildi.\n🔢 Qaysi oraliqdan savol berish kerak? (Masalan: 1-10)",
        'range_error': "⚠️ Noto'g'ri oraliq. 1 dan {count} gacha son kiriting.",
        'format_error': "⚠️ Noto'g'ri format. Masalan: 1-10",
        'select_question_order': "🔀 Savollar tartibini tanlang:",
        'btn_shuffle_questions': "🔄 Savollarni aralashtirish",
        'btn_sequential_questions': "📝 Ketma-ket savollar",
        'select_answer_order': "🔀 Javoblar tartibini tanlang:",
        'btn_shuffle_answers': "🔄 Javoblarni aralashtirish",
        'btn_sequential_answers': "📝 Ketma-ket javoblar",
        'quiz_starting': "🎯 Test boshlanmoqda...",
        'question': "📝 Savol {current}/{total}:",
        'quiz_finish_placeholder': "Test yakunlandi",
        'quiz_detailed_results': "<b>📊 Test natijalari:</b>\n\n<b>📝 Test: {name}</b>\n📆 Sana: {date}\n\n📚 <b>Natijalar:</b>\n✅ To'g'ri javoblar: <code>{correct}</code>\n❌ Noto'g'ri javoblar: <code>{wrong}</code>\n📊 Jami savollar: <code>{total}</code>\n\n📈 <b>Foiz:</b> <code>{percent}%</code>\n💯 <b>Ball:</b> <code>{points}</code>",
        'quiz_results_list_item': "<b>📝 {name}</b>\n📆 {date}\n📊 {percent}% ({correct}/{total})",
        'incorrect_file': "❌ Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.",
        'error_processing': "❌ Xatolik yuz berdi. Iltimos, faylni qayta yuboring.",
        'stats_title': "<b>📊 BOT STATISTIKASI 📊</b>",
        'stats_general': "<b>📈 Umumiy ma'lumotlar:</b>\n👥 Jami foydalanuvchilar: <code>{users_count}</code>\n📝 Jami yuklangan testlar: <code>{tests_count}</code>\n",
        'stats_users_title': "<b>👤 Foydalanuvchilar ro'yxati:</b>",
        'user_count': "Bot foydalanuvchilari soni: {count}",
        'test_file_forwarded': "👤 Yuqoridagi fayl {name} (@{username}) tomonidan yuborildi",
        'stop_info': "❗️ Testni to'xtatish uchun /stop buyrug'ini yuboring.",
        'test_stopped': "🛑 Test to'xtatildi!\n\n",
        'feedback_prompt': "💬 Iltimos, o'z fikr-mulohazalaringiz yoki takliflaringizni yuboring:",
        'feedback_sent': "✅ Fikr-mulohazangiz uchun rahmat! Xabaringiz adminga yuborildi.",
        'user_feedback': "💬 <b>Foydalanuvchi fikri:</b>\n{message}\n\n<b>Yuboruvchi:</b> {name} (@{username})",
        'invite_friends': "<b>👥 Do'stlaringizni taklif qiling!</b>\n\nBotimizni do'stlaringizga ulashing va ular bilan birga bilimlaringizni sinab ko'ring! Quyidagi havolani do'stlaringizga yuboring:",
        'your_invite_link': "🔗 <b>Sizning taklif havolangiz</b>:\n{link}",
        'need_invite_friend': "👋 Xush kelibsiz! Botdan foydalanish uchun, iltimos kamida bitta do'stingizni taklif qiling. Bu bizning botimizni rivojlantirishga yordam beradi.",
        'referral_success': "👍 Rahmat! Do'stingiz botga qo'shildi. Endi siz botdan to'liq foydalanishingiz mumkin.\n Botni oshga tushirish uchun /start buyrug'ini jo'nating",
        'already_invited': "✅ Siz allaqachon do'stlaringizni taklif qilib bo'lgansiz. Botdan foydalanishingiz mumkin!",
        'video_guide_caption': "📹 Botdan foydalanish bo'yicha video qo'llanma",
        'video_guide_error': "⚠️ Video qo'llanmani yuborishda xatolik yuz berdi. Iltimos, keyinroq qayta urinib ko'ring.",
        'btn_broadcast': "📣 Xabar tarqatish",
        'broadcast_title': "<b>📣 XABAR TARQATISH</b>",
        'broadcast_select_type': "Qanday turdagi xabar yubormoqchisiz?",
        'broadcast_type_text': "📝 Matn xabar",
        'broadcast_type_photo': "🖼 Rasm",
        'broadcast_type_video': "📹 Video",
        'broadcast_type_poll': "📊 So'rovnoma",
        'broadcast_send_text': "Tarqatmoqchi bo'lgan matn xabarni kiriting:",
        'broadcast_send_photo': "Tarqatmoqchi bo'lgan rasmni yuboring:",
        'broadcast_send_video': "Tarqatmoqchi bo'lgan videoni yuboring:",
        'broadcast_send_poll': "So'rovnoma savolini kiriting:",
        'broadcast_poll_options': "So'rovnoma variantlarini har birini yangi qatorda kiriting (kamida 2 ta variant bo'lishi kerak):",
        'broadcast_confirm': "Xabar {users_count} ta foydalanuvchiga yuboriladi. Tasdiqlaysizmi?",
        'broadcast_confirm_yes': "✅ Ha, yuborish",
        'broadcast_confirm_no': "❌ Yo'q, bekor qilish",
        'broadcast_completed': "✅ Xabar muvaffaqiyatli {success_count} ta foydalanuvchiga yuborildi.\n❌ {failed_count} ta foydalanuvchiga yuborib bo'lmadi.",
        'broadcast_canceled': "❌ Xabar tarqatish bekor qilindi."
    },
    'ru': {
        'select_language': "🌐 <b>Tilni tanlang / Выберите язык:</b>",
        'language_selected': "✅ Русский язык выбран. Бот работает на русском языке.",
        'bot_welcome': "✨ <b>Quizmaster</b> - бот для создания викторин из файлов Word!",
        'menu_placeholder': "Выберите пункт меню",
        'btn_create_quiz': "📝 Создать викторину",
        'btn_my_tests': "📚 Мои тесты",
        'btn_results': "📊 Мои результаты",
        'btn_guide': "📖 Руководство",
        'btn_feedback': "💬 Жалобы/Предложения",
        'btn_invite': "👥 Пригласить друзей",
        'btn_admin_stats': "👤 Статистика админа",
        'btn_main_menu': "🏠 Вернуться в главное меню",
        'upload_file': """📄 Пожалуйста, загрузите тестовый файл (в формате .docx или .txt).

Формат должен быть следующим:

Старый формат (для файлов .docx):
Question 1.
====
# правильный ответ
====
неправильный ответ
====
неправильный ответ
====
неправильный ответ
+++++
Question 2.
====
# правильный ответ
====
неправильный ответ
====
неправильный ответ
====
неправильный ответ

Новый формат (для файлов .txt):
?Вопрос 1
+Правильный ответ
-Неправильный ответ 1
-Неправильный ответ 2
-Неправильный ответ 3

?Вопрос 2
+Правильный ответ
-Неправильный ответ 1
-Неправильный ответ 2
-Неправильный ответ 3""",
        'upload_word': """📄 Загрузите файл .docx или .txt.

Старый формат (для файлов .docx):
Question 1.
====
# правильный ответ
====
неправильный ответ
====
неправильный ответ
====
неправильный ответ
+++++
Question 2.
====
# правильный ответ
====
неправильный ответ
====
неправильный ответ
====
неправильный ответ

Новый формат (для файлов .txt):
?Вопрос 1
+Правильный ответ
-Неправильный ответ 1
-Неправильный ответ 2
-Неправильный ответ 3

?Вопрос 2
+Правильный ответ
-Неправильный ответ 1
-Неправильный ответ 2
-Неправильный ответ 3""",
        'no_results': "📊 Вы еще не участвовали ни в одном тесте!",
        'no_tests': "📚 У вас пока нет тестов. Отправьте файл Word, чтобы создать тест.",
        'available_tests': "📚 <b>Ваши доступные тесты:</b>",
        'test_not_found': "❌ Тест не найден. Пожалуйста, попробуйте снова.",
        'test_info': "<b>📝 Тест: {name}</b>\n\n📊 <b>Информация:</b>\n📚 Количество вопросов: <code>{question_count}</code>\n📆 Дата создания: <code>{created_at}</code>\n\nЧто вы хотите сделать?",
        'btn_start_test': "▶️ Начать тест",
        'btn_delete_test': "🗑️ Удалить тест",
        'btn_back': "🔙 Назад",
        'test_deleted': "✅ Тест успешно удален.",
        'test_delete_error': "❌ Ошибка при удалении теста.",
        'help_title': "<b>📌 РУКОВОДСТВО ПО БОТУ</b>",
        'help_text': """<b>1️⃣ Создание викторины:</b>
   • <b>📝 Загрузка файла</b> - загрузите файл в формате .docx или .txt
   • <b>🔢 Выбор диапазона вопросов</b> - например "1-10"
   • <b>🔀 Перемешивание вопросов</b> - по желанию
   • <b>🔄 Перемешивание ответов</b> - по желанию
   
<b>2️⃣ Мои тесты:</b>
   • <b>📚 Просмотр сохраненных тестов</b> - ранее загруженные тесты
   • <b>▶️ Начать тест</b> - повторно решить сохраненный тест
   • <b>🗑️ Удалить тест</b> - удалить ненужные тесты
   
<b>3️⃣ Мои результаты:</b>
   • <b>📊 Просмотр статистики</b> - правильные/неправильные ответы
   • <b>💯 Баллы</b> - в 50/100-бальной системе

<b>💡 Структура файла (старый формат):</b>
• <i>Текст вопроса</i>
• <code>#Правильный ответ</code> (начинается с #)
• <i>Другие ответы</i> (без символа #)
• <code>++++</code> (Разделитель между вопросами)

<b>💡 Структура файла (новый формат):</b>
• <code>?Текст вопроса</code> (начинается с ?)
• <code>+Правильный ответ</code> (начинается с +)
• <code>-Неправильный ответ</code> (начинается с -)

<b>🔍 Пример (новый формат):</b>
?Столица Узбекистана?
+Ташкент
-Самарканд
-Бухара
-Наманган

?1+1=?
+2
-3
-0
-4

<b>🤔 Если у вас возникли проблемы, обратитесь через кнопку.</b>""",
        'only_docx': "⚠️ Пожалуйста, отправляйте только файлы в формате .docx!",
        'only_docx_txt': "⚠️ Пожалуйста, отправляйте только файлы в формате .docx или .txt!",
        'no_questions_found': "❌ В файле не найдены вопросы. Пожалуйста, загрузите файл в правильном формате.",
        'enter_test_name': "📝 Назовите тест (например: 'Физика', 'Математика тест 1', ...)",
        'enter_test_name_error': "⚠️ Пожалуйста, укажите название теста!",
        'test_saved': "✅ Тест '{name}' успешно сохранен.\n📚 Всего найдено {count} вопросов.\n🔢 Укажите диапазон вопросов (Например: 1-10)",
        'range_error': "⚠️ Неверный диапазон. Введите число от 1 до {count}.",
        'format_error': "⚠️ Неверный формат. Например: 1-10",
        'select_question_order': "🔀 Выберите порядок вопросов:",
        'btn_shuffle_questions': "🔄 Перемешать вопросы",
        'btn_sequential_questions': "📝 Последовательные вопросы",
        'select_answer_order': "🔀 Выберите порядок ответов:",
        'btn_shuffle_answers': "🔄 Перемешать ответы",
        'btn_sequential_answers': "📝 Последовательные ответы",
        'quiz_starting': "🎯 Тест начинается...",
        'question': "📝 Вопрос {current}/{total}:",
        'quiz_finish_placeholder': "Тест завершен",
        'quiz_detailed_results': "<b>📊 Результаты теста:</b>\n\n<b>📝 Тест: {name}</b>\n📆 Дата: {date}\n\n📚 <b>Результаты:</b>\n✅ Правильные ответы: <code>{correct}</code>\n❌ Неправильные ответы: <code>{wrong}</code>\n📊 Всего вопросов: <code>{total}</code>\n\n📈 <b>Процент:</b> <code>{percent}%</code>\n💯 <b>Баллы:</b> <code>{points}</code>",
        'quiz_results_list_item': "<b>📝 {name}</b>\n📆 {date}\n📊 {percent}% ({correct}/{total})",
        'incorrect_file': "❌ Произошла ошибка. Пожалуйста, попробуйте еще раз.",
        'error_processing': "❌ Произошла ошибка. Пожалуйста, загрузите файл снова.",
        'stats_title': "<b>📊 СТАТИСТИКА БОТА 📊</b>",
        'stats_general': "<b>📈 Общая информация:</b>\n👥 Всего пользователей: <code>{users_count}</code>\n📝 Всего загруженных тестов: <code>{tests_count}</code>\n",
        'stats_users_title': "<b>👤 Список пользователей:</b>",
        'user_count': "Количество пользователей бота: {count}",
        'test_file_forwarded': "👤 Вышеуказанный файл был отправлен пользователем {name} (@{username})",
        'stop_info': "❗️ Чтобы остановить тест, отправьте команду /stop.",
        'test_stopped': "🛑 Тест остановлен!\n\n",
        'feedback_prompt': "💬 Пожалуйста, отправьте свои отзывы или предложения:",
        'feedback_sent': "✅ Спасибо за ваш отзыв! Ваше сообщение было отправлено администратору.",
        'user_feedback': "💬 <b>Отзыв пользователя:</b>\n{message}\n\n<b>Отправитель:</b> {name} (@{username})",
        'invite_friends': "<b>👥 Пригласите своих друзей!</b>\n\nПоделитесь нашим ботом с друзьями и проверяйте знания вместе! Отправьте друзьям следующую ссылку:",
        'your_invite_link': "🔗 <b>Ваша ссылка для приглашения</b>:\n{link}",
        'need_invite_friend': "👋 Добро пожаловать! Чтобы использовать бота, пожалуйста, пригласите хотя бы одного друга. Это поможет развитию нашего бота.",
        'referral_success': "👍 Спасибо! Ваш друг присоединился к боту. Теперь вы можете полноценно использовать бота.",
        'already_invited': "✅ Вы уже пригласили своих друзей. Вы можете использовать бота!",
        'video_guide_caption': "📹 Видеоруководство по использованию бота",
        'video_guide_error': "⚠️ Произошла ошибка при отправке видеоруководства. Пожалуйста, попробуйте позже.",
        'btn_broadcast': "📣 Рассылка сообщений",
        'broadcast_title': "<b>📣 РАССЫЛКА СООБЩЕНИЙ</b>",
        'broadcast_select_type': "Какой тип сообщения вы хотите отправить?",
        'broadcast_type_text': "📝 Текстовое сообщение",
        'broadcast_type_photo': "🖼 Фото",
        'broadcast_type_video': "📹 Видео",
        'broadcast_type_poll': "📊 Опрос",
        'broadcast_send_text': "Введите текстовое сообщение, которое хотите разослать:",
        'broadcast_send_photo': "Отправьте фото, которое хотите разослать:",
        'broadcast_send_video': "Отправьте видео, которое хотите разослать:",
        'broadcast_send_poll': "Введите вопрос для опроса:",
        'broadcast_poll_options': "Введите варианты ответов, каждый с новой строки (минимум 2 варианта):",
        'broadcast_confirm': "Сообщение будет отправлено {users_count} пользователям. Подтверждаете?",
        'broadcast_confirm_yes': "✅ Да, отправить",
        'broadcast_confirm_no': "❌ Нет, отменить",
        'broadcast_completed': "✅ Сообщение успешно отправлено {success_count} пользователям.\n❌ Не удалось отправить {failed_count} пользователям.",
        'broadcast_canceled': "❌ Рассылка отменена."
    }
}

def get_text(lang, key):
    """Berilgan til uchun matnni qaytaradi"""
    if lang not in TEXTS:
        lang = 'uz'  # Default til
    
    return TEXTS[lang].get(key, TEXTS['uz'].get(key, f"TEXT_{key}"))