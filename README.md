# Integration Test With Pytes

## 專案介紹
使用Pytest進行整合測試

## 2. 環境建置
本專案使用PYTHON並且以poetry進行套件管理，請先安裝[POETRY](https://python-poetry.org/)
## 3. 執行測試
```shell
poetry run pytest --env qa
```
預設使用QA環境，若要使用其他環境，請於`--env`後面加上環境名稱，例如:`local`

## 4. 專案結構
```shell
C:.
├─src
└─tests
    ├─scripts
    ├─test_case
    └─utils
```
1. `src`為專案主要程式碼
2. `tests`放置測試程式碼
3. `scripts`放置腳本程式碼 ex: `local.py` 中設定了執行測試前要啟動主專案
4. `test_case`放置測試案例
5. `utils`放置工具程式碼