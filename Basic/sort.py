




data = [
    {
        "exercise": 8,
        "timestamp": 5
    },
    {
        "exercise": 8,
        "timestamp": 2
    },
    {
        "exercise": 8,
        "timestamp": 3
    },
    {
        "exercise": 5,
        "timestamp": 1
    },
    {
        "exercise": 5,
        "timestamp": 4
    }
]

data = sorted(data, key=lambda k: k['timestamp'])

print(data)
