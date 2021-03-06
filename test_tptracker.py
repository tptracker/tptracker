import pytest
import tptracker


def test_data_extractor_v1() -> None:
    """ Checks the function for normal data"""
    file = "test_data.csv"
    actual = tptracker.data_extractor(file)
    expected = {'Location': 'Current Status',
                'Room1': True,
                'Room2': True,
                'Room 3': True,
                'Room 4': False,
                'Room 5': False,
                }
    assert actual == expected


if __name__ == '__main__':
    import pytest

    pytest.main(['test_tptracker.py'])
