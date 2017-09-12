from deep_mapper import process_mapping
from djmodel_filler.utils import xmlparser
from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import Q
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **options):
        # we store the data locally, but you can convert
        # and receive each time new via url
        PATH_TO_SOURCE = '{}/simple_app/external_sources/afisha.xml'.format(settings.BASE_DIR)

        # basic structure that stores all the necessary
        # information to perform the mapping
        map_order = [
            {
                'model': 'simple_app.Event',
                'map': {
                    'external_id': {'path': '/@id'},
                    'title': {'path': '/title'},
                    'type': {'path': '/@type'},
                    'description': {'path': '/text'},
                    'short_description': {'path': '/description'},
                    'tags': {'path': '/tags/tag', 'postprocess': lambda x: ', '.join(x)},
                    'persons': {'path': '/persons/person'},
                    'image_source': {'path': '/gallery/image/@href'},
                    'duration': {'path': '/runtime', 'postprocess': int},
                    'legal_age': {'path': '/age_restricted', 'postprocess': lambda x: int(x.replace('+', ''))},
                },
                'root': '/feed/events/event',
                'source': PATH_TO_SOURCE,
            },
            {
                'model': 'simple_app.Place',
                'map': {
                    'external_id': {'path': '/@id'},
                    'name': {'path': '/title'},
                    'city': {'path': '/city'},
                    'address': {'path': '/address'},
                    'tags': {'path': '/tags/tag', 'postprocess': lambda x: ', '.join(x)},
                    'image_source': {'path': '/gallery/image[0]/@href'},
                    'about': {'path': '/text'},
                    'url': {'path': '/url'},
                },
                'root': '/feed/places/place',
                'source': PATH_TO_SOURCE,
            },
            {
                'model': 'simple_app.Schedule',
                'map': {
                    'event': {'path': '/@event'},
                    'place': {'path': '/@place'},
                    'starts': {'path': '/@date', 'postprocess': date},
                },
                'root': '/feed/schedule/session',
                'source': PATH_TO_SOURCE,
                'related': {
                    'event': {'model': 'simple_app.Event', 'determine_field': 'external_id'},
                    'place': {'model': 'simple_app.Place', 'determine_field': 'external_id'},
                }
            }
        ]


        sources = {}
        for map_line in map_order:

            # it's a controversial question whether it is necessary to store
            # large data objects in memory or load them every time if necessary
            # - I decided to save in memory cuz I know that my file is same for each structure
            path_hash = hash(map_line['source'])
            data = sources.get(path_hash, xmlparser(map_line['source']))
            if path_hash not in sources:
                sources[path_hash] = data

            model = apps.get_model(*map_line['model'].split('.'))
            mapping_result = process_mapping(data, map_line['map'], map_line.get('root', ''))

            for item in mapping_result:
                if 'related' in map_line:
                    # generator is better than if statment inside full-for-cycle
                    related_item_keys = ((key, value) for key, value in iter(item.items()) if
                                         key in map_line['related'])

                    # related fields will be re-placed with actual element-relations from database
                    for key, value in related_item_keys:
                        rel_model = apps.get_model(*map_line['related'][key]['model'].split('.'))
                        item[key] = rel_model.objects.filter(
                            Q(**{map_line['related'][key]['determine_field']: value})).first()

                # block that saves each element is not didnt presented
                # written based on external_id as hardcode, but will be
                # re-written later as part of map_options
                if not model.objects.filter(external_id=item.get('external_id', -1)):
                    model.objects.create(**item)