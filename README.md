# Portfolio Website 👋

💻 Website containing all full-stack development projects, as well as blog posts.

![screenshot](https://raw.githubusercontent.com/cammarb/my-portfolio/master/portfolio_screenshot.png)

## Run project
### 1. Clone the project and open the folder
```
git clone https://github.com/cammarb/my-portfolio.git && cd my-portfolio
```

### 2. Create virtual enviroment
#### Linux/MacOS
```
python3 -m venv venv
```
#### Powershell
```
py -3 -m venv venv
```
### 3. Activate virtual enviroment
#### Linux/MacOS
```
. venv/bin/activate
```
#### Powershell
```
venv\Scripts\activate
```
### 4. Install dependencies
```
pip install -r requirements.txt
```
### 5. Run project
```
flask run
```

## Pages

### Home

Short description about me and my skills (web dev related).

### Projects

It will display a gallery of the projects I have developed,
including a preview image of them, a short description and the
technologies used, as well as a link to the repository.

### Blog

List of my entries will be shown and on each blog post a title
should be required to be posted.

### Contact

Display of links to my Github profile, email, Linkedin and PDF
resume.

## Features
- [x] 🖼 Responsive design
- [x] ➕ Blog
    - [x] Create
    - [x] Delete 
    - [ ] Edit
- [x] 📁 Project
    - [x] Create
    - [x] Delete 
    - [ ] Edit
- [x] 🔒 Login/Authentication
    - [x] Register
    - [x] Login  
### To be implemented in the future
- [x] 💡 Dark and light mode switcher
- [ ] 🔍 Search and filter blog entries
- [ ] 🎨 Background animations

## Built in with

- Python (Flask)
- Javascript
- CSS
- HTML

