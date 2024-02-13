import os
import json

from dataclasses import dataclass
import fitz


class BackTester():
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self._check_data_dir()
        self.resumes = self._load_resumes(data_dir)
        self.ground_truth = self._load_ground_truth(data_dir)

    def run(self, analyser, regret_threshold):
        results = {f_name: analyser.run(resume) for f_name, resume in self.resumes.items()}
        results = BackTesterResults(results, regret_threshold)
        return results

    def _load_resumes(self, data_dir):
        pdfs = [f for f in os.listdir(data_dir) if f.endswith('.pdf')]
        resumes = {pdf: read_pdf(os.path.join(data_dir, pdf)) for pdf in pdfs}
        return resumes

    def _load_ground_truth(self, data_dir):
        ground_truth = read_json_file(os.path.join(data_dir, 'ground_truth.json'))
        return ground_truth

    def _check_data_dir(self):
        assert 'ground_truth.json' in os.listdir(self.data_dir)
        ground_truth = read_json_file(os.path.join(self.data_dir, 'ground_truth.json'))
        pdfs = [f.replace('.pdf', '') for f in os.listdir(self.data_dir) if f.endswith('.pdf')]
        for pdf in pdfs:
            assert pdf in ground_truth, f'No ground truth for {pdf}'
            assert isinstance(ground_truth[pdf], float)


class BackTesterResults():
    def __init__(self, results, regret_threshold):
        self.results = results
        self.regret_threshold = regret_threshold

    @property
    def catastrophic_loss(self):
        return self.regret_threshold

    @property
    def score(self):
        return self.regret_threshold


def read_json_file(fname):
    with open(fname, 'r') as f:
        return json.load(f)


def read_pdf(fname):
    pdf = fitz.open(fname)
    return pdf
