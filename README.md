# Ingredient Parser
This parser takes an ingredient as a string and returns structured data.

For example "1 Cup oatmeal" returns an `Ingredient` object:
```python
{"n": 1,
 "u": "cup",
 "f": "oatmeal"}
```

To run this example, run `python run_parser.py`, then curl with the ingredient:
```curl http://127.0.0.1:5000/?ing=1 cup oatmeal```
