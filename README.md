# Term Project - Star Alignment Finder

### Team Members:
- Vanessa Bravo & Christian Aiza

### Introduction
The Star Alignment Finder is a web-based application that retrieves the NASA Astronomy Picture of the Day (APOD) for a given date. This tool is designed to make astronomy accessible to a broad audience by providing stunning visuals and intriguing facts about the cosmos. Our project connects users to the universe by delivering daily astronomical phenomena directly through a web interface.

### Big Idea
Why explore the universe alone when you can have the cosmos at your fingertips? Our project was inspired by the desire to bridge the gap between complex astronomical data and everyday enthusiasts by providing an easy-to-use platform that educates, inspires, and ignites curiosity about the universe.

## User Instructions

### Getting Started
This section provides detailed steps on downloading, installing, and initiating the Star Alignment Finder:
1. **Clone the repository**: `git clone https://github.com/yourusername/star-alignment-finder.git`
2. **Navigate to the project directory**: `cd star-alignment-finder`
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Run the application**: `flask run`
5. **Open a web browser** and visit `http://127.0.0.1:5000` to start exploring the universe.

### Prerequisites
- Flask
- An API key from NASA (which can be obtained (https://api.nasa.gov))

## Implementation Information

### Architecture
The application utilizes Flask as its backend framework, serving data fetched from NASA's APOD API. The front end is crafted with HTML and CSS, providing a user-friendly interface.

### Key Technologies
- Flask: for setting up the server and routes.
- NASA APOD API: for fetching astronomy pictures and descriptions.
- Python-dotenv: for managing environment variables.

## Project Overview

The Star Alignment Finder is a Python web application designed to provide users with the NASA Astronomy Picture of the Day based on a specific date. This project aims to make astronomy more accessible and engaging by allowing users to explore significant astronomical events and imagery through a user-friendly web interface. The application uses NASA's APOD (Astronomy Picture of the Day) API to fetch data and images, which can be a great educational tool or a personal interest platform for astronomy enthusiasts. The primary goals of this project were to enhance our skills in API integration, improve our understanding of Flask for web development, and learn to process and display complex data in a simple and comprehensible format.

## Reflection

### Development Process

The development journey of the Star Alignment Finder was filled with both challenges and achievements. We encountered initial hurdles in API integration, particularly in handling date-specific requests and managing API rate limits. Debugging issues related to date formatting and API key authentication were significant early obstacles. We utilized resources such as Stack Overflow and extensive documentation reading, which immensely improved our problem-solving skills.

Our teamwork strategy involved collaborative coding sessions, which proved essential in overcoming complex challenges. This approach allowed us to share insights and alternative solutions quickly, speeding up the debugging and feature implementation processes. Furthermore, working closely helped us synchronize our understanding of Flask's capabilities and limitations, leading to more efficient code.

### Learning and Use of AI Tools

This project deepened our understanding of Python and Flask in creating web applications that interact with external APIs. We learned to manipulate and display data fetched from NASA's API, enhancing the interactivity of our application. The use of AI tools like ChatGPT assisted us in understanding more complex aspects of API data handling and Flask routing mechanisms. This tool was instrumental in helping us troubleshoot and refine our code, making the learning process both educational and practical.

Additionally, the experience of formatting and presenting data in a user-friendly manner taught us valuable lessons in web design and user experience, skills that are highly applicable across many areas of software development.

### Project Evolution

The evolution of the Star Alignment Finder was documented through version control, allowing us to track changes and improvements over time. We used Git for version control, which, despite initial challenges, became an invaluable part of our development workflow, helping us manage project versions and collaborate more effectively.