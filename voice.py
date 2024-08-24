
import os , requests, re , json
apiKey = "c389d68b-459e-4db2-af3a-7a83b07be465"
def apiFunction(usersInputObj):
    inputsArray = [{"id": "{input_1}", "label": "Enter text", "type": "text"}]
    prompt = "Generate a realistic voice from this text {input_1}"
    filesData, textData = {}, {}
    for inputObj in inputsArray:
        inputId = inputObj['id']
        if inputObj['type'] == 'text':
            prompt = prompt.replace(inputId, usersInputObj[inputId])
        elif inputObj['type'] == 'file':
            path = usersInputObj[inputId]
            file_name = os.path.basename(path)
            f = open(path, 'rb')
            filesData[inputId] = f

    textData['details'] = json.dumps({'appname': 'voice generator ai','prompt': prompt,'documentId': 'no-embd-type','appId' : '66c8b1ec64d827b744a2a141' , 'memoryId' : '','apiKey': apiKey})
    response = requests.post('https://apiappstore.guvi.ai/api/output', data=textData, files=filesData)
    output = response.json()
    return output['output']
usersInputObj = {'{input_1}' : input("Enter text "),}
output = apiFunction(usersInputObj)
url_regex = r'http://localhost:7000/'
replaced_string = re.sub(url_regex,'https://apiappstore.guvi.ai/' , output)
print(replaced_string)
