# TwtGPT

## Daily Twitter Automation Script

This script generates and posts five tweets daily using OpenAI's GPT-4 model and the Twitter API. It uses environment variables to securely store API keys.

## Features

- Generates tweets based on predefined topics using OpenAI's GPT-4.
- Automatically posts the tweets to Twitter using the Tweepy library.
- Schedules daily execution using the `schedule` library.

## Requirements

- Python 3.7 or later
- OpenAI API Key
- Twitter API credentials (API Key, API Secret, Access Token, Access Secret)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/daily-twitter-bot.git
   cd daily-twitter-bot
   ```

2. Install dependencies:
   ```bash
   pip install openai tweepy schedule python-dotenv
   ```

3. Set up environment variables:
   - Create a `.env` file in the project root with the following content:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     TWITTER_API_KEY=your_twitter_api_key
     TWITTER_API_SECRET=your_twitter_api_secret
     TWITTER_ACCESS_TOKEN=your_twitter_access_token
     TWITTER_ACCESS_SECRET=your_twitter_access_secret
     ```

4. Update the predefined topics in the script (optional).

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. The script will:
   - Generate five tweets daily.
   - Post the tweets to Twitter.
   - Repeat this process daily at the scheduled time (default: 9:00 AM).

## Customization

- **Scheduling**: Modify the time in the `schedule.every().day.at("09:00")` line in the script.
- **Topics**: Update the `topics` list in the `generate_and_post_daily_tweets` function with your own ideas.

## Deployment

For continuous operation:
- **Linux/Mac**: Use `cron` to run the script as a background job.
- **Windows**: Use Task Scheduler.
- **Cloud Hosting**: Deploy the script on a platform like Heroku, AWS, or Google Cloud for 24/7 uptime.

## Security

- Never hardcode API keys in your script.
- Use `.gitignore` to prevent the `.env` file from being committed to version control.

## Libraries Used

- `openai`: For tweet generation.
- `tweepy`: For posting tweets to Twitter.
- `schedule`: For daily task scheduling.
- `python-dotenv`: For managing environment variables during development.