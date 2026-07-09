# LinkedIn Auto Job Applier

A bot that automates applying to jobs on LinkedIn — searches for relevant jobs, answers application questions, and applies for you.

## Install

```
pip install -r requirements.txt
```

Requires Python 3.10+ and Google Chrome installed.

## Configure

Edit the files in `config/`:

- `personals.py` — your name, phone, address
- `questions.py` — answers for common application questions, resume path
- `search.py` — job search filters and preferences
- `secrets.py` — LinkedIn login and (optional) OpenAI API key
- `settings.py` — bot behavior (stealth mode, click intervals, etc.)

Place your resume at the path set in `default_resume_path` (in `config/questions.py`).

## Run

```
python server.py
```
This starts the live dashboard and runs the bot. Open `http://localhost:5000` to watch job applications live and respond to any "needs your input" prompts.

## Disclaimer

For educational use only. Use at your own risk and make sure your usage complies with LinkedIn's terms of service.
