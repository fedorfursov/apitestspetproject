current_weather_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "weather": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "main": {"type": "string"},
                    "description": {"type": "string"},
                },
                "required": ["main", "description"]
            }
        },
        "main": {
            "type": "object",
            "properties": {
                "temp": {"type": "number"},
                "pressure": {"type": "number"},
                "humidity": {"type": "number"}
            },
            "required": ["temp", "pressure", "humidity"]
        }
    },
    "required": ["name", "weather", "main"]
}