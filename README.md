# Build-a-YouTube - for AI ethics curriculum YouTube and You

YouTube and You is a curriculum designed for 7th grade science classes that adheres to the Massachusetts Science and Technology/ Engineering Curriculum Framework (2016). Build-a-YouTube is an activity in Day 4 of the 2-week curriculum. For more details about the curriculum, please [visit this Google Folder](https://drive.google.com/drive/folders/1_BdoUng8V2OL-bTBaDItMBta1Gh4mD9n?usp=sharing)

This web application is developed using the OpenAI API quickstart example as a framework. Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd build-a-youtube
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!
