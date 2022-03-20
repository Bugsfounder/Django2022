## Number of Slide Calculation
```
from math import ceil
```
```
nSlides = n//4 + ceil((n/4)-(n//4))
```
```
products = Product.objects.all() # fetch all data from database
n = len(products) # length of products
nSlides = n//4 + ceil((n/4)-(n//4))
```

## Slicing in Jinja
```
# <Array>|slice:"<START_INDEX>:<END_INDEX>"
```
    products|slice:"1:"
```
products|slice:"1:" # products[1:]
products|slice:"0:3" # products[0:3]
```
```
{% for i in products|slice:"1:" %}
    .
    .
    .
{% endfor %}
```

## Create Generator Using Range Function
```
range(<FROM>, <TO>)
range(1, 10) # Generator for 1 to 10 
range(10) # Generator for 0 to 10
```
    range(1, 10)


## For And If 
#### For Loop
```
{% for i in product|slice:"1:" %}
    .
    .
    .
    .
{% endfor %}
```

#### If Condition
```
{% if forloop.counter|divisibleby:3 and forloop.counter > 0 and not forloop.last %}
    .
    .
    .
    .
{% endif %}
```

#### Accessing Data
```
{{product.0.image}} # 0 index
{{i.image}}
{{ i.product_name }}
{{i.desc}}
```

#### Code
```
{% for i in product|slice:"1:"%}
    <div class="col-xs-3 col-sm-3 col-md-3">
    <div class="card" style="width: 18rem;">
        <img src='/media/{{i.image}}' class="card-img-top" alt="...">
        <div class="card-body">
        <h5 class="card-title">{{i.product_name}}</h5>
        <p class="card-text">{{i.desc}}</p>
        <a href="#" class="btn btn-primary">Add To Cart</a>
        </div>
    </div>
    </div>
{% if forloop.counter|divisibleby:3 and forloop.counter > 0 and not forloop.last %}
    </div><div class="carousel-item">
{% endif %}
{% endfor %}
```