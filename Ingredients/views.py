from django.shortcuts import render

# Create your views here.
from Ingredients.forms import IngredientForm
from .models import Ingredients as ingr

TypeOfImg = ['png', 'jpg', 'jpeg']


def create_Ingredient(request):
 #   if not request.user.is_authenticated():
  #      return render(request, 'Home/login.html')
   # else:
        form = IngredientForm(request.POST or None, request.FILES or None)
        if form.is_valid():

            name=form.cleaned_data['name']
            Ingredient = form.save(commit=True)

            Ingredient.pics = request.FILES.get('pics','')
            file_type = Ingredient.pics.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in TypeOfImg:
                context = {
                    'Ingredient': Ingredient,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'Ingredients/create_ingredient.html', context)

            Ingredient.save()
            return render(request, 'Ingredients/detail.html', { 'Ingredient': Ingredient})
        context = {
            "form": form,
        }
        return render(request, 'Ingredients/create_ingredient.html', context)



def  list_of_Ingredients(request):

    x =ingr.objects.all()
    return render(request, 'Ingredients/ingrediantswiew.html', {  'Ingredients': x})

#def edit_Ingredient(request,id):
 #   Ingredient=ingr.objects.get(id=id)
  #  return render(request, 'Ingredients/exit_ingredient.html', { 'Ingredient': Ingredient})


#def update_Ingredient(request):

def delete_Ingredient(request,Ingredient_id):
        album = ingr.objects.get(pk=Ingredient_id)
        album.delete()
        albums = ingr.objects.all()
        return render(request, 'Ingredients/ingrediantswiew.html', {'Ingredients': albums})











