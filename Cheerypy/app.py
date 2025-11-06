import cherrypy

class HelloApp:
    @cherrypy.expose
    def index(self):
        return "<h1>Welcome to CheeryPy</h1>"
    @cherrypy.expose
    def greet(self,name="Guest"):
        return f'<h1>Hello,{name}</h1>'

if __name__=="__main__":
    cherrypy.quickstart(HelloApp(),'/')