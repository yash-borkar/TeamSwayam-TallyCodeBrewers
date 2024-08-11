# CompileSpace 🚀💻

## Code Brewers Hackathon Project for Tally Solutions

Welcome to CompileSpace - Your All-in-One Online Coding Platform! 🎉



## 🌟 Introduction

CompileSpace is an innovative online coding platform developed for the "Code Brewers" hackathon by Tally Solutions. Our goal is to provide a comprehensive environment for coders of all levels, from beginners to competitive programmers.


## 🛠️ Features

CompileSpace offers three main sections:

1. **Code Playground** 🎨
   - Simple code compilation environment
   - Perfect for beginners and quick code testing

2. **Code Arena** 🏟️
   - Solve a variety of competitive Data Structures and Algorithms (DSA) questions
   - Improve your problem-solving skills

3. **Code Battleground** ⚔️
   - Participate in exciting coding contests
   - Compete with other programmers in real-time challenges
     
## 💡 Usage

1. **Code Playground**: 
    - Navigate to the Code Playground section
    - Choose your preferred programming language
    - Write your code in the editor
    - Click "Run" to compile and see the output

2. **Code Arena**:
    - Browse available DSA questions
    - Select a question to solve
    - Write your solution in the provided editor
    - Submit your answer for evaluation

3. **Code Battleground**:
    - Check the contest schedule
    - Join an ongoing or upcoming contest
    - Solve problems within the given time limit
    - View your ranking on the leaderboard
  
## Getting Started 🚀

To get started with CompileSpace, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yash-borkar/TeamSwayam-TallyCodeBrewers.git

2. **Navigate to the Project Directory**:
   ```bash
   cd TeamSwayam-TallyCodeBrewers

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the Application**:
   ```bash
   python app.py

## Contributing 🤝

We welcome contributions to improve CompileSpace! To contribute, please follow these steps:

1. **Fork the Repository**:
   - Click the "Fork" button at the top right corner of the repository page on GitHub to create your own copy.

2. **Clone Your Fork**:
   - Clone the forked repository to your local machine:
     ```bash
     git clone https://github.com/yash-borkar/TeamSwayam-TallyCodeBrewers.git
     ```

3. **Create a Feature Branch**:
   - Navigate to the project directory and create a new branch for your feature or fix:
     ```bash
     git checkout -b feature/YourFeature
     ```

4. **Make Your Changes**:
   - Implement your changes or add your feature. Ensure you adhere to the project's coding standards and add any necessary tests.

5. **Commit Your Changes**:
   - Commit your changes with a descriptive message:
     ```bash
     git commit -am 'Add new feature or fix description'
     ```

6. **Push to the Branch**:
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/YourFeature
     ```

7. **Create a Pull Request**:
   - Go to the original repository on GitHub and click on "Compare & pull request" to create a new pull request.

8. **Provide a Description**:
   - Add a detailed description of your changes and why they are needed.

9. **Submit the Pull Request**:
   - Review your changes and submit the pull request for review.

Thank you for contributing to CompileSpace!

## 🔮 Future Scopes
#### We plan to enhance CompileSpace with additional features and improvements, including
   - Security Enhancements: Utilizing Docker and Kubernetes to containerize all compilers and the
     Flask application for improved security and scalability.
   - Multi-Language Support: Adding support for multiple programming languages to cater to a broader
      audience.
   - Advanced Analytics: Implementing features to analyze user performance and provide personalized recommendations.
   - Enhanced UI/UX: Continuously refining the user interface and experience based on user feedback.
   - Sandbox Environment: Creating a secure sandbox environment for running user code to prevent potential security risks and ensure isolated execution.

## Containerizing the web application in Docker 
   #### Follow below commands
   # compiler_exec_from_docker
 - Inside compiler_exec_from_docker (folder)
 - use this folder for docker deployment
docker container exec for multiple isolated compilers to execute in flask application

### check for running services in docker ( cmd utils )
```
docker ps # to check running process
```
#### before building container ensure to clear other services
```
docker-compose down
```
#### inside compiler_exec that is root folder exec following command
```
docker-compose up --build
```
### you can see the " 2 " server ( localhost / bridge network)
```
click  on those server links and try the 3 compilers and hit run :)
```


## 👥 Contributors
- Kartikey Sapkal (https://www.linkedin.com/in/kartikey-sapkal-316822248/)
- Prathamesh Kapadne (https://www.linkedin.com/in/prathamesh-kapadne-a1b573219/)
- Yash Borkar (https://www.linkedin.com/in/yashborkar/)
  
## Happy Coding! 🎈👨‍💻👩‍💻
