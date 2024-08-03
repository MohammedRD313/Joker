import os
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        response = {
            "message": "𝗦𝗰𝗼𝗿𝗽𝗶𝗼 𝘄𝗼𝗿𝗸𝘀 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅"
        }
        return jsonify(response)

class HealthCheck(Resource):
    def get(self):
        return jsonify({"status": "healthy"})

api.add_resource(Greeting, '/')
api.add_resource(HealthCheck, '/health')

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)  # قم بإيقاف التشغيل debug في الإنتاج
