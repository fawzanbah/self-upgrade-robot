from flask import Flask, request, jsonify
from self_upgrade_robot import SelfUpgradeRobot

app = Flask(__name__)
robot = SelfUpgradeRobot()

@app.route("/")
def home():
    return "🤖 Self-Upgrade Robot Ready!"

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    cmd = data.get("command", "").lower()

    # --- MAIN SELF UPGRADE ---
    if cmd == "upgrade":
        robot.self_update("https://github.com/fawzanbah/self-upgrade-robot.git")
        return jsonify({"message": "✅ Robot updated!"})

    # --- FRONTEND UPGRADE COMMAND ---
    if cmd == "upgrade frontend":
        robot.download_feature(
            "https://raw.githubusercontent.com/fawzanbah/self-upgrade-robot/main/frontend.html",
            "frontend.html"
        )
        return jsonify({"message": "🟦 Frontend upgraded!"})

    # --- ADD UI BOX COMMAND ---
    if cmd == "add box":
        robot.download_feature(
            "https://raw.githubusercontent.com/fawzanbah/self-upgrade-robot/main/ui_box.html",
            "ui_box.html"
        )
        return jsonify({"message": "📦 UI box added!"})

    return jsonify({"message": "❌ Unknown command."})

if __name__ == "_main_":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)