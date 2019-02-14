# Ingredient Parser
## Problem
We need a parser that will return structured ingredient data given an ingredient string.
More specifically, the ingredient parser should run as an http service and be
able to reliably handle 1000 parsing requests per second, even on commodity hardware.


For the purpose of expediency and simplicity, assume that we only care about the following
units of measure: cups, teaspoons, and grams. For each measurement we should be able to
parse their names and abbreviations in a case-insensitive way. A non-exhaustive list of 
labels and abbreviations to support are as follows:
- Cup, cups, C., c., c
- Teaspoons, teaspoon, Tsp, tsp., tsp
- Gram, grams, gram, g, g.

Your parser should be able to process strings in the formats of the examples below:
- 1 cup sugar
- 4 tsp. Orange Juice
- 5 eggs
- 5 cups of salt
- salt and pepper to taste
- 1 teaspoon vanilla extract
- 500 g all-purpose flour
- 3.5 GRAMS xanthum gum 
- 20 cups chopped onions
- 50 grams grampa's potato slaw


All strings passed to the parser are assumed to be valid ingredients, and the
parser shouldn't need to worry about accepting empty strings or other data types.

## Resolution
A successful solution will accept a request over http as input and return an `Ingredient` as
output. The specification of the `Ingredient` datatype and the way requests are formed 
are up to your discretion. 
