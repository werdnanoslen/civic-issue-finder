# -------------------
# Imports
# -------------------

from flask import Flask, render_template, request
import json
from requests import get
from requests.exceptions import ConnectionError

# -------------------
# Init
# -------------------

app = Flask(__name__)

# -------------------
# Routes
# -------------------

@app.route('/')
def index():
  org_name = request.args.get('organization_name')
  default_labels = request.args.get('default_labels')
  return render_template('index.html', org_name=org_name, default_labels=default_labels, main=True)

@app.route('/find', methods=['POST'])
def find():
  '''
  Finds issues based on the given label
  '''
  # Get optional parameters
  org_name = request.form.get('org_name', None)
  default_labels = request.form.get('default_labels', None)

  # Get labels from form
  labels = request.form['labels']
  labels.replace(' ', '')

  # Include optional labels
  if default_labels != 'None':
    default_labels.replace(' ', '')
    labels += ',' + default_labels

  try:
    # If we have an organization name only query that organization
    if org_name != 'None':
      issues = get('http://codeforamerica.org/api/organizations/%s/issues/labels/%s?per_page=100' % (org_name, labels))
    # Otherwise get issues across all organizations
    else:
      issues = get('http://codeforamerica.org/api/issues/labels/'+labels+'?per_page=100')
  except ConnectionError, e:
    return render_template('index.html', org_name=org_name, default_labels=default_labels, error=True)

  if issues.status_code != 200:
    return render_template('index.html', org_name=org_name, default_labels=default_labels, error=True)

  # Parse the API response
  issues = json.loads(issues.content)

  return render_template('index.html', issues=issues['objects'], labels=request.form['labels'], org_name=org_name, default_labels=default_labels)


if __name__ == "__main__":
    app.run(debug=True, port=4000)