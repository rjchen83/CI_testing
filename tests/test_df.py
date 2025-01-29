import pytest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import df

@pytest.fixture
def data_frame():
    return df

def test_data_frame(data_frame):
    assert data_frame.shape == (3, 2)
    assert data_frame.columns.tolist() == ['A', 'B']
    assert data_frame['A'].tolist() == [1, 2, 3]
    assert data_frame['B'].tolist() == [4, 5, 6]

def test_data_frame2(data_frame):
    assert data_frame.shape == (3, 2)
    assert data_frame.columns.tolist() == ['A', 'B']
    assert data_frame['A'].tolist() == [1, 2, 4]
    assert data_frame['B'].tolist() == [4, 5, 6]