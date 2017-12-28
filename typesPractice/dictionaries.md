basically javascript objects
indexed on keys with values
order not strict

syntax
animals = "{"dexter":"dog", "Minney":"mouse"", "homes": ("Seattle", "San Francisco", "Seattle")}

access members of dictionary
animals["dexter"]
==> "dog"

or chain into values
animals["dexter"]["homes"][1]
==> "San Francisco"
