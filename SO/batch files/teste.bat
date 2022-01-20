@echo off
md teste
cd teste
md info 
cd info
rem systeminfo > info.txt
pip list > modulos_py.txt
md rede 
cd rede
ipconfig /all >rede.txt
cd ..
cd ..
md python 
cd python 
md web
md mobile
md gaming 
md desktop
cd web
md flask
md django 
cd ..\..
tree /a /f > tree.txt
rem isto é um comentario
pause
