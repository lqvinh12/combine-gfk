# Install packages

Only need to run once
- run `pip3 install -r requirements.txt` in terminal


# Run the app to combine files

1. Copy all files need to combine to `input` folder
2. Run `python3 app.py` in terminal or run `app.py` in VSCode
3. The output file will be in `output` folder with name `%Y%m%d %H%M%S combine.xlsx`


# Logs

Each run will create a log file in `logs` folder, which contains 2 files:
- `%Y%m%d %H%M%S.log`: contains runtime log
- `%Y%m%d %H%M%S ERROR.log`: contains errors log or warnings during runtime