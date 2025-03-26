# HTTP Website Analytics Tester

A Python-based bot that simulates user sessions on HTTP websites to test analytics functionality. 

# Do not use for commercial purposes 
Using python bots to boost analytics is strictly prohibited.

## Overview

This tool creates automated browser sessions that mimic real user behavior on HTTP websites. It's designed to:

- Navigate through HTTP websites, handling security warnings automatically
- Simulate realistic user browsing patterns (scrolling, clicking, reading)
- Maintain sessions for specific durations to generate meaningful analytics data
- Work with modern analytics platforms to verify data collection

## Features

- **HTTP Support**: Handles HTTP websites including "proceed" buttons for security warnings
- **Realistic Browsing**: Simulates human-like scrolling, reading time, and navigation
- **Configurable Sessions**: Customizable session duration and count
- **Environment-based Configuration**: Uses `.env` file to store website URLs and other settings

## Purpose

This tool is specifically designed for:
1. Testing analytics implementations
2. Verifying session tracking functionality
3. Simulating user engagement without scraping content
4. Controlled environment testing
5. Used inside controlled environment

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install selenium python-dotenv
   ```
3. Create a `.env` file in the root directory with your website URL:
   ```
   WEBSITE_URL=http://your-website.com
   ```
4. Install Chrome WebDriver (ensure it matches your Chrome version)

## Usage

Run the script with:

```bash
python main.py
```

The bot will:
- Start multiple browser sessions based on your configuration
- Navigate to your specified website
- Handle any HTTP security warnings automatically
- Click on links, scroll through pages, and simulate reading time
- Run each session for the configured duration

## Configuration

Edit your `.env` file to customize:
- `WEBSITE_URL`: The HTTP website to test
- Add other parameters as needed

## Important Notes

- This tool **does not** scrape website content
- It only clicks on elements if they are available and within the same domain
- Designed for testing analytics functionality in controlled environments
- Not intended for production use or to artificially inflate analytics metrics