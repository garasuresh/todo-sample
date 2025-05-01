from flask import Flask

app = Flask(__name__)

data = {
  1: {"task": "Learn python", "done": False},
  2: {"task": "Build todo", "done": False}
}

# @app.route("/todos", methods=["GET"])
# def get_todos():
#   response = []
#   for key, value in data.items():
#     temp = value
#     temp["id"] = key 
#     response.append(temp)
#   return response

@app.route("/todos/<int:id>", methods=["GET"])
def get_todo(id): 
  return data[id]


if __name__ == '__main__':
  app.run(debug=True)