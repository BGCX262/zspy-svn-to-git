@call ../set_path.bat
@cd build
mingw32-make
@cd ..
@move /Y libcn_word.dll cn_word.pyd 
@echo.
@echo.
