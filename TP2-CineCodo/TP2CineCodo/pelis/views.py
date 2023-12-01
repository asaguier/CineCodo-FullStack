from django.shortcuts import render
from .models import Peli
#from .models import Proxima
#from .models import Estreno

# Create your views here.

def home(request):
#    return HttpResponse(html_base + "<h1>H1 Pagina principal</h1> <h2>H2 Prueba</h2>")
    pelis=Peli.objects.all ()
#    print(pelis)
#    proximas=Proxima.objects.all ()
#    print(proximas)
#    estrenos=Estreno.objects.all ()
#    print(estrenos)
#    render(request, "pelis/index.html", {'pelis':pelis})
#    render(request, "pelis/index.html", {'proximas':proximas})
#    render(request, "pelis/index.html", {'estrenos':estrenos})
#    return render(request, "pelis/index.html", {'pelis':pelis}, {'estrenos':estrenos}, {'proximas':proximas}
    return render(request, "pelis/index.html", {'pelis':pelis})