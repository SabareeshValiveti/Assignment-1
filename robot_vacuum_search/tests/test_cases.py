def get_tests():
    return [
        {
            "name": "Small Grid",
            "grid": [
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ],
            "start": (1,1),
            "dirty": {(0,0),(2,2)}
        },
        {
            "name": "Medium Grid",
            "grid": [
                [0,0,0,0],
                [0,1,1,0],
                [0,0,0,0],
                [0,0,0,0]
            ],
            "start": (0,0),
            "dirty": {(3,3),(2,1),(0,3)}
        }
    ]
