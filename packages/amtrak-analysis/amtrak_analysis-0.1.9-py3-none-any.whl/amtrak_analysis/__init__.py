import pkg_resources
from .analysis import AmtrakAnalysis

def run_analysis(csv_path=None, n_valid=36):
    if csv_path is None:
        csv_path = pkg_resources.resource_filename(__name__, 'data/Amtrak.csv')
    analysis = AmtrakAnalysis(csv_path)
    analysis.run_analysis(n_valid)