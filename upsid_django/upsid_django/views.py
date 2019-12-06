from django.shortcuts import render
from django.http import HttpResponse
from .models import Langues, Branches, LanguesBranches, LanguesGeolocalisation, Phonemes, PhonemesLangues


def accueil(request) :
    return render(request, "upsid_django/Shield/index.html")
    #return HttpResponse("ok")

def display_map(request):
    #récupérer le code upsid de toutes les langues de nos tables
    langues = Langues.objects
    liste_upsid = []
    liste_langues = []
    for langue in langues.all():
        liste_langues.append(langue.nom)
        liste_upsid.append(langue.upsid)

    #récupérer les géolocalisations des tables
    #geoloc = LanguesGeolocalisation.objects
    #langue_geoloc = {}
    #for upsid in liste_upsid:
        #liste_geoloc_selon_upsid = []
        #for loc in geoloc.all():
            #print(str(loc.upsid).strip("Langues object (").strip(")"), str(upsid), type(loc.upsid), type(upsid))
            #if str(loc.upsid).strip("Langues object (").strip(")") == str(upsid):
                #liste_geoloc_selon_upsid.append(loc.geolocalisation)
        #langue_geoloc[upsid]=liste_geoloc_selon_upsid
        #{'dico_upsid_loc':langue_geoloc}
    #return render(request, "upsid_django/test.html", {'langues':liste_langues, 'liste_upsid':liste_upsid})
    return render (request, "upsid_django/maCarte.html", {'liste_langues':liste_upsid, 'langues':liste_langues})

def display_info_langue(request):
    return render(request, "upsid_django/matrix-admin-master/tables.html")
