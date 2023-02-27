from ckan import plugins as p
from ckan.plugins import interfaces as i
import logging

logger = logging.getLogger(__name__)

class FixedSearchPlugin(p.SingletonPlugin):
    p.implements(i.IPackageController, inherit=True)
    
    def before_dataset_search(self, search_params):
        q = search_params['q']
        title = 'title:'
        text = 'text:'
        star = '*'
        
        if str(q).startswith(title) and str(q).endswith(star):
            return search_params
        
        elif str(q).startswith(text) and str(q).endswith(star):
            return search_params
        
        else:
            modified_q = title + q + star
            search_params['q'] = modified_q
            logger.info('Searched string was modified')
            return search_params
