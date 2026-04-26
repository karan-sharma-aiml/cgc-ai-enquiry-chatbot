import requests

# ✅ Backend URL (IMPORTANT - port match karo)
URL = "http://127.0.0.1:8001/chat"

# ✅ Test cases (input → expected keyword in response)
test_cases = [
    {"input": "bca fees kya hai", "expected": "50"},
    {"input": "btech fees kitni hai", "expected": "80"},
    {"input": "hostel hai kya", "expected": "hostel"},
    {"input": "placement hota hai kya", "expected": "placement"},
    {"input": "library hai kya", "expected": "library"},
    {"input": "courses kya hai", "expected": "BCA"},
    {"input": "random question xyz", "expected": "Sorry"}
]

def test_chatbot():
    print("🚀 Starting Chatbot Tests...\n")
    
    correct = 0

    for i, test in enumerate(test_cases, start=1):
        try:
            response = requests.post(URL, json={
                "message": test["input"],
                "user_id": "test_user"
            })

            if response.status_code == 200:
                reply = response.json().get("reply", "")
                
                print(f"🔹 Test {i}")
                print("👉 Input:", test["input"])
                print("🤖 Bot:", reply)

                if test["expected"].lower() in reply.lower():
                    print("✅ PASS\n")
                    correct += 1
                else:
                    print("❌ FAIL\n")

            else:
                print(f"❌ API Error: {response.status_code}\n")

        except Exception as e:
            print(f"❌ Exception: {e}\n")

    # 🎯 Accuracy
    total = len(test_cases)
    accuracy = (correct / total) * 100

    print("===================================")
    print(f"🎯 Accuracy: {accuracy:.2f}% ({correct}/{total})")
    print("===================================")


if __name__ == "__main__":
    test_chatbot()