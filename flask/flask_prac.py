from flask import Flask

app = Flask(__name__)

# Route Decorator - Tell Flask which url should trigger our function
# <name> is a placeholder...you can put anystring here and it will become route name 
@app.route("/<name>")
def hello_world(name):
	if name != "Christopher":
		return "Wrong Name!"
	else:
		return f"Hello {name}"

@app.route("/about")
def about():
    return {
        "about": "Part 1 of flask tutorial..." 
    }

@app.route("/projects")
def projects():
	return {
		"status": "This is a new project..."
	}

# Add 0.0.0.0 so flask can listen on the network 
app.run(host="0.0.0.0",port=5000, debug=True)
