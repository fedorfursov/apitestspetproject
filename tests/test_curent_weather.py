import pytest
from jsonschema import validate, ValidationError
from  schemas import weather_schemas

def test_get_current_weather_with_coords(weather_client):
    lat = 51.51
    lon = -0.13

    response = weather_client.get_current_weather(lat, lon)

    assert response["name"] == "London"
    assert "weather" in response
    assert "main" in response
    assert response["main"]["temp"] is not None

    try:
        validate(instance=response, schema=weather_schemas.current_weather_schema)
    except ValidationError as e:
        pytest.fail(f"Структура ответа не соответствует схеме: {e.message}")