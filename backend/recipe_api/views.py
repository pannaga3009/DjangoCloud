from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Recipe
import json

@csrf_exempt
def recipe_list(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        data = [{'id': recipe.id, 'recipe_name' : recipe.recipe_name, 'recipe_details': recipe.recipe_details} for recipe in recipes]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            recipe = Recipe.objects.create(
                recipe_name = data['recipe_name'],
                recipe_details=data['recipe_details']
            )
            recipe.save()
            return JsonResponse({'id': recipe.id, 'recipe_name': recipe.recipe_name, 'recipe_details': recipe.recipe_details}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data. Make sure to include recipe_name and recipe_details in your request.'}, status=400)


@csrf_exempt
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return JsonResponse({'error': 'Recipe not found.'}, status=404)
    if request.method == 'GET':
        data = {'id': recipe.id, 'recipe_name': recipe.recipe_name, 'recipe_details': recipe.recipe_details}
        return JsonResponse(data)
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            recipe.recipe_name = data['recipe_name']
            recipe.recipe_details = data['recipe_details']
            recipe.save()
            return JsonResponse({'id': recipe.id, 'recipe_name': recipe.recipe_name, 'recipe_details': recipe.recipe_details})
        except KeyError:
            return JsonResponse({'error': 'Invalid data. Make sure to include recipe_name and recipe_details in your request.'}, status=400)
    elif request.method == 'DELETE':
        recipe.delete()
        return JsonResponse({'message': 'Recipe deleted successfully.'}, status=204)
