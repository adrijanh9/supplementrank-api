import json

def dictToJson(d):

    jobject = json.dumps(d, indent=4)

    return jobject