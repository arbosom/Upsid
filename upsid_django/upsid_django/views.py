from django.shortcuts import render
from django.http import HttpResponse
from .models import Langues, Branches, LanguesBranches, LanguesGeolocalisation, Phonemes, PhonemesLangues


def accueil(request) :
    return render(request, "upsid_django/Shield/index.html")
    return HttpResponse("ok")

def display_map(request):
    #récupérer le code upsid de toutes les langues de nos tables
    langues = Langues.objects
    liste_upsid = []
    for langue in langues.all():
        liste_upsid.append(langue.upsid)
    #récupérer les géolocalisations des tables
    geoloc = LanguesGeolocalisation.objects
    langue_geoloc = {}
    for upsid in liste_upsid:
        liste_geoloc_selon_upsid = []
        for loc in geoloc.all():
            #print(str(loc.upsid).strip("Langues object (").strip(")"), str(upsid), type(loc.upsid), type(upsid))
            if str(loc.upsid).strip("Langues object (").strip(")") == str(upsid):
                liste_geoloc_selon_upsid.append(loc.geolocalisation)
        langue_geoloc[upsid]=liste_geoloc_selon_upsid
    #return render(request, "upsid_django/test.html", {'dico_upsid_loc':langue_geoloc, 'liste_upsid':liste_upsid})
    return render (request, "upsid_django/themekit-master/index.html", {'liste_langues':liste_langues, 'dico_upsid_loc':langue_geoloc})
"""
    if '<langue>' in request.GET:
        #return render (request, "upsid_django/themekit-master/index.html", {'liste_langues':liste_langues, 'dico_upsid_loc':langue_geoloc})
        return HttpResponse("ok")
"""
def display_info_langue(request):
    if '<langue>' in request.GET: #si le bouton X (de la barre de recherche) est cliqué
        #####
        #return render(request, "upsid_django/matrix-admin-master/tab.html")
        return HttpResponse("ok")

    else:
        #return render(request, "upsid_django/matrix-admin-master/tab.html")
        return HttpResponse("ok")
