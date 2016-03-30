import webapp2
import os
import sys
import json
import jinja2

import arithmetic
import sample_template

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            self.response.headers['Content-Type'] = 'application/json'
            pType = self.request.get("type").lower()

            #Check if it's arithmetic and do the arithmetic stuff.
            if pType in arithmetic.appliesTo:
                ranges = int(self.request.get("range", default_value="100"))
                payload = arithmetic.arithmetic(pType, ranges)

            #check if a word problem
            if pType in sample_template.appliesTo:
                payload = sample_template.wordProblem()

            self.response.write(json.dumps(payload, indent=4, sort_keys=True))

        #Is there some error? Throw up the home page.
        except Exception as exception:
            self.response.headers['Content-Type'] = 'text/html'
            exception2 = sys.exc_info()[0]

            template = JINJA_ENVIRONMENT.get_template('errorpage.html')
            self.response.write(template.render(exception=exception, exception2=exception2))
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=False)