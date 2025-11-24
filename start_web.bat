@echo off
chcp 65001 >nul
echo ===================================
echo 台北市交通監控系統 - Web 版本
echo ===================================
echo.
echo 正在啟動 Flask 後端服務...
echo.

cd backend
python app.py

pause
