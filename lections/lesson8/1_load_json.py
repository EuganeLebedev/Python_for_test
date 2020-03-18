import json

result = json.loads('{"test1": 1, "test2": 2}')
print(result['test1'])

with open("test.json") as f:
    content = f.read()

    result = json.loads(content)

    print(result)

    result["prob1"] = 123321123321

    with open("result.json", mode="w") as f2:
        json_content = json.dumps(result)

        f2.write(json_content)

