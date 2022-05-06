from django.test import TestCase
from .models import INDICATOR_TASK, Task

# Create your tests here.
class TaskModelTest(TestCase):

    def test_displays_sort_detail(self):
        """
        sort_description() return a short text of detail with three dots at the end
        """
        task = Task(title='Do Something Better', 
        detail='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nulla nunc, semper eu eros dictum, tristique dictum odio. Phasellus lacinia risus at nulla sodales semper. Pellentesque imperdiet, ante vitae ultrices fermentum, sapien est consequat leo, a hendrerit nulla ante at elit. Fusce vel lacus id libero egestas venenatis. Aliquam erat volutpat. Aenean euismod nisi felis, nec imperdiet turpis ultricies non. Mauris arcu metus, vestibulum in est mollis, venenatis fringilla nisl.', 
        indicator='Normal')
        
        self.assertEqual(len(task.sort_description()), 70)
        self.assertEqual(task.sort_description(), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nulla...')
        