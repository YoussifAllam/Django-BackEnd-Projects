# WepApp-VezeTa-Django-Project

![Screenshot 2023-09-07 001535](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/4c5a9f07-d908-4ddd-8cbf-baba5b472512)

### The frontend tamplate copyright from Colorlib
## Assignment Problem Statement:
Part 1:
1) Create a web-app where a user can login.
2) User can make profile that have his info .
3) User can view his/her profile.

Part 2:
1) User can search and view profile of doctors.
2) They can share their uploaded clinic photos with any of those users.
3) Users can see the shared files by other users also in uploaded files.

Additional Features:
1) In doctor profile  can set his/her profile picture.
2) Users can download other users uploaded files.
3) The user can upload any type of files such as images, videos, text files for it's clinic

## Technologies Used:
1) Python
2) Django
3) Bootstrap
4) JavaScript


## Additional Python Modules Required:
1) Django
2) django-crispy-forms
3) Pillow

## Prerequisites
Before you begin, ensure you have met the following requirements:
```
1) Python 3.6+
2) Django and Django REST framework installed. 
```
* You can install them using pip:
```
pip install django
pip install djangorestframework
```
* Installation Clone the repository to your local machine:
```
git clone https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project.git
```
* Navigate to the project directory:
```
cd bookstore
```
* Install the project dependencies:
```
pip install -r requirements.txt
```
* Apply the database migrations:
```
python project/manage.py makemigrations
python project/manage.py migrate
```
* Activate a virtual environment (optional but recommended):
```
venv_bookstore\Scripts\activate
```
* Start the development server:
```
python manage.py runserver
```

### In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/

# Screenshots :
### Home page that have all doctors informations
![Screenshot 2023-09-07 001535](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/4c5a9f07-d908-4ddd-8cbf-baba5b472512)
### Update user informations 
![Screenshot (94)](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/6e5c166d-d1c8-4d16-9e20-bc7de2a0fdb3)
### SignUp page
![Screenshot (95)](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/48aa86e3-afe7-4f52-a92e-821dc1b2dd14)
### Login page
![Screenshot (90)](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/4ca02965-85ec-4e98-954a-6b8742496117)
### doctor profile page
![Screenshot (91)](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/7cbe4769-c569-4ea8-8ed4-1655b004ead7)
### access doctor profile page using it's slug
![Screenshot (92)](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/28c16b71-4358-4b5f-81e6-4636fb544b14)
### admin page
![Screenshot (93)](https://github.com/YoussifAllam/WepApp-VezeTa-Django-Project/assets/96921160/b3391f99-24ab-4428-ac95-6d92377fedb7)



_____________________________________________________
Creating a README file for your GitHub repository that contains Django and Django REST Framework projects is a great way to introduce and explain your projects to other developers or anyone visiting your repository. Here's a basic template for a README file that you can customize according to the specifics of your projects:

markdown
Copy code
# Django Projects Collection

This repository contains a collection of web applications built with Django and Django REST Framework. These projects demonstrate various aspects of web development using Django, including API creation, CRUD operations, authentication, and more.

## Projects Included

1. **Project Name 1**: A brief description of what this project does and its main features.
2. **Project Name 2**: A brief description of what this project does and its main features.
3. **Project Name 3**: A brief description of what this project does and its main features.
   - And so on for each project...

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```bash
pip install django
pip install djangorestframework
Installing
A step by step series of examples that tell you how to get a development environment running:

bash
Copy code
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
pip install -r requirements.txt
python manage.py runserver
Navigate to http://127.0.0.1:8000 in your web browser to view the project.

Running the tests
Explain how to run the automated tests for this system:

bash
Copy code
python manage.py test
Deployment
Add additional notes about how to deploy this on a live system.

Built With
Django - The web framework used
Django REST Framework - The toolkit used to build APIs
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

Authors
Your Name - Initial work - YourUsername
See also the list of contributors who participated in this project.

License
This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments
Hat tip to anyone whose code was used
Inspiration
etc
bash
Copy code

### Tips for Customizing Your README
1. **Project Descriptions**: Be concise but informative; explain the purpose of each project and any special technologies or techniques it demonstrates.
2. **Getting Started**: Ensure these instructions are clear so anyone can clone your repo and get your projects running with minimal setup.
3. **Testing and Deployment**: Provide detailed instructions on how to deploy and test your projects, which will be beneficial for users who wish to use your projects in a production setting.

Feel free to expand or modify this template based on the complexity and number of proje
