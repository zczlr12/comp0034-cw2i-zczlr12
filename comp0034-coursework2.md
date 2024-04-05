# COMP0034 2023/24 Coursework2

## Application code

As a new model needs to be created for each new item, it might takes about 1 minute for the line chart to be displayed in the Future Trend page. For the item that has its model in the `src/pasta_sales/models`, the line chart should be displayed in several seconds.

## Test code

## Tools and techniques

URL of the Github repository: <https://github.com/ucl-comp0035/comp0034-cw2i-zczlr12>

### Set-up instructions

1. Fork this repository <https://github.com/ucl-comp0035/comp0034-cw2i-zczlr12>
2. Clone the forked repository to create a project in an IDE
3. Create and activate a virtual environment in the project folder

    - MacOS: `python3 -m venv .venv` then `source .venv/bin/activate`
    - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
4. Check `pip` is the latest versions: `pip install --upgrade pip`
5. Install the requirements `pip install -r requirements.txt`
6. Install the application code e.g. `pip install -e .`
4. Run the REST API app `flask --app rest_api run --debug`
5. Open a new terminal and run the pasta sales predictor app `python pasta_sales/app.py`
5. Open a browser and go to <http://127.0.0.1:8050>
6. Stop the apps using `CTRL+C`

## References

### Acknowledgement of the use of AI

I acknowledge the use of GitHub Copilot version 1.176.0 (GitHub, https://github.com/features/copilot) to generate some of the code and docstrings after the first few characters had been typed in the data preparation code.

### Attribution for the data set

Author: Paolo Mancuso, Veronica Piccialli, Antonio M. Sudoso (University of Rome Tor Vergata)

License: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode)

Location: https://data.mendeley.com/datasets/njdkntcpc9/1