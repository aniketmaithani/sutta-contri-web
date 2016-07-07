For api overview and usages, check out [this page](overview.md).

API Contains the following end-point

## /api/suttacontri


```
Call Type : POST
```

## POST DATA 

``` 
data type : application/json

  data = {
        "name": "test",
        "brand_of_cig": "test",
        "number_of_cig": "test",
        "money_given": "100.00"
    }
```

## Response 

``` 
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "test",
    "brand_of_cig": "test",
    "number_of_cig": "test",
    "money_given": "100.00"
}
```


