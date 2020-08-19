@echo off
if defined WINPYDIRBASE (
    call %WINPYDIRBASE%\scripts\env.bat
    @echo ==============================================================================
    @echo:
    @echo Using WinPython from %WINPYDIRBASE%
    @echo:
    @echo ==============================================================================
    @echo:
    )
del MANIFEST
rmdir /S /Q build
rmdir /S /Q dist
set PYTHONPATH=%cd%
python setup.py build bdist_wheel --universal
@echo:
@echo ==============================================================================
choice /t 5 /c yn /cs /d n /m "Do you want to upload packages to PyPI (y/n)?"
if errorlevel 2 goto :no
if errorlevel 1 goto :yes
:yes
@echo ==============================================================================
@echo:
twine upload dist/*
GOTO :continue
:no
@echo:
@echo Warning: Packages were not uploaded to PyPI
:continue
@echo:
@echo ==============================================================================
@echo:
@echo End of script
pause