import logging
from multiprocessing import cpu_count
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__file__)


def test_random_choice():
    # given
    choice_list = ['ice cream', 'candy']

    # when 
    result = random.choice(choice_list)

    # then
    assert result in choice_list
    logger.info(result)


def test_cpu_count():
    # when
    result = cpu_count()

    # then
    assert result >= 1
    logger.info(result)
