from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Demo bus route data
ROUTES = {
    ("Majestic", "Shivajinagar"): {
        "bus_number": "201",
        "travel_time": "20 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 15,
        "stops": ["Majestic", "Cubbon Park", "Shivajinagar"]
    },

    ("Shivajinagar", "Majestic"): {
        "bus_number": "201",
        "travel_time": "20 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 15,
        "stops": ["Shivajinagar", "Cubbon Park", "Majestic"]
    },

    ("Majestic", "Indiranagar"): {
        "bus_number": "500K",
        "travel_time": "30 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 20,
        "stops": ["Majestic", "Shivajinagar", "Ulsoor", "Indiranagar"]
    },

    ("Indiranagar", "Majestic"): {
        "bus_number": "500K",
        "travel_time": "30 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 20,
        "stops": ["Indiranagar", "Ulsoor", "Shivajinagar", "Majestic"]
    },

    ("Majestic", "Whitefield"): {
        "bus_number": "500D",
        "travel_time": "60 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Majestic", "Shivajinagar", "Ulsoor",
            "Indiranagar", "KR Puram", "Hoodi", "Whitefield"
        ]
    },

    ("Whitefield", "Majestic"): {
        "bus_number": "500D",
        "travel_time": "60 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Whitefield", "Hoodi", "KR Puram",
            "Indiranagar", "Ulsoor", "Shivajinagar", "Majestic"
        ]
    },

    ("Majestic", "Electronic City"): {
        "bus_number": "356",
        "travel_time": "75 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 35,
        "stops": [
            "Majestic", "Richmond Road", "Shanthinagar",
            "Madiwala", "Silk Board", "Bommanahalli", "Electronic City"
        ]
    },

    ("Electronic City", "Majestic"): {
        "bus_number": "356",
        "travel_time": "75 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 35,
        "stops": [
            "Electronic City", "Bommanahalli", "Silk Board",
            "Madiwala", "Shanthinagar", "Richmond Road", "Majestic"
        ]
    },

    ("Majestic", "Yeshwanthpur"): {
        "bus_number": "252",
        "travel_time": "40 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 25,
        "stops": [
            "Majestic", "Malleshwaram", "Rajajinagar",
            "Mahalakshmi", "Yeshwanthpur"
        ]
    },

    ("Yeshwanthpur", "Majestic"): {
        "bus_number": "252",
        "travel_time": "40 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 25,
        "stops": [
            "Yeshwanthpur", "Mahalakshmi", "Rajajinagar",
            "Malleshwaram", "Majestic"
        ]
    },

    ("Shivajinagar", "Indiranagar"): {
        "bus_number": "201",
        "travel_time": "30 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 20,
        "stops": ["Shivajinagar", "Ulsoor", "Indiranagar"]
    },

    ("Indiranagar", "Shivajinagar"): {
        "bus_number": "201",
        "travel_time": "30 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 20,
        "stops": ["Indiranagar", "Ulsoor", "Shivajinagar"]
    },

    ("Shivajinagar", "Whitefield"): {
        "bus_number": "500D",
        "travel_time": "55 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Shivajinagar", "Ulsoor", "Indiranagar",
            "KR Puram", "Hoodi", "Whitefield"
        ]
    },

    ("Whitefield", "Shivajinagar"): {
        "bus_number": "500D",
        "travel_time": "55 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Whitefield", "Hoodi", "KR Puram",
            "Indiranagar", "Ulsoor", "Shivajinagar"
        ]
    },

    ("Shivajinagar", "Electronic City"): {
        "bus_number": "356",
        "travel_time": "70 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 35,
        "stops": [
            "Shivajinagar", "Richmond Road", "Shanthinagar",
            "Madiwala", "Silk Board", "Electronic City"
        ]
    },

    ("Electronic City", "Shivajinagar"): {
        "bus_number": "356",
        "travel_time": "70 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 35,
        "stops": [
            "Electronic City", "Silk Board", "Madiwala",
            "Shanthinagar", "Richmond Road", "Shivajinagar"
        ]
    },

    ("Shivajinagar", "Yeshwanthpur"): {
        "bus_number": "252",
        "travel_time": "45 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 25,
        "stops": [
            "Shivajinagar", "Majestic", "Malleshwaram",
            "Rajajinagar", "Yeshwanthpur"
        ]
    },

    ("Yeshwanthpur", "Shivajinagar"): {
        "bus_number": "252",
        "travel_time": "45 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 25,
        "stops": [
            "Yeshwanthpur", "Rajajinagar",
            "Malleshwaram", "Majestic", "Shivajinagar"
        ]
    },

    ("Indiranagar", "Whitefield"): {
        "bus_number": "500D",
        "travel_time": "40 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 25,
        "stops": [
            "Indiranagar", "KR Puram", "Hoodi", "Whitefield"
        ]
    },

    ("Whitefield", "Indiranagar"): {
        "bus_number": "500D",
        "travel_time": "40 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 25,
        "stops": [
            "Whitefield", "Hoodi", "KR Puram", "Indiranagar"
        ]
    },

    ("Indiranagar", "Electronic City"): {
        "bus_number": "500C",
        "travel_time": "60 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Indiranagar", "Koramangala",
            "Madiwala", "Silk Board", "Electronic City"
        ]
    },

    ("Electronic City", "Indiranagar"): {
        "bus_number": "500C",
        "travel_time": "60 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Electronic City", "Silk Board",
            "Madiwala", "Koramangala", "Indiranagar"
        ]
    },

    ("Indiranagar", "Yeshwanthpur"): {
        "bus_number": "500K",
        "travel_time": "50 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Indiranagar", "Ulsoor", "Majestic",
            "Malleshwaram", "Yeshwanthpur"
        ]
    },

    ("Yeshwanthpur", "Indiranagar"): {
        "bus_number": "500K",
        "travel_time": "50 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 30,
        "stops": [
            "Yeshwanthpur", "Malleshwaram",
            "Majestic", "Ulsoor", "Indiranagar"
        ]
    },

    ("Whitefield", "Electronic City"): {
        "bus_number": "500C",
        "travel_time": "85 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 40,
        "stops": [
            "Whitefield", "KR Puram", "Indiranagar",
            "Madiwala", "Silk Board", "Electronic City"
        ]
    },

    ("Electronic City", "Whitefield"): {
        "bus_number": "500C",
        "travel_time": "85 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 40,
        "stops": [
            "Electronic City", "Silk Board", "Madiwala",
            "Indiranagar", "KR Puram", "Whitefield"
        ]
    },

    ("Whitefield", "Yeshwanthpur"): {
        "bus_number": "500D",
        "travel_time": "75 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 35,
        "stops": [
            "Whitefield", "Hoodi", "KR Puram",
            "Majestic", "Malleshwaram", "Yeshwanthpur"
        ]
    },

    ("Yeshwanthpur", "Whitefield"): {
        "bus_number": "500D",
        "travel_time": "75 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 35,
        "stops": [
            "Yeshwanthpur", "Malleshwaram",
            "Majestic", "KR Puram", "Hoodi", "Whitefield"
        ]
    },

    ("Electronic City", "Yeshwanthpur"): {
        "bus_number": "356",
        "travel_time": "90 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 40,
        "stops": [
            "Electronic City", "Silk Board", "Madiwala",
            "Shanthinagar", "Majestic",
            "Malleshwaram", "Yeshwanthpur"
        ]
    },

    ("Yeshwanthpur", "Electronic City"): {
        "bus_number": "356",
        "travel_time": "90 minutes",
        "bus_type": "BMTC Ordinary",
        "fare": 40,
        "stops": [
            "Yeshwanthpur", "Malleshwaram",
            "Majestic", "Shanthinagar",
            "Madiwala", "Silk Board", "Electronic City"
        ]
    }
}


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/route")
def find_route():

    start = request.args.get("from")
    destination = request.args.get("to")

    if not start or not destination:
        return jsonify({
            "error": "Please select both From and To locations."
        }), 400

    if start == destination:
        return jsonify({
            "error": "Starting point and destination cannot be the same."
        }), 400

    route = ROUTES.get((start, destination))

    if route is None:
        return jsonify({
            "error": f"No route available from {start} to {destination}."
        }), 404

    result = route.copy()
    result["from"] = start
    result["to"] = destination

    return jsonify(result)


if __name__ == "__main__":

    print("===================================")
    print("        BUS ROUTE FINDER")
    print("===================================")
    print("Server running at:")
    print("http://127.0.0.1:5000")
    print("===================================")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )