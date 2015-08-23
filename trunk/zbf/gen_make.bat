@call ../set_path.bat
@rmdir build /Q /S
@mkdir build
@cd build
cmake .. -G "MinGW Makefiles"
@cd..

@call compile.bat