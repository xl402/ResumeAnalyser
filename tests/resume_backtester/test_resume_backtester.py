import pandas as pd

from resume_backtester.backtester import BackTester
from resume_analyser import ResumeAnalyser


def test_backtester(backtest_data_dir):
    analyser = ResumeAnalyser()
    backtester = BackTester(backtest_data_dir)
    results = backtester.run(analyser, regret_threshold=7.0)
    assert isinstance(results.catastrophic_loss, float)
    assert isinstance(results.score, float)
