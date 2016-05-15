import webapp2, jinja2
import os, sys
import json

#import graph

import arithmetic, sample_template, differentiation, physics, areaVolume, relatedRates, riemann, optimization

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
                payload = arithmetic.generate(pType, ranges)

            #check if a word problem
            elif pType in sample_template.appliesTo:
                payload = sample_template.generate()

            #check if differentiation
            elif pType in differentiation.appliesTo:
                degree = int(self.request.get("degree", default_value="5"))
                payload = differentiation.generate(degree)

            elif pType in physics.appliesTo:
                payload = physics.generate()

            elif pType in areaVolume.appliesTo:
                maximum = int(self.request.get("max", default_value="3"))
                minimum = int(self.request.get("min", default_value="1"))
                payload = areaVolume.generate(minimum, maximum)
            elif pType in relatedRates.appliesTo:
                payload = relatedRates.generate()
            elif pType in riemann.appliesTo:
                payload = riemann.generate()
            elif pType in optimization.appliesTo:
                payload = optimization.generate()
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