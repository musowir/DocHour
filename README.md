# DocHour
DocHour is a web application built using the Django framework that enables users to book appointments with doctors from anywhere in the world and engage in chat sessions with expert medical professionals. The application allows users to search for doctors by specialty, location, and availability, making it easy to find and book appointments that fit their needs. Additionally, users can communicate with doctors through a chat interface, enabling them to ask questions, receive advice, and discuss their concerns in real-time. The DocHour project has the potential to make healthcare more accessible and convenient for users, as it eliminates the need for in-person appointments and allows users to receive medical guidance from the comfort of their own homes.

## Setup
1. install python (https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)
    
    don't forget to add as enviroment variable while installing ( how to do : https://drive.google.com/file/d/1y_HXNBPkXcLPN2dY4FHfo6gKh-gFRmnQ/view?usp=share_link)

2. Download and install vs code (https://code.visualstudio.com/download)

3. install git (https://www.geeksforgeeks.org/introduction-and-installation-of-git/)

4. create a folder and open vs code in that folder

5. open terminal in vs code

6. To check whether git is correctly installed

      `git -v`

7. cloning the project (downloading project to local machine)

      `git clone https://github.com/musowir/DocHour.git` 

8. go to project directory

      `cd DocHour`
      
9. create a virtual environment

    `python -m venv env`
    
10. activating environment

      `env\Scripts\activate`

11. To install required libraries 

     `pip install -r requirements.txt`
     
12.updating database

     python manage.py makemigrations
     python manage.py migrate
     
## Running the project

`python manage.py runserver`

All done! server running!


screenshot of the process : https://drive.google.com/file/d/1e3SQ67AeM0Fh2vic6eJb8TRXuyeprxqv/view?usp=share_link

