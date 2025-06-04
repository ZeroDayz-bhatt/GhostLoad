import threading
import requests
import time

def format_target(input_str):
    if not input_str.startswith("http://") and not input_str.startswith("https://"):
        return "http://" + input_str
    return input_str

def send_requests(target, count):
    for i in range(count):
        try:
            response = requests.get(target)
            print(f"[{i+1}] ✅ Sent request to {target} — Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{i+1}] ❌ Request failed — {e}")
        time.sleep(0.1)

def start_attack(target, threads, requests_per_thread):
    print(f"\n🚀 Starting test on: {target}")
    print(f"➡️ Threads: {threads}, Requests per thread: {requests_per_thread}\n")

    thread_list = []

    for i in range(threads):
        t = threading.Thread(target=send_requests, args=(target, requests_per_thread))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print("\n✅ Load test complete.")

if __name__ == "__main__":
    print("👋 Load Tester Tool (For Testing Only)")

    choice = input("🧭 Test on what? (1 = Domain, 2 = IP): ").strip()

    if choice == "1":
        raw = input("🔗 Enter domain name (e.g., example.com): ").strip()
    elif choice == "2":
        raw = input("🌐 Enter IP address (e.g., 192.168.1.1): ").strip()
    else:
        print("❌ Invalid choice. Exiting.")
        exit()

    target = format_target(raw)

    try:
        threads = int(input("🧵 Number of threads: ").strip())
        requests_per_thread = int(input("🔁 Requests per thread: ").strip())
    except ValueError:
        print("❌ Invalid thread/request number. Exiting.")
        exit()

    start_attack(target, threads, requests_per_thread)
