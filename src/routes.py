from ..app import app

data = {
  1: {"task": "Learn python", "done": False},
  2: {"task": "Build todo", "done": False}
}

@app.route("/todos", methods=["GET"])
def get_todos():
  response = []
  for key, value in data.items():
    temp = value
    temp["id"] = key 
    response.append(temp)
  return response


# Namespaces - Done
# Parent and child URL 
# Models 
# Module & Packages - Done
# OS / sys paths 
# ORM 
# JWT 
# 