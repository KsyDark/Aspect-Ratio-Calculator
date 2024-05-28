::Убиваем процесс программы
taskkill /f /im "Aspect Ratio Calculator.exe"
:: Запускает комплицию проекта с помощью pyinstaller
:: Предварительно установите кодировку - Кирилица OEM 866
pyinstaller --onefile --noconsole --icon=calc.ico "Aspect Ratio Calculator.py"
:: Запускаем программу после компиляции
cd dist
start "Aspect Ratio Calculator" "Aspect Ratio Calculator.exe"