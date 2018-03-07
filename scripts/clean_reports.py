"""
Remove files/folders for improperly created reports.
"""
import os
import shutil


repo_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
reports_dir = os.path.join(repo_dir, 'assets', 'reports')
for report in os.listdir(reports_dir):
    if not os.path.exists(os.path.join(repo_dir, '%s.md' % report)):
        repdir = os.path.join(reports_dir, report)
        print('Deleting report -> %s' % repdir)
        shutil.rmtree(repdir)
