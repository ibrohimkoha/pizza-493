from django.shortcuts import render
from .models import ScrollModel, ImageModel, DrinksModel, FricesModel,BurgerModel, SaladModel, PizzaModel
# Create your views here.
from .forms import UserForm 
def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            redirect('pages:home')
    scrolls = ScrollModel.objects.all().order_by('-pk')[:5]
    image = ImageModel.objects.all()
    drinks = DrinksModel.objects.all()
    frices = FricesModel.objects.all()
    burger = BurgerModel.objects.all()
    salad = SaladModel.objects.all()
    pizza = PizzaModel.objects.all()
    context = {
        'scrolls':scrolls,
        'image':image,
        'drinks':drinks,
        'frices':frices,
        'burger':burger,
        'pizza':pizza,
        'salad':salad,
    }
    return render(request, template_name='index.html', context=context)