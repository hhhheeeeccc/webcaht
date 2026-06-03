import pytest
from aura.backend.engine import AuraEngine

def test_check_slow_queries():
    engine = AuraEngine("test-proj", "test-team")
    slow_data = [
        {"datname": "db1", "query": "SELECT *", "mean_exec_time": 600},
        {"datname": "db2", "query": "SELECT 1", "mean_exec_time": 10}
    ]
    incidents = engine.check_slow_queries(slow_data)
    assert len(incidents) == 1
    assert incidents[0]["title"] == "AUR-SQL: Slow Query Detected"

def test_process_flow():
    engine = AuraEngine("test-proj", "test-team")
    slow_data = [{"datname": "db1", "query": "SELECT *", "mean_exec_time": 1000}]
    results = engine.process(slow_data)
    assert len(results) == 1
    assert results[0]["reported"] is True

def test_no_incidents():
    engine = AuraEngine("test-proj", "test-team")
    fast_data = [{"datname": "db1", "query": "SELECT 1", "mean_exec_time": 5}]
    incidents = engine.check_slow_queries(fast_data)
    assert len(incidents) == 0
