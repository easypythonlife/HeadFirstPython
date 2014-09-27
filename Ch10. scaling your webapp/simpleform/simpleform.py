#import wsgiref.handlers

#from google.appengine.ext import webapp
import webapp2
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext.db import djangoforms

import birthDB

#class BirthDetailsForm(djangoforms.ModelForm):
#    class Meta:
#        model = birthDB.BirthDetails

class IndexPage(webapp2.RequestHandler):
    def get(self):
        html = template.render('templates/header.html', {'title': 'Provide your birth details'})
        html = html + template.render('templates/form_start.html', {})
#        html = html + str(BirthDetailsForm(auto_id=False))
        html = html + """
                <tr><th>Name:</th><td><input type="text" name="name" /></td></tr>
                <tr><th>Date of Birth:</th><td><input type="text" name="date_of_birth" /></td></tr>
                <tr><th>Time of Birth:</th><td><input type="text" name="time_of_birth" /></td></tr>
        """
        html = html + template.render('templates/form_end.html', {'sub_title': 'Submit Details'})
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

app = webapp2.WSGIApplication([('/.*', IndexPage)], debug=True)

run_wsgi_app(app)
#def main():
#    run_wsgi_app(app)
#
#if __name__ == '__main__':
#    main()