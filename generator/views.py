import os
import random
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

def home(request):
    nb_names = min(int(request.GET.get('n', 0)), settings.MAX_NAMES)

    if nb_names <= 0:
        nb_names = 50

    first_names_file = open(os.path.join(settings.BASE_PATH, 'generator/names/fr/first_names.txt'), 'r')
    first_names = first_names_file.readlines()
    first_names_file.close()

    last_names_file = open(os.path.join(settings.BASE_PATH, 'generator/names/fr/last_names.txt'), 'r')
    last_names = last_names_file.readlines()
    last_names_file.close()

    names = set()

    while len(names) < nb_names:
        names.add('%s %s' % (random.choice(first_names).strip(),
                             random.choice(last_names).strip()))

    return render_to_response('names.html',
                              {
                                'names': names,
                                'nb_names': nb_names
                              },
                              RequestContext(request))
