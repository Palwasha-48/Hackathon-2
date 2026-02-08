@echo off
echo ========================================================
echo        HUGGING FACE DEPLOYMENT (Palwasha-49)
echo ========================================================

:: 1. Navigate to the parent directory (outside the project folder)
cd ..

:: 2. Configuration
set /p HF_TOKEN="Your api key"
set HF_USERNAME=Palwasha-49
set SPACE_NAME=Hackathon-II

:: 3. Clean up previous attempts (if any)
if exist hf_deploy_palwasha (
    echo Cleaning up old temp folder...
    rmdir /s /q hf_deploy_palwasha
)

:: 4. Clone the Hugging Face Space using the token for automation
echo.
echo [1/4] Downloading your Space (%HF_USERNAME%/%SPACE_NAME%)...
git clone https://%HF_USERNAME%:%HF_TOKEN%@huggingface.co/spaces/%HF_USERNAME%/%SPACE_NAME% hf_deploy_palwasha



:: 4. Copy the backend files from the current project
echo.
echo [2/4] Copying Phase 2 Backend files...
:: Note: specific path based on your project structure
xcopy "Hackathon-2\Phase-2\backend\*" "hf_deploy_palwasha\" /E /Y /Q

:: 5. Navigate into the deployment folder
cd hf_deploy_palwasha

echo.
echo [3/4] Preparing Git...
:: Ensure remote is set with token (in case folder already exists or logic changes)
git remote set-url origin https://%HF_USERNAME%:%HF_TOKEN%@huggingface.co/spaces/%HF_USERNAME%/%SPACE_NAME%

:: Configure user for this repo (generic) to ensure commit works
git config user.email "%HF_USERNAME%"
git config user.name "palwasheyqureshi@gmail.com"

git add .
git commit -m "Deploying Phase 2 Backend"

echo.
echo ========================================================
echo [4/4] READY TO PUSH! (Automated)
echo ========================================================
echo.
echo Target: https://huggingface.co/spaces/%HF_USERNAME%/%SPACE_NAME%
echo Authentication: Token is already configured.
echo.
echo Press any key to PUSH changes to the Space...
pause

echo.
echo Pushing now...
git push

echo.
echo If it says 'Success', you are done!
echo Check your Space: https://huggingface.co/spaces/Palwasha-49/Hackathon-II
pause
