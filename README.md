# Yummy_Pies

**Project plan  :**

     User can :
                Register,Login/out
                Create recipy
                CRUD own recipies 
                Read others recipies and  comment,(like/hate), choose recipy to make it.
     Admin (super user) can :  
                            CRUD  recipies and ingredients
                            Remove or block users
     Models :
                Recipy :
                        Difficulty (easy , midium , hard )
                        Instruction(s)
                        Ingredients
                        Comments (from users)
                        Cost (sum up ingridians price)
                Ingridients:        
                            Name
                            Price
     Apps:
            Recipy:
                    Users can create recipyies choose  ingridients (if not exist create it) and e.g write instructions
                    Admin can modify it              
            Ingridient:
                        CRUD  igridients from Admin (users can only create it) 
            Your_recipies: 
                        Show cost of all chosen recipies,require ingridients 
                        User can remove recipy from basket           
 
            
**Tutorials :**

    1. http://www.python.rk.edu.pl/w/p/wprowadzenie-do-django-10/
    2. https://docs.djangoproject.com/pl/1.11/
    3. https://www.youtube.com/watch?v=XQll-WgZcpE&index=20&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK


**Usefull commends:**

    1. django-admin.py startproject "new_project"_ - Create project dictionary and  default  django files.
    2. python manage.py startapp "new_aplication"_ - Create aplication.
    3. python manage.py migrate - Create database from models 
    4. python manage.py runserver - Run app serwer default at http://127.0.0.1:8000/
    5. python manage.py createsuperuser - Create superuser/admin
    6. python manage.py makemigrations -Make new migrations
