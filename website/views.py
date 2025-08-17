from django.shortcuts import render

def home(request):
    """Renderiza a página inicial (home)."""
    return render(request, 'website/index.html')

def sobre(request):
    """Renderiza a página 'sobre'."""
    return render(request, 'website/sobre.html')

def contato(request):
    """Renderiza a página de contato."""
    return render(request, 'website/contato.html')