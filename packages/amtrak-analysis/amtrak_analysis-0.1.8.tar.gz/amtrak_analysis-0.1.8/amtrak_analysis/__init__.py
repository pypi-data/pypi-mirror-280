from .analysis import AmtrakAnalysis

def run_analysis(csv_path, n_valid=36):
    analysis = AmtrakAnalysis(csv_path)
    analysis.run_analysis(n_valid)