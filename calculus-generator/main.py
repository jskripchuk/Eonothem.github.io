import webapp2, jinja2
import os, sys
import json

#import graph

import arithmetic, sample_template

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.headers['Access-Control-Allow-Origin'] = '*'
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

#class Images(webapp2.RequestHandler):
#    def get(self):
#        f = self.request.get("f")
#        self.response.write("<img src='%s'/>" % graph.graph(f))
        
app = webapp2.WSGIApplication([
    ('/', MainHandler)#,
    #('/images', Images)
], debug=True)