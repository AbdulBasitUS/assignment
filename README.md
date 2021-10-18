
# Pizza API

This application stores information about different types of pizza


## Installation

Create a virtual environment to install dependencies in and activate it:

```bash
virtualenv env
env/Scripts/activate
```
Make sure ```(env)``` is  in front of the prompt. This indicates that virtual environment is activated.

Then intall the dependencies:

```bash
pip install -r requirements.txt
```
Once ```pip``` has finished downloading the dependencies.
Migrate the app.

```bash
python manage.py makemigrations
python manage.py migrate
```

After Migration you can run the app.

```bash
python manage.py runserver
```
Connect to the API using Postman on port 8000.

## API Documentation

For better user experience you can go to:
```http
  GET http://localhost:8000/swagger/
  GET http://localhost:8000/redoc/
```

### Pizza Types

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /pizzas/types | To create a new type |
| GET | /pizzas/types | To retrieve all types |
| PUT | /pizzas/types/:typeId | To edit the details of a single type |
| DELETE | /pizzas/types/:typeId | To delete a single type |

- #### Create a new pizza type

```http
  POST /pizzas/types
```

&emsp; Request:

        {
            "type_name": "round"
        }

&emsp; Response:

    Status: 201 Created
        {
            "id": 1,
            "type_name": "round"
        }

- #### Get all pizza types

```http
  GET /pizzas/types
```

&emsp; Response:

    Status: 200 OK
        [
            {
                "id": 1,
                "type_name": "round"
            },
            {
                "id": 2,
                "type_name": "square"
            }
        ]

- #### Edit a pizza type

```http
  PUT /pizzas/types/1
```

&emsp; Request:

        {
            "type_name": "Round"
        }

&emsp; Response:

    Status: 202 Accepted
        {
            "id": 1,
            "type_name": "Round"
        }

- #### Delete a pizza type

```http
  DELETE /pizzas/types/2
```

&emsp; Response:

    Status: 204 No Content

&nbsp;  
### Pizza Sizes

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /pizzas/sizes | To create a new size |
| GET | /pizzas/sizes | To retrieve all sizes |
| PUT | /pizzas/sizes/:sizeId | To edit the details of a single size |
| DELETE | /pizzas/sizes/:sizeId | To delete a single type |


- #### Create a new pizza size

```http
  POST /pizzas/sizes
```

&emsp; Request:

        {
            "size_name": "small"
        }

&emsp; Response:

    Status: 201 Created
        {
            "id": 1,
            "type_name": "small"
        }

- #### Get all pizza sizes

```http
  GET /pizzas/sizes
```

&emsp; Response:

    Status: 200 OK
        [
            {
                "id": 1,
                "size_name": "small"
            },
            {
                "id": 2,
                "size_name": "medium"
            }
        ]

- #### Edit a pizza size

```http
  PUT /pizzas/sizes/2
```

&emsp; Request:

        {
            "size_name": "Medium"
        }

&emsp; Response:

    Status: 202 Accepted
        {
            "id": 2,
            "size_name": "Medium"
        }

- #### Delete a pizza size

```http
  DELETE /pizzas/sizes/2
```

&emsp; Response:

    Status: 204 No Content

### Pizza Toppings

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /pizzas/toppings | To create a new topping |
| GET | /pizzas/toppings  | To retrieve all toppings |
| PUT | /pizzas/toppings/:toppingId  | To edit the details of a single topping |
| DELETE | /pizzas/toppings/:toppingId | To delete a single topping |


- #### Create a new pizza topping

```http
  POST /pizzas/toppings
```

&emsp; Request:

        {
            "topping_name": "Onion"
        }

&emsp; Response:

    Status: 201 Created
        {
            "id": 1,
            "topping_name": "Onion"
        }

- #### Get all pizza toppings

```http
  GET /pizzas/toppings
```

&emsp; Response:

    Status: 200 OK
        [
            {
                "id": 1,
                "topping_name": "Onion"
            },
            {
                "id": 2,
                "topping_name": "Tomato"
            },
            {
                "id": 3,
                "topping_name": "Corn"
            }
        ]
- #### Edit a pizza size

```http
  PUT /pizzas/toppings/2
```

&emsp; Request:

        {
            "topping_name": "Cheeze"
        }

&emsp; Response:

    Status: 202 Accepted
        {
            "id": 2,
            "topping_name": "Cheeze"
        }

- #### Delete a pizza topping

```http
  DELETE /pizzas/topping/3
```

&emsp; Response:

    Status: 204 No Content


### Pizza 

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /pizzas/pizzas | To create a new pizza |
| GET | /pizzas/pizzas | To retrieve all pizzas |
| PUT | /pizzas/pizzas/:pizzaId  | To edit the details of a single pizza |
| PATCH | /pizzas/pizzas/:pizzaId  | To edit partially the details of a single pizza |
| DELETE | /pizzas/pizzas/:pizzaId | To delete a single pizza |


- #### Create a new pizza

```http
  POST /pizzas/pizzas
```

&emsp; Request:

        {
            "type": 1,
            "size": 2,
            "toppings": [1, 2]
        }

&emsp; Response:

    Status: 201 Created
        {
            "id": 1,
            "type": {
                "id": 1,
                "type_name": "Round"
            },
            "size": {
                "id": 2,
                "size_name": "Medium"
            },
            "toppings": [
                {
                    "id": 1,
                    "topping_name": "Onion"
                },
                {
                    "id": 2,
                    "topping_name": "Tomato"
                }
            ]
        }

- #### Get all pizzas

```http
  GET /pizzas/pizzas
```

&emsp; Response:

    Status: 200 OK
        [
            {
                "id": 1,
                "type": {
                    "id": 1,
                    "type_name": "Round"
                },
                "size": {
                    "id": 2,
                    "size_name": "Medium"
                },
                "toppings": [
                    {
                        "id": 1,
                        "topping_name": "Onion"
                    },
                    {
                        "id": 2,
                        "topping_name": "Tomato"
                    }
                ]
            },
            {
                "id": 3,
                "type": {
                    "id": 2,
                    "type_name": "square"
                },
                "size": {
                    "id": 2,
                    "size_name": "Medium"
                },
                "toppings": [
                {
                    "id": 3,
                    "topping_name": "Corn"
                }
                ]
            },
        ]
- #### Edit a pizza

```http
  PUT /pizzas/pizzas/3
```

&emsp; Request:

        {
            "type": 2,
            "size": 1,
            "toppings": [1, 3]
        }

&emsp; Response:

    Status: 202 Accepted
        {
            "id": 3,
            "type": {
                "id": 2,
                "type_name": "square"
            },
            "size": {
                "id": 1,
                "size_name": "small"
            },
            "toppings": [
                {
                    "id": 1,
                    "topping_name": "Onion"
                },
                {
                    "id": 3,
                    "topping_name": "Corn"
                }
            ]
        }

```http
  PATCH /pizzas/pizzas/3
```

&emsp; Request:

        {
            "toppings": [1, 2]
        }

&emsp; Response:

    Status: 202 Accepted
        {
            "id": 3,
            "type": {
                "id": 2,
                "type_name": "square"
            },
            "size": {
                "id": 1,
                "size_name": "small"
            },
            "toppings": [
                {
                    "id": 1,
                    "topping_name": "Onion"
                },
                {
                    "id": 2,
                    "topping_name": "Tomato"
                }
            ]
        }

- #### Delete a pizza

```http
  DELETE /pizzas/pizza/3
```

&emsp; Response:

    Status: 204 No Content

- #### Filtering the pizzas based on size and type

```http
  GET /pizzas/pizza?type=1&size=2
```
&emsp; Response:

    Status: 200 OK
        [
            {
                "id": 1,
                "type": {
                    "id": 1,
                    "type_name": "Round"
                },
                "size": {
                    "id": 2,
                    "size_name": "Medium"
                },
                "toppings": [
                    {
                        "id": 1,
                        "topping_name": "Onion"
                    },
                    {
                        "id": 2,
                        "topping_name": "Tomato"
                    }
                ]
            }
        ]

- #### Filtering the pizzas based on type only

```http
  GET /pizzas/pizza?type=1
```
&emsp; Response:

    Status: 200 OK
        [
            {
                "id": 1,
                "type": {
                    "id": 1,
                    "type_name": "Round"
                },
                "size": {
                    "id": 2,
                    "size_name": "Medium"
                },
                "toppings": [
                    {
                        "id": 1,
                        "topping_name": "Onion"
                    },
                    {
                        "id": 2,
                        "topping_name": "Tomato"
                    }
                ]
            }
        ]


- #### Filtering the pizzas based on size only

```http
  GET /pizzas/pizza?size=1
```
&emsp; Response:

    Status: 200 OK
        [
            {
                "id": 3,
                "type": {
                    "id": 2,
                    "type_name": "square"
                },
                "size": {
                    "id": 2,
                    "size_name": "Medium"
                },
                "toppings": [
                  {
                      "id": 3,
                      "topping_name": "Corn"
                  }
                ]
            }
        ]
