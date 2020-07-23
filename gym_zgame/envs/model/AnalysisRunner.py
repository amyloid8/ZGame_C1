import os
import json
import argparse
from ZGameHumanPlay import ZGame
from ZGameAnalyze import Analyzer

if __name__ == '__main__':
    analyzer = Analyzer('data_log.json')
    analyzer.get_categories()
    analyzer.get_category_data('reward')