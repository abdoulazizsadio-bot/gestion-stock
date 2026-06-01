from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .data import articles as articles_data
from .forms import SignUpForm


def _render_page(request, template_name, context=None):
    """Rendu de page standard avec un contexte optionnel."""
    if context is None:
        context = {}
    return render(request, template_name, context)

def _compute_stock_metrics(articles):
    """Calcule des indicateurs de stock destinés à l'interface utilisateur."""
    total_products = len(articles)
    total_quantity = sum(item.get('quantite', 0) for item in articles)
    stock_value = sum(item.get('prix', 0) * item.get('quantite', 0) for item in articles)
    total_sales = stock_value * 1.5
    pending_orders = 4

    return {
        'total_products': total_products,
        'stock_value': stock_value,
        'total_sales': total_sales,
        'pending_orders': pending_orders,
        'total_quantity': total_quantity,
    }
    

@login_required
def index(request):
    recent_sales = [
        {'client': 'Toto', 'ref': '006', 'date': '25/12/2020', 'montant': '528,00 FCFA'},
        {'client': 'SA', 'ref': '005', 'date': '25/02/2020', 'montant': '528,00 FCFA'},
        {'client': 'Toto', 'ref': '001', 'date': '25/02/2020', 'montant': '2028,00 FCFA'},
    ]
    context = _compute_stock_metrics(articles_data)
    context.update({'articles': articles_data, 'recent_sales': recent_sales})
    return _render_page(request, 'index.html', context)


def contact(request):
    return _render_page(request, 'contact.html', {'articles': articles_data})


def articles(request):
    return _render_page(request, 'articles.html', {'articles': articles_data})


@login_required
def dashboard(request):
    return _render_page(request, 'dashboard.html', {'articles': articles_data})


def logout_view(request):
    logout(request)
    return _render_page(request, 'registration/logged_out.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return _render_page(request, 'registration/signup.html', {'form': form})