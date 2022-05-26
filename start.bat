@ECHO OFF
ECHO =====================
ECHO CONVERTING .ui and .qrc FILES
ECHO .
ECHO .
ECHO .

pyuic5 -x ./ui/interface.ui -o ./ui/interface.py 
pyuic5 -x ./ui/timer.ui -o ./ui/timer.py 
pyuic5 -x ./ui/timer_bg.ui -o ./ui/timer_bg.py 
pyuic5 -x ./ui/todolist.ui -o ./ui/todolist.py 
pyuic5 -x ./ui/custom_list_item.ui -o ./ui/custom_list_item.py 

pyrcc5 icons.qrc -o icons_rc.py

ECHO App is starting up...
python ./main.py