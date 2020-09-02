import pytest
import tasks
from task import Task


@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after.
    Args:
        tmpdir: 
    """
    # setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # this is where the testing happens

    # Teardown : stop db 
    tasks.stop_tasks_db()
    
    