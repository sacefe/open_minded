#!/usr/bin/env python

import pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

pytest.main(['-v'])