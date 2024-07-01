from jsonschema import validate, ValidationError


def validate_json(data, schema):
  """
  Validates JSON data against a given schema.

  Parameters:
    data (dict): The JSON data to validate.
    schema (dict): The JSON schema to validate against.

  Returns:
    tuple: A tuple containing a boolean indicating validity and an error message if invalid.
  """
  
  try:
    validate(instance=data, schema=schema)
    
    return True, None
  except ValidationError as e:
    return False, e.message
