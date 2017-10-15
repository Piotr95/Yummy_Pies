# Yummy_Pies

Project plan  :

     User can :
                Register,Login/out
                create recipy,
                CRUD own recipies 
                Read others recipies and  comment,(like/hate), choose recipy to make it.
     Admin (super user) can :  
                CRUD  recipies and ingredients
                Remove or block users
     Models :
        Recipy :
                Difficulty (easy , midium , hard )
                Instruction(s)
                ingredients
                Comments (from users)
                Cost (sum up ingridians price)
        Ingridiants        
                name
                price
     Apps:
        Recipy:
        Users can create recipyies choose  ingridients (if not exist create it) and e.g write instructions
        Admin can modify it              
        Ingridient:
        CRUD  igridients from Admin (users can only create it) 
        Shopping_basket: 
        Show cost of all chosen recipies,require ingridients 
        user can remove recipy from basket           
 
            
Tutorials :

1. http://www.python.rk.edu.pl/w/p/wprowadzenie-do-django-10/
2. https://docs.djangoproject.com/pl/1.11/
3. https://www.youtube.com/watch?v=XQll-WgZcpE&index=20&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK


Usefull commends:

1. django-admin.py startproject "new_project" - create project dictionary and defoult django files.
2. python manage.py startapp "new_aplication" - create aplication.
3. python manage.py migrate - create database from models 
4. python manage.py runserver - run app serwer  defoult at http://127.0.0.1:8000/
5. python manage.py createsuperuser - create superuser/admin
6. python manage.py makemigrations -make new migrations
