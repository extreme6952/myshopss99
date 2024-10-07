from .models import Category


#Процессор для отображения списка выпадения категорий на любой странице сайта


def categories(request):

    category = Category.objects.all()

    return {
        'categories':category
    }
