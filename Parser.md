# Ingredient Parser

This parser takes an ingredient as a string and returns structured data.

Please notice that input string is assumed to be valid. 

For example "3 g of sugar" returns an json object:
```python
{"item":"sugar","number":"3","unit":"gram"}
```

To run this example
- Run `python run_parser.py`
- Then curl with the ingredient:
```
curl -X POST -H "Content-Type: application/json" --data "{\"input_string\":\"3 g of sugar\", \"invalid\": 3}" http://127.0.0.1:8122/parse/ingredient
```

For questions, please contact Hao Chen.