::������� ����� �ணࠬ��
taskkill /f /im "Aspect Ratio Calculator.exe"
:: ����᪠�� �������� �஥�� � ������� pyinstaller
:: �।���⥫쭮 ��⠭���� ����஢�� - ��ਫ�� OEM 866
pyinstaller --onefile --noconsole --icon=calc.ico "Aspect Ratio Calculator.py"
:: ����᪠�� �ணࠬ�� ��᫥ �������樨
cd dist
start "Aspect Ratio Calculator" "Aspect Ratio Calculator.exe"