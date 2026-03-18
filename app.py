from flask import Flask, request, jsonify

app = Flask(__name__)

FILE_NAME = "students.txt"

@app.route('/')
def home():
    return "Student Manager API Running!"

@app.route('/students', methods=['GET'])
def get_students():
    students = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                name, age, course = line.strip().split(",")
                students.append({
                    "name": name,
                    "age": age,
                    "course": course
                })
    except FileNotFoundError:
        pass

    return jsonify(students)

@app.route('/add', methods=['POST'])
def add_student():
    data = request.json

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{age},{course}\n")

    return jsonify({"message": "Student added successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)