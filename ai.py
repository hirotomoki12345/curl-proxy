from flask import Flask, request, jsonify
from gemini import Gemini
import os


app = Flask(__name__)

cookies = {
    "_ga": "GA1.1.1485629292.1712635609",
    "_ga_WC57KJ50ZZ": "GS1.1.1712635608.1.0.1712635609.0.0.0",
    "NID": "513",
    "SID": "g.a000iQiRzGDqqCHVRHpazfn3mKSX-Fl8C_xM_sgHu1EqW_yzWEbsUlNcSp6zWiwqqbIOxumG8wACgYKAR4SAQASFQHGX2MiTt0DXrP30CdFP8pXx1IRtRoVAUF8yKpkc1fN_lDBCkqa0NsJymlC0076",
    "__Secure-1PSID": "g.a000iQiRzGDqqCHVRHpazfn3mKSX-Fl8C_xM_sgHu1EqW_yzWEbs-iDDYzm_3dMBvORrmn7iNQACgYKAU4SAQASFQHGX2Mi-tv4LFdS9oT-_cnVH1-ejxoVAUF8yKq1aSCoJsifUrGwqGFKz_Li0076",
    "__Secure-3PSID": "g.a000iQiRzGDqqCHVRHpazfn3mKSX-Fl8C_xM_sgHu1EqW_yzWEbs5WYNdVNvycsU6ZB6vMz4JQACgYKAbkSAQASFQHGX2Mi05HCg4u-2tYu9GHnkwAjDxoVAUF8yKp09dK63Jge0Uwx00G8DA3a0076",
    "HSID": "AVm8ITHR37q7Jrt6_",
    "SSID": "A5_3HRyb3gZ2dr7rz",
    "APISID": "9z3AsuBe6bEZ7XTe/AR0sq77a2d083CEC6",
    "SAPISID": "59Yaz8GgnOV6s7p7/Apv_XqsLz6facQXOJ",
    "__Secure-1PAPISID": "59Yaz8GgnOV6s7p7/Apv_XqsLz6facQXOJ",
    "__Secure-3PAPISID": "59Yaz8GgnOV6s7p7/Apv_XqsLz6facQXOJ",
    "SIDCC": "AKEyXzVb--PWTsUC6EHHcPbCVpQ9GAVuxGG29QUgbxgszyhe0qH-uRdFtv7a8F835idWTyfj",
    "__Secure-1PSIDCC": "AKEyXzX3eP6Doj3viFHTPzLP_2BrSkPt-wOr3vurEOnHBw2TD66Q62U3QwovWfkxNGO9ohEJXg",
    "__Secure-3PSIDCC": "AKEyXzXecrzPyjtS898k1-E3BmnXLcZkPHlFisSKl5cHP0ZSHBZeCMJQmucpFtUVBmXjSI5KQQ"
}

GeminiClient = Gemini(cookies=cookies)

@app.route('/query', methods=['GET'])
def query_gemini():
    question = request.args.get('question')
    if question:
        response_text, response_status = GeminiClient.send_request(question)
        return jsonify({'response': response_text})

    else:
        return jsonify({'error': 'No question provided'})

if __name__ == '__main__':
    app.run(debug=True)
