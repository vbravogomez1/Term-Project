# Term-Project

## Team Members
- Vanessa Bravo
- Christian Aiza

# Project Proposal: Star Alignment Finder

## The Big Idea

The primary goal of our project is to create a Python website that finds and shows "the astronomy picture of the day” based on a specific date. We got inspiration from the "get the weather based on a date" project shown in class, but we wanted to make it more fun and show something significant that people could gift each other and even print for themselves. We even think this might become a future business if implemented effectively.

We aim to use a NASA API ([https://api.nasa.gov/planetary/apod](https://api.nasa.gov/planetary/apod)) to bring astronomical data to a user-friendly interface, allowing users to view star patterns for any given date, such as birthdays, historical events, or significant dates like anniversaries. This project combines astronomy and coding to provide a unique educational opportunity!

The minimum viable product (MVP) will include basic functionality that allows users to enter a date and receive the corresponding star alignment data in a simple format and image. Our stretch goal is to create an interactive visualization that displays star positions in real time and provides additional information about notable constellations.

## Learning Objectives

Our team’s shared learning goal is to gain a comprehensive understanding of Python's role in managing and visualizing complex data from external sources, particularly through API integration. We aim to strengthen our skills in data processing and user-centered design. Each team member has a specific area of focus that supports these broader objectives:

- **Vanessa**: Aims to deepen her knowledge of API integration by learning how to establish stable connections with external APIs, specifically focusing on the NASA API.
- **Christian**: Seeks to enhance his understanding of user interface (UI) design, with a goal to create an interface in a visually intuitive and engaging format.

Together, we aim to develop skills not only in programming but also in technical collaboration and knowledge-sharing. We plan to achieve a project that functions smoothly from data retrieval to presentation through team collaborative coding and dedicating time to learn new concepts.

## Implementation Plan

To bring our project concept to life, we plan to leverage the NASA Astronomy Picture of the Day (APOD) API as our primary data source. However, we will evaluate and consider alternative or supplementary APIs if necessary to enhance our data set and improve our project. The implementation of our project will focus on the following main components:

1. **API Connection**: Retrieve relevant star alignment data based on user-provided dates, potentially including images or descriptive astronomical data. This involves configuring API authentication and managing API rate limits to prevent interruptions.

2. **Data Processing**: Filter and structure the information from the API response to extract meaningful astronomical data, such as star positions and notable constellations. Techniques for handling missing data, error-checking, and organizing hierarchical data will be essential.

3. **Visualization**: Make the project accessible and engaging through visualization.

4. **User Interface**: Design a simple interface for easy input and interaction, allowing users to retrieve star alignment information without unnecessary complexity.

## Project Schedule

We’re aiming to complete the project within three weeks, with an additional fourth week for unexpected issues or adjustments.

- **Week 1**: Initial Setup and Exploration  
  Set up the project, assign roles, explore the NASA API, and test data retrieval.

- **Week 2**: API Integration and MVP Development  
  Focus on reliable data retrieval and begin developing the MVP interface for date input and basic star data visualization.

- **Week 3**: Integration, Testing, User Experience, and Submission  
  Integrate all components, conduct thorough testing, and ensure consistent functionality.

## Collaboration Plan

Our collaboration will be organized around working and coding together, primarily using the same computer to enhance learning as beginner coders. We have experience working together in Python, so we are confident that both of us will contribute equally to the project.

## Risks and Limitations

The biggest risk we anticipate is technical reliance on the NASA API. Since our project depends on data retrieval from NASA, any API limitations or downtime could delay our progress. To mitigate this, we’re researching backup API sources and considering alternative visualization options to ensure project continuity even if API access is limited.

Another potential risk is front-end design, as we lack extensive experience with user interfaces. Creating a user-friendly interface is crucial, and while we had practice with Assignment 3 and covered Flask basics in class, the learning curve with front-end tools and frameworks could pose a challenge. We will use class resources and online tools to expand our knowledge of Flask and HTML basics.

## Additional Course Content

- **Advanced Data Structures**: Additional guidance on using tuples or dictionaries to organize API data would streamline our project.
- **API Handling Techniques**: More insights into making API requests, handling JSON responses, and managing limitations would enhance our project.
- **Iterations and Functions for Data Processing**: Instruction on efficient iterations and reusable functions, especially for handling nested data and formatting star alignment data, would be beneficial.

---

# Final Project

## Introduction
The Star Alignment Finder is a web-based application that retrieves the NASA Astronomy Picture of the Day (APOD) for a given date. This tool is designed to make astronomy accessible to a broad audience by providing stunning visuals and intriguing facts about the cosmos. Our project connects users to the universe by delivering daily astronomical phenomena directly through a web interface.

## Big Idea
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
- An API key from NASA (which can be obtained [here](https://api.nasa.gov))

## Implementation Information

### Architecture
The application utilizes Flask as its backend framework, serving data fetched from NASA's APOD API. The front end is crafted with HTML and CSS, providing a user-friendly interface.

### Key Technologies
- **Flask**: for setting up the server and routes.
- **NASA APOD API**: for fetching astronomy pictures and descriptions.
- **Python-dotenv**: for managing environment variables.

## Reflection

### Development Process

The development journey of the Star Alignment Finder was filled with both challenges and achievements. We encountered initial hurdles in API integration, particularly in handling date-specific requests and managing API rate limits. Debugging issues related to date formatting and API key authentication were significant early obstacles. We utilized resources such as Stack Overflow and extensive documentation reading, which immensely improved our problem-solving skills.

Our teamwork strategy involved collaborative coding sessions, which proved essential in overcoming complex challenges. This approach allowed us to share insights and alternative solutions quickly, speeding up the debugging and feature implementation processes. Furthermore, working closely helped us synchronize our understanding of Flask's capabilities and limitations, leading to more efficient code.

### Learning and Use of AI Tools

This project deepened our understanding of Python and Flask in creating web applications that interact with external APIs. We learned to manipulate and display data fetched from NASA's API, enhancing the interactivity of our application. The use of AI tools like ChatGPT assisted us in understanding more complex aspects of API data handling and Flask routing mechanisms. This tool was instrumental in helping us troubleshoot and refine our code, making the learning process both educational and practical.

Additionally, the experience of formatting and presenting data in a user-friendly manner taught us valuable lessons in web design and user experience, skills that are highly applicable across many areas of software development. We also used ChatGPT to learn how to correctly format our README.

### Project Evolution

The evolution of the Star Alignment Finder was documented through version control, allowing us to track changes and improvements over time. We used Git for version control, which, despite initial challenges, became an invaluable part of our development workflow, helping us manage project versions and collaborate more effectively.
